import os
import re
import sys
import subprocess

# Python version 3.11.5
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66


# How to use in moblie version
# Please run in Pydroid 3 - IDE for Python 3
# Then Just input Folder paths, the keyword you want to search, the replacement keyword, and the file extension
# If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)"]
# No need to edit the folder address in the code, you can run the program and use it right away.

# วิธีใช้บนมือถือ
# ให้รันบนPydroid 3 - IDE for Python 3
# ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]
# เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ คำที่ต้องการค้นหา คำที่อยากจะให้แก้ และนามสกุลของไฟล์นั้น ๆ 
# ไม่ต้องแก้ที่อยู่โฟลเดอร์ในโค้ดแล้วสามารถรันโปรแกรมแล้วใช้งานได้เลย

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

# ไม่ต้องแก้ที่อยู่โฟลเดอร์ในโค้ดแล้วสามารถรันโปรแกรมแล้วใช้งานได้เลย
# No need to edit the folder address in the code, you can run the program and use it right away.
folder_paths = []

print("Python version 3.11.5")
print("Code from ChatGPT")
print("Made By Bank's : Thai translator H Game")
print("Link Discord : https://discord.gg/q6FkGCHv66")
print("สามารถหาคำไทยได้แต่ต้องรันโค้ดผ่านโปรแกรมรันโค้ด เช่น Visual Studio Code")
print("")
print("How to use in moblie version")
print("Please run in Pydroid 3 - IDE for Python 3")
print("Then Just input Folder paths, the keyword you want to search, the replacement keyword, and the file extension.")
print("If you put flie in Pyroid3 Folder the path is [/storage/emulated/0/Documents/Pydroid3/(Put your folder name here)]")
print("No need to edit the folder address in the code, you can run the program and use it right away.")
print("")
print("วิธีใช้บนมือถือ")
print("ให้รันบนPydroid 3 - IDE for Python 3")
print("ถ้าเอาไฟล์ดิบที่ต้องการไว้ในโฟลเดอร์  Pyroid3 ตำแหน่งไฟล์คือ [/storage/emulated/0/Documents/Pydroid3/(ใส่ชื่อโฟลเดอร์ตรงนี้)]")
print("เพียงแค่ป้อนตำแหน่งของโฟลเดอร์ คำที่ต้องการค้นหา คำที่อยากจะให้แก้ และนามสกุลของไฟล์นั้น ๆ ")
print("ไม่ต้องแก้ที่อยู่โฟลเดอร์ในโค้ดแล้วสามารถรันโปรแกรมแล้วใช้งานได้เลย") 

print("")
print("Please set all Folder names to English first.")
print("Enter the folder paths you want to search in. Type 'done' when finished:")

def to_raw_string(s):
    return s.encode('unicode_escape').decode()

while True:
    path = input("Enter folder path (or 'done' to finish): ")
    # Check if user hasn't added any paths yet and tries to exit
    if path.lower() == 'done' and not folder_paths:
        print("You haven't added any folder paths yet. Please add at least one folder path.")
        continue
    elif path.lower() == 'done':
        break
    
    raw_path = to_raw_string(path)
    
    if not os.path.exists(raw_path):
        print("The provided path does not exist. Please enter a valid folder path.")
        continue
    
    # Check if path has already been added
    if raw_path in folder_paths:
        print("You have already added this folder path. Please add a different one.")
        continue
    
    folder_paths.append(raw_path)
    
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
    matching_files = sorted(tqdm(matching_files, desc="Sorting files", unit="file"), key=lambda x: natural_keys(os.path.basename(x)))
    
    if not matching_files:
        print(f"\nThe keyword '{keyword}' was not found in any {file_extension} file.")
    else:
        for match in matching_files:
            _, filename = os.path.split(match)
            print(f"The keyword '{keyword}' was replace with '{replace_keyword}' in the file: {filename}")
    
    choice = input("Do you want to search again? If you want to change the folder paths, type 'change'. (yes/no/change): ").lower()
    
    if choice == 'change':
        folder_paths = []
        print("Please set all Folder names to English first.")
        print("Enter the folder paths you want to search in. Type 'done' when finished:")
        
        while True:
            path = input("Enter folder path (or 'done' to finish): ")
            
            if path.lower() == 'done' and folder_paths:
                break
            elif path.lower() == 'done' and not folder_paths:
                print("You haven't entered any folder paths yet!")
                continue
            
            raw_path = to_raw_string(path)
            if not os.path.exists(raw_path):
                print("The provided path does not exist. Please enter a valid folder path.")
                continue
            if raw_path in folder_paths:
                print("You've already added this folder path. Please add a different one.")
                continue

            folder_paths.append(raw_path)

    elif choice != 'yes':
        sys.exit()
