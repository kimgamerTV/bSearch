import os
import re
import subprocess  # Import subprocess library

try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing now...")
    subprocess.check_call(["pip", "install", "tqdm"])
    from tqdm import tqdm

# This function is used for natural sorting
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66

# Set the folder paths you want to search in
folder_paths = [r'F:\SUMMER ALL TRANSLATE\All monob plus level']

while True:
    keyword = input("Enter the keyword to search for: ")

    found = False
    files_to_search = []
    matching_files = []

    for folder_path in folder_paths:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                files_to_search.append(file_path)

    for file_path in tqdm(files_to_search, desc="Searching files", unit="file", position=0, leave=True):
        with open(file_path, 'r', encoding='utf8') as f:
            content = f.read()
            if keyword in content:
                matching_files.append(file_path)
                found = True

    # Display results after the progress bar
    # Sort the matching_files list using natural sorting
    for _ in tqdm(matching_files, desc="Sorting files", unit="file", position=1, leave=True):  # progress bar for sorting
        matching_files.sort(key=lambda x: natural_keys(os.path.basename(x)))

    # Then, display the sorted files
    for match in matching_files:
        _, filename = os.path.split(match)
        print(f"The keyword '{keyword}' was found in the file: {filename}")

    if not found:
        print(f"\nThe keyword '{keyword}' was not found in any file.")

    choice = input("Do you want to search again? (yes/no): ").lower()
    if choice != 'yes':
        break
