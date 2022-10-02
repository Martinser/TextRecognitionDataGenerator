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

def handle_file(path_old,path_new):
    '''
        处理码表，把在Unicode 扩展E~F的不能生成的字符去除
        path_old:初赛B榜码表.txt所在的路径
        path_new:生成的新码表所在的路径
    '''
    path1 =path_old
    path2 =path_new
    en_list=[]
    all_list=[]
    with open(path1,'r',encoding='utf-8', errors="ignore")as f:
        with open(path2, 'w', encoding='utf-8', errors="ignore", ) as f2:
            content=f.readlines()
            for i in range(len(content)):
                temp=content[i][0].encode()
                en_list.append(temp)
                all_list.append(content[i][0])
                if temp < b'\xf0\xab\xa0\xa0':#判断其utf-8编码是否符合要求
                    f2.writelines(content[i][0]+'\n')


if __name__ == '__main__':
    args = parse_arguments()
    file_path=args.file_path#'F:/TextRecognitionDataGenerator-master/'
    handle_file(file_path+'初赛B榜码表.txt',file_path+'trdg/dicts/cn.txt')
    print("Dict has created in "+file_path+'trdg/dicts/cn.txt successfully')