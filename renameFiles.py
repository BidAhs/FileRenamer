import os

def rename_files(folder_path):
    files = os.listdir(folder_path)

    for file_name in files:
        old_path = os.path.join(folder_path, file_name)

        new_file_name = file_name[18:] #removes the first 18 characters feel free to change the 18 to be less or more :)

        new_path = os.path.join(folder_path, new_file_name)

        os.rename(old_path, new_path)

# Usage
folder_path = r'/path/to/your/folder'
rename_files(folder_path)
