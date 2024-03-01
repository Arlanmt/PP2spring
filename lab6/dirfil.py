import os

def list_directories_and_files(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"Directory: {entry.name}")
                elif entry.is_file():
                    print(f"File: {entry.name}")
    except FileNotFoundError:
        print("Specified path not found.")

# Example usage:
list_directories_and_files("/path/to/your/directory")






import os

def check_path_access(path):
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readability: {os.access(path, os.R_OK)}")
    print(f"Writability: {os.access(path, os.W_OK)}")
    print(f"Executability: {os.access(path, os.X_OK)}")

# Example usage:
check_path_access("/path/to/your/file_or_directory")




import os

def check_path_and_extract_components(path):
    if os.path.exists(path):
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("Path does not exist.")

# Example usage:
check_path_and_extract_components("/path/to/your/file")




def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"Number of lines: {line_count}")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
count_lines_in_file("/path/to/your/text_file.txt")






def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

# Example usage:
data_list = ["item1", "item2", "item3"]
write_list_to_file("/path/to/your/output_file.txt", data_list)






import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"Content for file {letter}.txt")

# Example usage:
generate_text_files()






def copy_file_contents(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
    except FileNotFoundError:
        print("Source file not found.")

# Example usage:
copy_file_contents("/path/to/source_file.txt", "/path/to/destination_file.txt")





import os

def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"File deleted: {path}")
        except PermissionError:
            print(f"Permission error. Unable to delete file: {path}")
    else:
        print("File does not exist.")

# Example usage:
delete_file("/path/to/your/file_to_delete.txt")
