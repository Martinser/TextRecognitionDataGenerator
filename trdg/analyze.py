import os
import shutil

def mkdir_file():
    path='/home/don/ocr/mistake/'
    path2='/home/don/ocr/930/'
    cn_path='/home/don/ocr/cn.txt'
    file_list=os.listdir(path2)
    file_list=sorted(file_list)


    with open(cn_path,'r',encoding='utf-8') as f1:
        content=f1.readlines()
        for i in range(len(content)):
            temp_name=content[i].split('\n')[0]
            if os.path.exists(path+temp_name)==False:
                os.mkdir(path+temp_name)

        print(len(os.listdir(path)))

        for j in range(0,len(file_list),2):
            temp_name=file_list[j]
            temp_name2=file_list[j].split('.')[0].split('_')[0]
            if temp_name2!='齃':
                shutil.copyfile(path2+temp_name,path+temp_name2+'/'+temp_name)

def choose(path,path2):
    path=path
    path2=path2
    content=os.listdir(path)
    cout=0
    with open(path2,'w',encoding='utf-8') as f1:
        for i in range(len(content)):
            temp=path+content[i]
            if len(os.listdir(temp))==0:
                f1.writelines(content[i]+'\n')
                cout=cout+1
    print(cout)


def rename(path1,path2,ssr):
    path1=path1
    path2=path2
    content_list=sorted(os.listdir(path2))
    print(content_list)

    with open(path1,'w',encoding='utf-8')as f1:
        for i in range(0,len(content_list),2):
            temp=content_list[i].split('.')[0].split('_')[0]
            temp_name='image_'+str(ssr)+'_'+str(ssr)+'_'+str(i)+'.jpg'
            os.rename(path2+content_list[i],path2+temp_name)
            f1.writelines(temp_name+','+temp+'\n')


def maybe():
    path2='/home/don/ocr/936/'
    path1='/home/don/ocr/all_image/'
    content_list = sorted(os.listdir(path2))
    for i in range(len(content_list)):
        if content_list[i].split('.')[1]=='jpg':
            shutil.copyfile(path2+content_list[i],path1+content_list[i])


if __name__ == '__main__':
    #rename('/home/don/ocr/label/6.txt','/home/don/ocr/936/',6)
    # mkdir_file()
    #choose('/home/don/ocr/mistake/','/home/don/ocr/mistake_label/1.txt')
    maybe()







