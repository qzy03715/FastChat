import requests
import json

url = "https://lomgltui.cloud.sealos.io/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-LqvYqCdxvjhoQed2BfFd884cEd014cC792A9823f809a8820"
}
history = []
def chat(msg: str):
    history.append({ "role": "user", "content": msg})
    data = {
        "model": "gpt-4",
        "messages": history
    }
    content = requests.post(url, headers=headers, data=json.dumps(data)).json()["choices"][0]["message"]["content"]
    history.append({ "role": "assistant", "content": content})
    return content
print(chat("nihao"))



# '''
# #模型下载
# from modelscope import snapshot_download
# model_dir = snapshot_download('qwen/Qwen-1_8B-Chat')
# '''


# '''
# 下面是命令行指令

# 清华园
# -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

# 获取模型答案
# python gen_model_answer.py --model-path /home/featurize/Qwen-1_8B-Chat --model-id Qwen-1_8B-Chat

# 生成打分
# python gen_judgment.py --model-list Qwen-1_8B-Chat
# python gen_judgment.py --model-list Ruijie_Navigator

# 将打分进行汇总
# python show_result.py


# 遇到的一个问题：需要创建两个虚拟环境
  
#   qwen的用pydantic 2.1.1  
#     #pip uninstall pydantic 
#     #pip install pydantic 2.1.1
 
#   fastchat要用pydantic<2.0.0的
#     #pip install fastapi uvicorn pydantic==2.1.1 openai sse_starlette

    
# {"name": "single-v1", "type": "single", "system_prompt": "你是个能干的助手", "prompt_template": "[Instruction]\n请充当公正的法官,评估人工智能助理对下面显示的用户问题的回答质量。你的评估应该考虑诸如帮助性、相关性、准确性、深度和回答的细节水平等因素。通过提供简短的解释开始评估。尽可能客观。在提供解释后,您必须严格按照以下格式对回复进行评分,评分范围为1到100: \"[[rating]]\", for example: \"Rating: [[5]]\".\n\n[Question]\n{question}\n\n[The Start of Assistant's Answer]\n{answer}\n[The End of Assistant's Answer]", "description": "Prompt for general questions", "category": "general", "output_format": "[[rating]]"}
# {"name": "single-math-v1", "type": "single", "system_prompt": "你是个能干的助手", "prompt_template": "[Instruction]\n请作为一名公正的法官,评估人工智能助理对下面显示的用户问题的回答质量。你的评估应该考虑正确性和有用性。你将得到一个参考答案和助理的答案。通过将助理的答案与参考答案进行比较来开始评估。识别并纠正任何错误。尽可能客观。在提供解释后,您必须严格按照以下格式对回复进行评分,评分范围为1到100: \"[[rating]]\", for example: \"Rating: [[5]]\".\n\n[Question]\n{question}\n\n[The Start of Reference Answer]\n{ref_answer_1}\n[The End of Reference Answer]\n\n[The Start of Assistant's Answer]\n{answer}\n[The End of Assistant's Answer]", "description": "Prompt for general questions", "category": "math", "output_format": "[[rating]]"}
# {"name": "single-v1-multi-turn", "type": "single", "system_prompt": "请作为一个公正的裁判,评估人工智能助手对以下用户问题的回答质量。你的评价应该考虑的因素包括回答的有用性、相关性、准确性、深度、创造性和详细程度。你的评估应该集中在助手对第二个用户问题的回答上。通过提供一个简短的解释来开始你的评估。尽可能客观。在给出你的解释后,你必须严格按照以下格式对回答进行1到100的评分: \"[[rating]]\", for example: \"Rating: [[5]]\".\n\n", "prompt_template": "<|The Start of Assistant A's Conversation with User|>\n\n### User:\n{question_1}\n\n### Assistant A:\n{answer_1}\n\n### User:\n{question_2}\n\n### Assistant A:\n{answer_2}\n\n<|The End of Assistant A's Conversation with User|>", "description": "Prompt for general questions", "category": "general", "output_format": "[[rating]]"}
# {"name": "single-math-v1-multi-turn", "type": "single", "system_prompt": "请作为一个公正的法官,评估人工智能助手对用户问题的回答质量。您的评估应考虑正确性和有用性。你会得到一个参考答案和助理的答案。你的评价应该集中在助理对第二个问题的回答上。通过比较助理的答案和参考答案来开始你的评估。识别并纠正任何错误。尽可能客观。在给出你的解释后,你必须严格按照以下格式对回答进行1到100的评分: \"[[rating]]\", for example: \"Rating: [[5]]\".\n\n", "prompt_template": "<|The Start of Reference Answer|>\n\n### User:\n{question_1}\n\n### Reference answer:\n{ref_answer_1}\n\n### User:\n{question_2}\n\n### Reference answer:\n{ref_answer_2}\n\n<|The End of Reference Answer|>\n\n\n<|The Start of Assistant A's Conversation with User|>\n\n### User:\n{question_1}\n\n### Assistant A:\n{answer_1}\n\n### User:\n{question_2}\n\n### Assistant A:\n{answer_2}\n\n<|The End of Assistant A's Conversation with User|>", "description": "Prompt for general questions", "category": "math", "output_format": "[[rating]]"}


# '''

