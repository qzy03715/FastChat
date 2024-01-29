import pandas as pd

# 读取Excel文件
input_file_path = "E:\\RjDir\\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\\Desktop\\file\\领航员全面测评数据集_参数自动化评测测试表_参数自动化评测.xlsx"
output_file_path = "E:\\RjDir\\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\\Desktop\\file\\output.xlsx"

# 读取Excel文件
df = pd.read_excel(input_file_path)

# 处理背景知识列
def process_background_knowledge(background_knowledge):
    # 解析背景知识列，假设每行都是一个表格，格式为 | 列名 | 数据 |
    lines = background_knowledge.split('\n')
    model_name = lines[0].split('|')[1].strip()
    model_info = lines[1].split('|')[1].strip()
    # 构建新的格式
    return f"型号：{model_name}, {model_info}"

# 应用函数到每一行
df['背景知识'] = df['背景知识'].apply(process_background_knowledge)

# 保存到新的Excel文件
df.to_excel(output_file_path, index=False)

print("文件已生成")