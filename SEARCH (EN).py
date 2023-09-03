import os
from tqdm import tqdm
# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66                        

# Set the folder paths you want to search in
folder_paths = [r'F:\Folder1\Raw text']

# Input the keyword to search for
keyword = input("Enter the keyword to search for: ")

# Initialize a variable to indicate whether the keyword is found
found = False

# Create a list to store all the files to be searched
files_to_search = []
matching_files = []  # To store the files where the keyword is found

# Iterate over each specified directory
for folder_path in folder_paths:
    # Iterate over each file in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            files_to_search.append(file_path)

# Iterate over each file in files_to_search with a progress bar
for file_path in tqdm(files_to_search, desc="Searching files", unit="file", position=0, leave=True):
    # Open and read the file
    with open(file_path, 'r', encoding='utf8') as f:
        content = f.read()

        # If the keyword is found in the file
        if keyword in content:
            matching_files.append(file_path)
            found = True

# Display results after the progress bar
for match in matching_files:
    _, filename = os.path.split(match)
    print(f"The keyword '{keyword}' was found in the file: {filename}")

# If the keyword wasn't found in any file
if not found:
    print(f"\nThe keyword '{keyword}' was not found in any file.")

input("Press any key to exit...")  # This line will make the program wait for user input before exiting.
