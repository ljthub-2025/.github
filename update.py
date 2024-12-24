import os
import re


def update_profile_readme():
    with open('profile/README.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # 更新日記列表
    diary_list = get_diary_list()
    latest_diary = f'- [{diary_list[-1]["title"]}]({diary_list[-1]["file"]})'
    diary_list_str = '\n'.join([f'- [{diary["title"]}]({diary["file"]})' for diary in diary_list])

    with open('profile/README_TEMPLATE.md', 'r', encoding='utf-8') as file:
        template = file.read()

    return template.replace('{{ latest_diary }}', latest_diary).replace('{{ diary_list }}', diary_list_str)

def get_diary_list():
    diary_list = []
    for file in os.listdir('diaries'):
        for diary in os.listdir(f'diaries/{file}'):
            if diary.endswith('.md'):
                with open(f'diaries/{file}/{diary}', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    title = lines[0].strip('#').strip()
                    diary_list.append({"title": title, "file": f'{file}/{diary}'})
    return diary_list

if __name__ == '__main__':
    with open('profile/README.md', 'w', encoding='utf-8') as file:
        content = update_profile_readme()
        print(content)
        file.write(content)
