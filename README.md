# TextRecognitionDataGenerator


生成1000张正常
```
python run.py -c 1000 -l cn -w 30 -r -t 4 -or 1 -b 1  -stw 2 -sw 0 -obb 1 --output_dir you_path_/out/1/
```

2_1000张旋转  
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





This repository is built using the TextRecognitionDataGenerator(https://github.com/Belval/TextRecognitionDataGenerator)  repositories.



