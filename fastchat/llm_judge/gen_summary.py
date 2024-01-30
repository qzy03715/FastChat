import json
import os

# 输入文件路径
gpt4_single_file_path = "D:\\Git\\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\model_judgment\\Qwen-72B-Chat_single.jsonl"
question_file_path = "D:\\Git\\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\question.jsonl"
ruijie_file_path = "D:\\Git\\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\model_answer\\Ruijie_Navigator.jsonl"
gpt4_ref_file_path = "D:\\Git\\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\reference_answer\\gpt-4.jsonl"

# 输出文件路径
output_file_path = "D:\\Git\\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\summary_72b.json"

# 初始化一个字典来存储所有数据
summary_data = {}

# 读取question.jsonl文件并填充summary_data
with open(question_file_path, 'r', encoding='utf-8') as question_file:
    for line in question_file:
        entry = json.loads(line.strip())
        summary_data[entry["question_id"]] = {
            "question": entry["turns"]
        }


# 读取Ruijie_Navigator.jsonl文件，更新summary_data中的answer字段
with open(ruijie_file_path, 'r', encoding='utf-8') as ruijie_file:
    for line in ruijie_file:
        ruijie_entry = json.loads(line.strip())
        question_id = ruijie_entry["question_id"]
        if question_id in summary_data:
            # 假设每个question_id只有一个answer，所以只取第一个
            summary_data[question_id]["answer"] = ruijie_entry["choices"][0]["turns"]

# 读取gpt-4.jsonl文件，更新summary_data中的reference字段
with open(gpt4_ref_file_path, 'r', encoding='utf-8') as gpt4_ref_file:
    for line in gpt4_ref_file:
        gpt4_ref_entry = json.loads(line.strip())
        question_id = gpt4_ref_entry["question_id"]
        if question_id in summary_data:
            summary_data[question_id]["reference"] = gpt4_ref_entry["choices"][0]["turns"]

# 读取gpt-4_single.jsonl文件，更新summary_data
with open(gpt4_single_file_path, 'r', encoding='utf-8') as gpt4_single_file:
    for line in gpt4_single_file:
        gpt4_single_entry = json.loads(line.strip())
        question_id = gpt4_single_entry["question_id"]
        if question_id in summary_data:
            summary_data[question_id]["score"] = gpt4_single_entry["score"]
            summary_data[question_id]["judgment"] = gpt4_single_entry["judgment"]

# 将summary_data写入输出文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(summary_data, output_file, ensure_ascii=False, indent=4)

print(f"Data extraction and merging completed. Output saved to {output_file_path}")