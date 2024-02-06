import openpyxl
import json
import os

# Excel文件路径
excel_path = r"E:\RjDir\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\Desktop\1_领航员全面测评数据集_功能配置(VPN与隧道技术)_问题汇总.xlsx"
# JSON文件路径
json_path = 'D:\\Git\FastChat\\fastchat\\llm_judge\\data\\mt_bench\\question_waiting_for_using.jsonl'

# 读取Excel文件
workbook = openpyxl.load_workbook(excel_path)
sheet = workbook.active

# 初始化计数器
question_id = 1

# 创建JSON字符串列表
json_strings = []

# 遍历Excel表格
for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过标题行
    # 获取问题和答案
    question = row[0]
    answer = row[3]

    # 创建JSON对象
    json_object = {
        "question_id": question_id,
        "category": "test",
        "turns": [question],
        "reference": [answer]
    }

    # 将JSON对象转换为字符串并添加到列表
    json_strings.append(json.dumps(json_object, ensure_ascii=False))

    # 更新计数器
    question_id += 1

# 将JSON字符串写入文件，每个字符串占一行
with open(json_path, 'w', encoding='utf-8') as json_file:
    for json_string in json_strings:
        json.dump(json_object, json_file, ensure_ascii=False)
        json_file.write(json_string + '\n')


print(f"JSON文件已生成在路径: {json_path}")