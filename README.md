# TextRecognitionDataGenerator
此次比赛生成的数据一共有六种类型分别是：
  * 正常竖直
  * 左右旋转（左右旋转-15°~15°）
  * 正弦扭曲，竖直扭曲
  * 正弦扭曲，横向扭曲（针对比赛特殊类型的图像做随机位置的“先扭曲后竖直”操作）
  * 余弦扭曲，竖直扭曲
  * 余弦扭曲，横向扭曲（针对比赛特殊类型的图像做随机位置的“先扭曲后竖直”操作）

所有生成的图像均采用：
*  码表中的字符均匀随机生成
*  字符宽度有3种均匀随机变换
* 字体有6种均匀随机变换
* 字体文件如果不包含当前单字的字形，采用SourceHanSans-Normal.ttf和SimSun-ExtB.ttf字体文件依次判定生成
* 图像中每一个单字的大小在 [68,96]之间生成
* 图像中每一个单字的位置在 [0.81,1.1]之间变换


生成图像的参数：
  *   `-c`：生成图像的数量
  *  `-l`：生成图像的语言
  *  `-w`：每一张图像中所包含字符的数量
  *  `-r`：如果`-w`参数n生效，则每一张字符的数量为 [1,n] 之间
  * `-t`：为CPU使用的线程数量
  * `-or`：0: 水平排列，1: 竖直排列
  * `-b`：生成图像的背景，1: 空白
  * `-stw`：定义字体的宽度
  * `-sw`：定义字符之间的间距
  * `-obb`：是否生成对应bbox文件
  * `-d`：对字符扭曲，0: None (Default), 1: Sine wave, 2: Cosine wave, 3: Random"
  * `-do`：如果`-d`参数生效，则定义对字符在哪一个方向上扭曲，0: Vertical (Up and down), 1: Horizontal (Left and Right), 2: Both
  * `--output_dir`:输出的位置


**1.生成码表**
  ```
  python handle_font_file.py --file_path you_path_/
  ```

**2.生成多字或者单字图像**

**2.1生成多字**
  ```
  cd trdg
  ```
  1000张正常图像
  ```
  python run.py -c 1000 -l cn -w 30 -r -t 4 -or 1 -b 1  -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/1/
  ```

  1000张旋转图像  
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -k 15 -rk -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/2/
  ```

  1000张正弦扭曲、竖直扭曲图像
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 1 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/3/
  ```

  1000张正弦扭曲、横向扭曲图像
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 1 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/4/
  ```

  1000张余弦扭曲、竖直扭曲图像
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 2 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/5/
  ```

  1000张余弦扭曲、横向扭曲图像
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 2 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/6/
  ```
  
  在生成上述六种数据后运行handle_mutil_word.py
  ```
  cd ..
  python handle_mutil_word.py --file_path you_path/
  ```
  
**2.2生成单字**
  ```
  cd trdg
  ```
  
  14404张正常图像
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/1/
  ```

  14404张旋转图像  
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -k 15 -rk -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/2/
  ```

  14404张正弦扭曲、竖直扭曲图像
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 1 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/3/
  ```

  14404张正弦扭曲、横向扭曲图像
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 1 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/4/
  ```

  14404张余弦扭曲、竖直扭曲图像
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 2 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/5/
  ```

  14404张余弦扭曲、横向扭曲图像
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 2 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/6/
  ```
  
  在生成上述六种数据后运行handle_one_word.py
  ```
  cd ..
  python handle_one_word.py --file_path you_path/
  ```

字体相关文件下载链接
*  [SimSun-ExtB.ttf](http://xiazaiziti.com/210549.html)
* [SourceHanSans-Normal.ttf](https://github.com/Belval/TextRecognitionDataGenerator/tree/master/trdg/fonts/cn)
* [biaosong.ttf](https://github.com/Martinser/TextRecognitionDataGenerator/releases/tag/font1.0)
* [cao.ttf]()
* [hang.TTF]()
* [kai.TTF]()
* [li.TTF]()

This repository is built using the [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator) repositories.



