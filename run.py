import os
import json
import sys


from pathlib import Path
cur_path = Path(__file__).parent.absolute()
from internvl_chat import chat

multiple_choice_prompt = "输入的图片为一张选择题的图片，答案应该为A、B、C、D四个选项中的其中一个，答案需从 A、B、C、D 中选其一，直接输出答案字母，勿添加任何其他内容。"
fill_in_thee_blank_prompt = "输入的图片为一张填空题的图片，你需要做的是直接输出这道题的答案，不要给出任何解释型语言，直接输出答案"
short_answr_prompt = "输入的图片为一张应用题的图片，应用题的答案需要为latex格式，即答案需要在 \bbox[] 中，方便解析。如输出结果中没有\bbox[] 信息视为格式错误,你需要做的是直接输出这道题的答案，不要给出任何解释型语言，"

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
            image_path = os.path.join(IMAGE_INPUT_DIR,content["image"])
            tag = content["tag"]
            if tag == '选择题':
                prompt = multiple_choice_prompt

            elif tag == '填空题':
                prompt = fill_in_thee_blank_prompt
            elif tag == '计算题':
                prompt = short_answr_prompt
            else:
                raise RuntimeError('问题类型错误')
            
            answer = chat(image_path,prompt)
            
            print('Answer',answer)

            data.append({
                'image':image_path,
                'tag':tag,
                'steps':'',
                'answer':answer,
            })

    if not data:
        raise RuntimeError("没有生成任何答案，data 为空")
    print(data)
    # —— 写文件 ————————————————————————————————————————
    with OUPUT_PATH.open("w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"文件保存成功 → {OUPUT_PATH}")
    print("------------------------------推理结束-----------------------------")
if __name__ == "__main__":

    inference()
