#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test-1 
@File    ：qwenvl_chat.py
@IDE     ：PyCharm 
@Author  ：高豫辉
@Date    ：2025/6/7 14:45 
@Desc    ：
'''

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# # torch.manual_seed(1234)

# # Note: The default behavior now has injection attack prevention off.
# tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL-Chat-Int4", trust_remote_code=True)

# # use cuda device
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat-Int4", device_map="cuda", trust_remote_code=True).eval()

def chat(image_path,question):

    # # 1st dialogue turn
    # query = tokenizer.from_list_format([
    #     {'image': image_path},
    #     {'text': question},
    # ])
    # response, history = model.chat(tokenizer, query=query, history=None)
    # print(response)
    # # 图中是一名年轻女子在沙滩上和她的狗玩耍，狗的品种可能是拉布拉多。她们坐在沙滩上，狗的前腿抬起来，似乎在和人类击掌。两人之间充满了信任和爱。
    # return response
    return 'D'