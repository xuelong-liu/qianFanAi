# import os
# import qianfan
#
# os.environ["QIANFAN_ACCESS_KEY"] = "fb806e47f4d34dfc829a6e5d05655b6a"
# os.environ["QIANFAN_SECRET_KEY"] = "b9cce6d94e49480696d2281812d7dfd6"
#
# # 接下来就可以调用 SDK 的所有功能
# chat = qianfan.ChatCompletion()
# resp = chat.do(messages=[{"role": "user", "content": "你好，千帆"}])
#
# print(resp["result"])

import os
import qianfan

# 动态获取最新模型列表依赖 IAM Access Key 进行鉴权，使用应用 AK 鉴权时不支持该功能
os.environ["QIANFAN_ACCESS_KEY"] = "fb806e47f4d34dfc829a6e5d05655b6a"
os.environ["QIANFAN_SECRET_KEY"] = "b9cce6d94e49480696d2281812d7dfd6"

# 模型名称可以通过 qianfan.ChatCompletion.models() 获取
# 也可以在命令行运行 qianfan chat --list-model 查看
chat_comp = qianfan.ChatCompletion(model="Yi-34B-Chat")
resp = chat_comp.do(
    messages=[{"role": "user", "content": "你好，千帆"}],
    # （可选）设置模型参数，与 API 参数一致
    top_p=0.8,
    temperature=0.9,
    penalty_score=1.0,
)

print(resp["result"])