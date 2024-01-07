import os
import re
import sys
import subprocess

# Natural sorting functions
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

# Convert folder path to raw string
def to_raw_string(s):
    return s.encode('unicode_escape').decode()

# Check if tqdm is installed, and if not, install it
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found! Installing tqdm...")
    subprocess.run([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm
    
folder_paths = []

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

output_file_path = input("Enter the path for the output file (e.g., output.txt): ")
output_file_path = to_raw_string(output_file_path)

while True:  # This outer loop allows for multiple keyword searches
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
            content = f.readlines()
            for line_number, line in enumerate(content, start=1):
                if keyword in line:
                    matching_files.append((file_path, line_number, line.strip()))
                    found = True

    # Sorting the matching files naturally
    matching_files = sorted(tqdm(matching_files, desc="Sorting files", unit="file"), key=lambda x: natural_keys(os.path.basename(x[0])))

    with open(output_file_path, 'a', encoding='utf8') as output_file:
        for match in matching_files:
            file_path, line_number, line_content = match
            _, filename = os.path.split(file_path)
            result_line = f"Keyword '{keyword}' found in line {line_number} in file {filename}: {line_content}\n"
            print(result_line)
            output_file.write(result_line)

    if not found:
        print(f"\nThe keyword '{keyword}' was not found in any .{file_extension} file.")
    else:
        open_choice = input("Do you want to open any of the matched files? (yes/no): ").lower()

        if open_choice == 'yes':
            while True:
                filename_to_open = input("Enter the name of the file you want to open, 'all' to open all, or 'done' to finish: ")
        
                if filename_to_open.lower() == 'done':
                    break

                if filename_to_open.lower() == 'all':
                    for match in matching_files:
                        os.system(f'start "" "{match[0]}"')  # Notice the extra quotes
                    break
                
                for match in matching_files:
                    if filename_to_open in os.path.basename(match[0]):
                        os.system(f'start "" "{match[0]}"')  # Notice the extra quotes

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
