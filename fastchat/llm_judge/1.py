#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen-1_8B-Chat')



'''
python gen_model_answer.py --model-path /home/featurize/Qwen-1_8B-Chat --model-id Qwen-1_8B-Chat

python gen_judgment.py --model-list Qwen-1_8B-Chat

python show_result.py

'''