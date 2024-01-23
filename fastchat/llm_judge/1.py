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

'''
