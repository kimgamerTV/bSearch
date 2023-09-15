import os
import re
import sys
import subprocess

# Python version 3.11.5
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66
# สามารถหาคำไทยได้แต่ต้องรันโค้ดผ่านโปรแกรมรันโค้ด เช่น Visual Studio Code

# How to use
# Just input Folder paths, the keyword you want to search, the replacement keyword, and the file extension.

# Natural sorting functions
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

# Check if tqdm is installed, and if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm
    
folder_paths = []

print("Please set all Foler name to english first")
print("Enter the folder paths you want to search in. Type 'done' when finished:")

def to_raw_string(s):
    return s.encode('unicode_escape').decode()

while True:
    path = input("Enter folder path (or 'done' to finish): ")
    if path.lower() == 'done':
        break
    folder_paths.append(to_raw_string(path))

while True:
    keyword = input("Enter the keyword to search for: ")
    replace_keyword = input(f"Enter the keyword to replace '{keyword}' with: ")
    file_extension = input("Enter the file extension you want to search (e.g., txt or .txt): ").strip()
    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension

    files_to_search = []
    matching_files = []

    for folder_path in folder_paths:
        if os.path.exists(folder_path):
            for filename in sorted(os.listdir(folder_path), key=natural_keys):  # Sorting filenames naturally
                if filename.endswith(file_extension):
                    file_path = os.path.join(folder_path, filename)
                    files_to_search.append(file_path)

    for file_path in tqdm(files_to_search, desc="Searching and Replacing", unit="file", position=0, leave=True):
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()
        if keyword in content:
            matching_files.append(file_path)
            new_content = content.replace(keyword, replace_keyword)
            with open(file_path, 'w', encoding='utf8') as f:
                f.write(new_content)

    # Sorting the matching files naturally
    matching_files = sorted(matching_files, key=lambda x: natural_keys(os.path.basename(x)))
    
    for match in matching_files:
        _, filename = os.path.split(match)
        print(f"The keyword '{keyword}' was found and replaced in the file: {filename}")

    if not matching_files:
        print(f"\nThe keyword '{keyword}' was not found in any {file_extension} file.")

    choice = input("Do you want to search and replace again? (yes/no): ").lower()
    if choice != 'yes':
        break
