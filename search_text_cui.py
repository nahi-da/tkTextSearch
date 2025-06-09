import os
from tkinter.filedialog import askdirectory
import traceback

ignore_dirs = (".venv", ".pyenv", ".conda")

def search_string_in_files(directory, search_string, target_ext):
    # 指定したディレクトリ内のすべてのファイルを再帰的に探索
    for root, _, files in os.walk(directory):
        if any(ignore_dir in root for ignore_dir in ignore_dirs):
            continue
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if not target_ext == "":
                if os.path.splitext(file_path)[1] == target_ext:
                    # 読み取り可能かどうかを確認
                    if os.access(file_path, os.R_OK):
                        try:
                            with open(file_path, 'r', encoding='utf-8') as file:
                                line_number = 0
                                for line in file:
                                    line_number += 1
                                    if search_string in line:
                                        print("-" * 50)
                                        print(f"ファイルパス: {file_path}\n行番号: {line_number}\n行内容: {line.strip()}")
                                        print()
                        except UnicodeDecodeError:
                            pass

if __name__ == "__main__":
    folder = askdirectory()
    print("ディレクトリ > " + folder)
    keyword = input("検索したい文字列 > ")
    filetype = input("ファイルの拡張子 > ")
    try:
        search_string_in_files(folder, keyword, filetype)
    except Exception as e:
        traceback.print_exception(e)
    
    input("続行するにはEnterを押してください... ")
