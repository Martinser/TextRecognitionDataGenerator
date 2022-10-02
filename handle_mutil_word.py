# coding:utf-8
import csv
import os
import random
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import math
from PIL import Image
from tqdm import tqdm
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate synthetic text data for text recognition."
    )
    parser.add_argument(
        "--file_path",
        type=str,
        nargs="?",
        default="F:/TextRecognitionDataGenerator-master/"
    )
    return parser.parse_args()


def get_label(name,ids,ssr,font_path,file_path,path3,path4,path6,path5,path7,decide_font):
    '''
        name:图像需改的名称
        ids:图像info中的编号
        ssr:id的标记符
        font_path：生成的字典的路径
        file_path：图像所在的路径
        path3:label的info所在的路径
        path4:label的bbox所在的路径
        path5:图像备份所在的路径
        path6:label的单字训练格式所在的路径
        path7:label的字典所在的路径
        decide_font:标记符
    '''
    path= file_path
    path2=font_path
    path3=path3
    path4=path4

    copys=os.listdir(path)
    if os.path.exists(path5)==False:
        os.mkdir(path5)
    for i in copys:
        shutil.copyfile(path+i,path5+i)

    list_file=os.listdir(path)

    images_list=[]
    anno_list=[]
    #content_dic={'之':0}
    content_dic = {}

    with open(path2,'r', encoding='utf-8', errors="ignore") as f:
        contenet=f.readlines()
        for i in range(len(contenet)):
            temp=contenet[i].split('\n')[0]
            content_dic[temp]=i
    #content_dic.pop('\ufeff之')
    print(content_dic)

    ids = ids
    for i in range(0,len(list_file),2):
        dic_one = {"file_name": 'wg', "height": 720, "width": 1280, "id": 811000171}
        temp=list_file[i].split('_')
        img=Image.open(path+list_file[i])
        vs=int(temp[1].split('.')[0])+ssr
        dic_one["file_name"]=name+str(vs)+'.jpg'
        dic_one["height"]=img.height
        dic_one["width"]=img.width
        dic_one["id"]=vs
        images_list.append(dic_one)

        ssd = 1
        with open(path+list_file[i].split('.')[0]+'_boxes.txt','r', encoding='utf-8', errors="ignore") as f3:
            strs1=list_file[i].split('_')[0]
            con=f3.readlines()
            for v in range(0,len(con)):
                dic_two = {"area": 1, "iscrowd": 0, "image_id": 1, "bbox": [32, 32, 32, 32], "category_id": 2,
                           "ignore": 0, "id": 0}
                if v>=len(strs1):
                    ssd=0
                    print("Delete images with build errors!: ",images_list[-1])
                    del images_list[-1]#删除生成错误的图像
                    continue
                dic_two['area'] =img.height*img.width
                dic_two['image_id'] =vs
                temp_list=[]
                temp2=con[v].split('\n')[0].split(' ')
                temp_list.append(int(temp2[0]))
                temp_list.append(int(temp2[1]))
                temp_list.append(abs(int(temp2[2])-int(temp2[0])+1))
                temp_list.append(abs(int(temp2[3])-int(temp2[1])+1))
                dic_two['bbox'] =temp_list
                dic_two['category_id'] =content_dic[strs1[v]]
                dic_two['id']=ids
                anno_list.append(dic_two)
                ids=ids+1
        img.close()
        f3.close()

        if ssd==1:
            with open(path6, 'a', encoding='utf-8', errors="ignore") as f6:
                os.rename(path+list_file[i],path+name+str(vs)+'.jpg')
                f6.write(name+str(vs)+'.jpg'+','+list_file[i].split('_')[0]+'\n')

    with open(path3,'a',encoding='utf-8', errors="ignore") as f2:
        #f2.write("{\n")
        #f2.write('    "images": [\n')
        for i in range(len(images_list)):
            f2.write("        {\n")
            tmp=0
            for k,v in images_list[i].items():
                if tmp==0:
                    f2.writelines('            "'+k+'": "'+str(v)+'",\n')
                elif tmp==3:
                    f2.writelines('            "'+k+'": '+str(v)+'\n')
                else:
                    f2.writelines('            "'+k+'": '+str(v)+',\n')
                tmp=tmp+1
            if i==len(images_list)-1 and decide_font==6:
                f2.write("        }\n")
            else:
                f2.write("        },\n")
        #f2.writelines('    ],\n')

    with open(path4, 'a', encoding='utf-8', errors="ignore") as f4:
        #f4.writelines('    "type": "instances",\n')
        #f4.writelines('    "annotations": [\n')
        for i in range(len(anno_list)):
            f4.writelines('        {\n')
            tmp = 0
            for k, v in anno_list[i].items():
                if tmp == 0:
                    f4.writelines('            "' + k + '": ' +str(v)+ ',\n')
                elif tmp == 6:
                    f4.writelines('            "' + k + '": ' +str(v)+'\n' )
                elif tmp == 3:
                    f4.writelines('            "bbox": [\n')
                    for v_temp in range(len(v)):
                        if v_temp!=len(v)-1:
                            f4.writelines("                "+str(v[v_temp])+',\n')
                        else:
                            f4.writelines("                "+str(v[v_temp])+'\n')
                    f4.writelines('            ],\n')
                else:
                    f4.writelines('            "' + k + '": ' +str(v) + ',\n')
                tmp = tmp + 1
            if i == len(anno_list) - 1 and decide_font==6:
                f4.writelines("        }\n")
            else:
                f4.writelines("        },\n")
        #f4.write('    ],\n')

        if decide_font==6:
            with open(path7,'a',encoding='utf-8', errors="ignore") as f7:
                f7.write('    "categories": [\n')
                ssc=0
                for key,value in content_dic.items():
                    f7.writelines("        {\n")
                    dic_three={"supercategory": "none","id": 0, "name": "clothes"}
                    dic_three["id"] =value
                    dic_three["name"] =key
                    f7.writelines('            "supercategory": "'+dic_three["supercategory"]+'",\n')
                    f7.writelines('            "id": '+str(dic_three["id"])+",\n")
                    f7.writelines('            "name": "'+dic_three["name"]+'"\n')
                    if ssc == len(content_dic) - 1:
                        f7.writelines("        }\n")
                    else:
                        f7.writelines("        },\n")
                    ssc=ssc+1
                f7.writelines('    ]\n')
                f7.writelines('}\n')

    return ids


if __name__ == '__main__':
    args = parse_arguments()
    your_path = args.file_path  # 'F:/TextRecognitionDataGenerator-master/'

    ids=0
    list_cout=[-1,999,1999,2999,3999,4999]
    all_path=your_path+'label/'
    if os.path.exists(all_path)==False:
        os.mkdir(all_path)
    with open(all_path+'all_label.txt','a',encoding='utf-8') as all_f:
        file_path=your_path
        all_f.write("{\n")
        all_f.write('    "images": [\n')
        for i in range(1,7):
            ids=get_label(name='image_'+str(i)+'_',ids=ids,ssr=list_cout[i-1]+1,
                          font_path=file_path+'trdg/dicts/cn.txt',
                          file_path=file_path+'out/'+str(i)+'/',
                          path3=file_path+'label/'+str(i)+'_info.txt',
                          path4=file_path+'label/'+str(i)+'_bbox.txt',
                          path6=file_path+'label/'+str(i)+'_one.txt',
                          path5=file_path+'out/'+str(i)+'_reser/',
                          path7=file_path+'label/dict.txt',
                          decide_font=i)
            with open(file_path+'label/'+str(i)+'_info.txt','r',encoding='utf-8') as temp_f1:
                content=temp_f1.readlines()
                for j in content:
                    all_f.write(j)
        all_f.writelines('    ],\n')
        all_f.writelines('    "type": "instances",\n')
        all_f.writelines('    "annotations": [\n')
        for i in range(1,7):
            with open(file_path+'label/'+str(i)+'_bbox.txt','r',encoding='utf-8') as temp_f2:
                content=temp_f2.readlines()
                for j in content:
                    all_f.write(j)
        all_f.write('    ],\n')
        with open(file_path+'label/dict.txt','r',encoding='utf-8') as temp_f3:
            content = temp_f3.readlines()
            for j in content:
                all_f.write(j)

    print("Mutil_word's files has created successfully ")

