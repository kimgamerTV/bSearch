import os
from tqdm import tqdm

# Code from ChatGPT
# Made By Bank's : Thai translator H Game
# Link Discord : https://discord.gg/q6FkGCHv66

# Set the folder paths you want to search in
# F:\Folder\Raw text
folder_paths = [r'F:\Folder\Raw text']

while True:  # This loop will allow the user to keep searching
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
    # Use tqdm to wrap the matching_files list during sorting
    sorted_files = sorted(tqdm(matching_files, desc="Sorting files", position=1, leave=True), key=lambda x: os.path.basename(x))
    for match in sorted_files:
        _, filename = os.path.split(match)
        print(f"The keyword '{keyword}' was found in the file: {filename}")

    # If the keyword wasn't found in any file
    if not found:
        print(f"\nThe keyword '{keyword}' was not found in any file.")

    # Ask the user if they want to search again
    choice = input("Do you want to search again? (yes/no): ").lower()
    if choice != 'yes':
        break  # Exit the loop and end the program
