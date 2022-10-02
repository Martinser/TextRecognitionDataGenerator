# TextRecognitionDataGenerator
此次比赛生成的数据一共有六种类型分别是：
  * 正常竖直
  * 左右旋转（左右旋转-15°~15°）
  * 正弦扭曲，竖直扭曲
  * 正弦扭曲，横向扭曲（针对比赛特殊类型的图像做随机位置的“先扭曲后竖直”操作）
  * 余弦扭曲，竖直扭曲
  * 余弦扭曲，横向扭曲（针对比赛特殊类型的图像做随机位置的“先扭曲后竖直”操作）


**1.生成码表**
  ```
  python handle_font_file.py --file_path you_path_/
  ```

**2.生成多字或者单字：**

**2.1生成多字**
  ```
  cd trdg
  ```
  1000张正常
  ```
  python run.py -c 1000 -l cn -w 30 -r -t 4 -or 1 -b 1  -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/1/
  ```

  1000张旋转  
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -k 15 -rk -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/2/
  ```

  1000张正弦扭曲，竖直扭曲
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 1 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/3/
  ```

  1000张正弦扭曲，横向扭曲
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 1 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/4/
  ```

  1000张余弦扭曲，竖直扭曲
  ```
  python run.py -c 10 -l cn -w 30 -r -t 4 -or 1 -b 1 -d 2 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/5/
  ```

  1000张余弦扭曲，横向扭曲
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
  
  14404张正常
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/1/
  ```

  14404张旋转  
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -k 15 -rk -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/2/
  ```

  14404张正弦扭曲，竖直扭曲
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 1 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/3/
  ```

  14404张正弦扭曲，横向扭曲
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 1 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/4/
  ```

  14404张余弦扭曲，竖直扭曲
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 2 -do 0 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/5/
  ```

  14404张余弦扭曲，横向扭曲
  ```
  python run.py -c 14404 -l cn -w 1 -t 12 -or 1 -b 1 -d 2 -do 1 -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/6/
  ```
  
  在生成上述六种数据后运行handle_one_word.py
  ```
  cd ..
  python handle_one_word.py --file_path you_path/
  ```




This repository is built using the TextRecognitionDataGenerator(https://github.com/Belval/TextRecognitionDataGenerator)  repositories.



