# from dotenv import load_dotenv, find_dotenv
# # 读取本地/项⽬的环境变量。
# # find_dotenv() 寻找并定位 .env ⽂件的路径
# # load_dotenv() 读取该 .env ⽂件，并将其中的环境变量加载到当前的运⾏环境中
# # 如果你设置的是全局的环境变量，这⾏代码则没有任何作⽤。
# _ = load_dotenv(find_dotenv())
import os
os.environ["QIANFAN_ACCESS_KEY"] = "fb806e47f4d34dfc829a6e5d05655b6a"
os.environ["QIANFAN_SECRET_KEY"] = "b9cce6d94e49480696d2281812d7dfd6"

import qianfan
def gen_wenxin_messages(prompt):
   '''
   构造⽂⼼模型请求参数 messages
   请求参数：
   prompt: 对应的⽤户提示词
   '''
   messages = [{"role": "user", "content": prompt}]
   return messages
def get_completion(prompt, model="ERNIE-Bot", temperature=0.01):
   '''
   获取⽂⼼模型调⽤结果
   请求参数：
   prompt: 对应的提示词
   model: 调⽤的模型，默认为 ERNIE-Bot，也可以按需选择 ERNIE-Bot-4 等其他模型
   temperature: 模型输出的温度系数，控制输出的随机程度，取值范围是 0~1.0，且不能
  设置为 0。温度系数越低，输出内容越⼀致。
   '''
   chat_comp = qianfan.ChatCompletion()
   message = gen_wenxin_messages(prompt)
   resp = chat_comp.do(messages=message,
   model=model,
   temperature = temperature,
   system="你是⼀名个⼈助理-⼩鲸⻥")
   return print(resp["result"])

get_completion("你好，介绍⼀下你⾃⼰")
