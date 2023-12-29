import json


def load_question_bank(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['topicList']


def format_question(question_data, question_number):
    formatted_question = f"{question_number}. {question_data['title']}\n"

    for option in question_data['options']:
        formatted_question += f"{option}\n"

    formatted_question += f"\n正确答案: {', '.join(question_data['answer'].split(','))}\n\n"

    return formatted_question


def write_formatted_questions(question_bank, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for idx, question in enumerate(question_bank, start=1):
            formatted_question = format_question(question, idx)
            output_file.write(formatted_question + '\n' * 3)


# 示例用法
json_file_path = r'E:\RjDir\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\Downloads\339666.json'
output_file_path = r'E:\RjDir\admin_d95c8884-f44c-4529-8f3b-48d5788371c1\Downloads\formatted_questions_with_answers.txt'

question_bank = load_question_bank(json_file_path)
write_formatted_questions(question_bank, output_file_path)
