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
# Just input Folder paths, the keyword you want to search, the replacement keyword, and the file extension
# No need to edit the folder address in the code, you can run the program and use it right away.

# วิธีใช้
# เพียงป้อนตำแหน่งของโฟลเดอร์ คำที่ต้องการค้นหา คำที่อยากจะให้แก้ และนามสกุลของไฟล์นั้น ๆ 
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

# Convert folder path to raw string
def to_raw_string(s):
    return s.encode('unicode_escape').decode()
    
# No need to edit the folder address in the code, you can run the program and use it right away.
# ไม่ต้องแก้ที่อยู่โฟลเดอร์ในโค้ดแล้วสามารถรันโปรแกรมแล้วใช้งานได้เลย
folder_paths = []

print("Python version 3.11.5")
print("Code from ChatGPT")
print("Made By Bank's : Thai translator H Game")
print("Link Discord : https://discord.gg/q6FkGCHv66")
print("สามารถหาคำไทยได้แต่ต้องรันโค้ดผ่านโปรแกรมรันโค้ด เช่น Visual Studio Code")
print("")
print("How to use")
print("Just input Folder paths, the keyword you want to search, the replacement keyword, and the file extension.")
print("No need to edit the folder address in the code, you can run the program and use it right away.")
print("")
print("วิธีใช้")
print("เพียงป้อนตำแหน่งของโฟลเดอร์ คำที่ต้องการค้นหา คำที่อยากจะให้แก้ และนามสกุลของไฟล์นั้น ๆ ")
print("ไม่ต้องแก้ที่อยู่โฟลเดอร์ในโค้ดแล้วสามารถรันโปรแกรมแล้วใช้งานได้เลย")
    
print("")
print("Please set all Folder names to English first.")
print("Enter the folder paths you want to search in. Type 'done' when finished:")
    
while True:
    path = to_raw_string(input("Enter folder path (or 'done' to finish): "))
    
    if path.lower() == 'done':
        if not folder_paths:
            print("You haven't entered any folder paths yet!")
            continue
        else:
            break

    if path in folder_paths:
        print("You've already added this folder path. Please add a different one.")
        continue  # continue to next loop iteration

    folder_paths.append(path)


while True: # This outer loop allows for multiple keyword searches
    keyword = input("Enter the keyword to search for: ")
    file_extension = input("Enter the file extension you want to search (e.g., txt or .txt): ").strip()
    if file_extension.startswith('.'):
        file_extension = file_extension[1:]

    found = False
    files_to_search = []
    matching_files = []

    for folder_path in folder_paths:
        if os.path.exists(folder_path):
            for filename in sorted(os.listdir(folder_path), key=natural_keys):
                if filename.endswith('.' + file_extension):
                    file_path = os.path.join(folder_path, filename)
                    files_to_search.append(file_path)

    for file_path in tqdm(files_to_search, desc="Searching files", unit="file", position=0, leave=True):
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()
            if keyword in content:
                matching_files.append(file_path)
                found = True
                
    # Sorting the matching files naturally
    matching_files = sorted(tqdm(matching_files, desc="Sorting files", unit="file"), key=lambda x: natural_keys(os.path.basename(x)))

    for match in matching_files:
        _, filename = os.path.split(match)
        print(f"The keyword '{keyword}' was found in the file: {filename}")

    if not found:
        print(f"\nThe keyword '{keyword}' was not found in any .{file_extension} file.")

    choice = input("Do you want to search again? If you want to change the folder paths, type 'change'. (yes/no/change): ").lower()

    if choice == 'change':
        folder_paths = []
        print("Please set all Folder names to English first.")
        print("Enter the folder paths you want to search in. Type 'done' when finished:")
        
        while True:
            path = to_raw_string(input("Enter folder path (or 'done' to finish): "))

            if path.lower() == 'done' and folder_paths:
                break
            elif path.lower() == 'done' and not folder_paths:
                print("You haven't entered any folder paths yet!")
                continue
            if path in folder_paths:
                print("You've already added this folder path. Please add a different one.")
                continue  # continue to next loop iteration
            folder_paths.append(path)

    elif choice != 'yes':
        break
