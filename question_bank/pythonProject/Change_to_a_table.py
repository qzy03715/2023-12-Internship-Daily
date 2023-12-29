import json
import pandas as pd


def load_question_bank(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['topicList']


def create_excel_table(question_bank, output_path):
    # 创建一个空的 DataFrame
    df_result = pd.DataFrame(columns=['序号', '题目', '标准答案', '睿易AI的答案', '正确与否'])

    for idx, question in enumerate(question_bank, start=1):
        # 将题目和选项合并为一个字符串
        question_text = f"{question['title']}\n" + '\n'.join(question['options'])

        # 获取标准答案
        standard_answer = ', '.join(question['answer'].split(','))

        # 将题目信息添加到 DataFrame 中
        df_result = pd.concat([df_result, pd.DataFrame({
            '序号': [idx],
            '题目': [question_text],
            '标准答案': [standard_answer],
            '睿易AI的答案': [''],
            '正确与否': ['']
        })], ignore_index=True)

    # 将 DataFrame 写入 Excel 文件
    df_result.to_excel(output_path, index=False, engine='openpyxl')


# 示例用法
json_file_path = r'E:\RjDir\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\Downloads\339668.json'
output_excel_path = r'E:\RjDir\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\Downloads\output_table.xlsx'

question_bank = load_question_bank(json_file_path)
create_excel_table(question_bank, output_excel_path)
