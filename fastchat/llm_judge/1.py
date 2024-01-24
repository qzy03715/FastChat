#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen-1_8B-Chat')



'''
下面是命令行指令

获取模型答案
python gen_model_answer.py --model-path /home/featurize/Qwen-1_8B-Chat --model-id Qwen-1_8B-Chat

生成打分
python gen_judgment.py --model-list Qwen-1_8B-Chat

将打分进行汇总
python show_result.py


遇到的一个问题：需要创建两个虚拟环境
  
  qwen的用pydantic 2.1.1  
    #pip uninstall pydantic 
    #pip install pydantic 2.1.1
 
  fastchat要用pydantic<2.0.0的
    #pip install fastapi uvicorn pydantic==2.1.1 openai sse_starlette


'''
