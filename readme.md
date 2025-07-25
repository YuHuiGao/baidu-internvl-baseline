# 百度2025国际大数据竞赛baseline

## 项目简介

基于InternVL2.5-1B模型开发

## 环境搭建

初版环境与更新后的环境不同，目前评测环境已更新！
- 创建requirements.txt文件，包含InternVL模型必须的包

新版环境（当前环境）
```
Python 3.10
CUDA 12.6
torch                   2.6.0
torchaudio              0.21.0
torchvision             2.6.0
```

旧版环境
```
Python 3.10
CUDA 11.6

Package                 Version
----------------------- -----------
absl-py                 2.0.0
attrs                   23.1.0
cachetools              5.3.1
certifi                 2023.7.22
charset-normalizer      3.3.0
coloredlogs             15.0.1
contourpy               1.1.1
cycler                  0.12.1
exceptiongroup          1.1.3
flatbuffers             23.5.26
fonttools               4.43.1
google-auth             2.23.2
google-auth-oauthlib    1.0.0
grpcio                  1.59.0
humanfriendly           10.0
idna                    3.4
imageio                 2.31.5
importlib-metadata      6.8.0
iniconfig               2.0.0
joblib                  1.3.2
kiwisolver              1.4.5
lazy_loader             0.3
lightgbm                4.1.0
Markdown                3.5
MarkupSafe              2.1.3
matplotlib              3.8.0
mpmath                  1.3.0
networkx                3.1
numpy                   1.26.0
oauthlib                3.2.2
onnx                    1.14.1
onnxruntime-gpu         1.16.0
opencv-python           4.8.1.78
packaging               23.2
pandas                  2.1.1
Pillow                  10.0.1
pip                     23.2.1
pluggy                  1.3.0
protobuf                4.24.4
py                      1.11.0
pyasn1                  0.5.0
pyasn1-modules          0.3.0
pyparsing               3.1.1
pytest                  7.4.2
python-dateutil         2.8.2
pytz                    2023.3.post1
PyWavelets              1.4.1
requests                2.31.0
requests-oauthlib       1.3.1
rsa                     4.8
scikit-image            0.22.0
scikit-learn            1.3.1
scipy                   1.11.3
seaborn                 0.13.0
setuptools              68.0.0
six                     1.16.0
sympy                   1.12
tensorboard             2.14.1
tensorboard-data-server 0.7.1
tensorboard-plugin-wit  1.8.1
threadpoolctl           3.2.0
tifffile                2023.9.26
toml                    0.10.2
tomli                   2.0.1
torch                   1.12.0
torchaudio              0.12.0
torchvision             0.13.0
typing_extensions       4.8.0
tzdata                  2023.3
urllib3                 2.0.6
Werkzeug                3.0.0
wheel                   0.41.2
xgboost                 2.0.0
zipp                    3.17.0
```

- 下载模型权重到文件夹
- 编写run.py（文件名可变）根据输入的jsonl文件问题做回答

```
import os
import json
import sys

from pathlib import Path
cur_path = Path(__file__).parent.absolute()

#第一种获取方式
IMAGE_INPUT_DIR = Path(sys.argv[1])
Query_PATH = Path(sys.argv[2])
OUPUT_PATH = Path(sys.argv[3])

#第二种获取方式
IMAGE_INPUT_DIR = os.environ["IMAGE_INPUT_DIR"]
Query_PATH = os.environ["QUERY_PATH"]
OUPUT_PATH = os.environ["OUPUT_PATH"]



def inference():
    print("------------------------------开始推理-----------------------------")
    # 保证输出目录存在
    OUPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    base_path = os.path.dirname(os.path.abspath(__file__))
    data = []

    with open(Query_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            # 解析每行JSON数据
            content = json.loads(line)
            # 图片文件路径
            image_path = os.path.join(IMAGE_INPUT_DIR,content["image"])
            # 问题标签，选择题、填空题、计算题
            tag = content["tag"]
			#下面填写你的模型处理逻辑
			......
            #把答案写入OUPUT_PATH的jsonl文件中
            ......
            
if __name__ == "__main__":

    inference()
```

- 编写run.sh文件
pytorch提交界面的run.sh脚本内容与paddlepaddle赛道run.sh脚本内容不同，请选手注意！！！
使用错误的环境将导致分数无效！！！

pytorch环境run.sh脚本
```
#运行推理脚本
${conda_path}/envs/pytorch-env/bin/python run.py \
  $IMAGE_INPUT_DIR \
  $QUERY_PATH \
  $OUPUT_PATH \
```

paddlepaddle环境run.sh脚本
paddlepaddle赛道禁用pytorch，违规将导致分数无效！！！
```
#运行推理脚本
${conda_path}/envs/paddlepaddle-env/bin/python run.py \
  $IMAGE_INPUT_DIR \
  $QUERY_PATH \
  $OUPUT_PATH \
```




