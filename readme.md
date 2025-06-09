# 百度2025国际大数据竞赛baseline

## 项目简介

基于InternVL2.5-1B模型开发

## 环境搭建

- 创建requirements.txt文件，包含InternVL模型必须的包

```
# 评测环境详见比赛界面
```

- 下载模型权重到文件夹
- 编写run.py（文件名可变）根据输入的jsonl文件问题做回答

```
import os
import json
import sys

from pathlib import Path
cur_path = Path(__file__).parent.absolute()

IMAGE_INPUT_DIR = Path(sys.argv[1])
Query_PATH = Path(sys.argv[2])
OUPUT_PATH = Path(sys.argv[3])

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

```
#运行推理脚本
${conda_path}/envs/pytorch-env/bin/python run.py \
  $IMAGE_INPUT_DIR \
  $Query_PATH \
  $OUPUT_PATH \
```

