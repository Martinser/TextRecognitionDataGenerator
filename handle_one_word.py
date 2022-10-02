import os
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


def rename(path1,path2,ssr):
    '''
        生成image对应的label文件
        path1:label's path
        path2:image's path
        ssr:image命名的标记符号
    '''
    path1=path1
    path2=path2
    content_list=sorted(os.listdir(path2))

    with open(path1,'w',encoding='utf-8')as f1:
        for i in range(0,len(content_list),2):
            temp=content_list[i].split('.')[0].split('_')[0]
            temp_name='image_'+str(ssr)+'_'+str(ssr)+'_'+str(i)+'.jpg'
            os.rename(path2+content_list[i],path2+temp_name)
            f1.writelines(temp_name+','+temp+'\n')

def remove_file(path1,path2):
    '''
        移动单字图像
        path1:所有单字图像路径
        path2:原有图像的路径
    '''
    path1=path1#'/home/don/ocr/all_image/'
    path2=path2#'/home/don/ocr/936/'

    content_list = sorted(os.listdir(path2))
    for i in range(len(content_list)):
        if content_list[i].split('.')[1]=='jpg' and content_list[i].split('_')[0]!='':
            shutil.copyfile(path2+content_list[i],path1+content_list[i])

if __name__ == '__main__':
    args = parse_arguments()
    file_path = args.file_path  # 'F:/TextRecognitionDataGenerator-master/'

    for i in range(1,7):
        temp_label_path='your_path+/label/'+str(i)+'_one_word.txt'
        temp_image_path=file_path+'out/'+str(i)+'/'
        all_image_path=file_path+'out/all_image/'
        rename(temp_label_path,temp_image_path,str(i))
        remove_file(all_image_path,temp_image_path)
        print("One_word's files has created successfully ")








