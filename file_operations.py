import os

print("To skip an operation use -")
operation = input("What do you want to do with file(s)? (w --> create, r --> read, d --> delete) ").lower()

def file_creation():
    def multiple_file_creation():
        file_count = int(input("How many files: "))
        for i in range(1, file_count+1):
            full_file_name = f"{file_name}{i}.{file_extension}"
            with open(full_file_name, "w") as new_file:
                new_file.write(file_content)
            print(f"{full_file_name} created successfully!")

    def single_file_creation():
        try:
            full_file_name = f"{file_name}.{file_extension}"
            with open(full_file_name, "w") as new_file:
                new_file.write(file_content)
            print(f"{full_file_name} created successfully!")
        except FileNotFoundError:
            print("The specified file or directory does not exist.")
        except PermissionError:
            print("Permission denied. You don't have the necessary permissions.")
        except IsADirectoryError:
            print("Cannot create a file in an existing directory with the same name.")
        except FileExistsError:
            print("File with the same name already exists.")

    file_name = input("File's name (don't include extension): ")
    file_location = input("File's location: ")
    file_extension = input("File's extension (don't include '.'): ")
    multiple_files = input("Multiple files with same name? (y/n) ").lower()
    file_content = input("File's content: ")

    if multiple_files == "y":
        multiple_file_creation()

    if multiple_files == "n":
        single_file_creation()

def file_removal():
    def single_file_removal():
        try:
            os.remove(full_file_name)
            print(f"{full_file_name} successfully removed!")
        except FileNotFoundError:
            print("\033[91m!!!File not found!!!\033[0m")
    
    def multiple_file_removal():
        starts_with = input("Remove files which start with: ")
        if starts_with == "-":
            ends_with = input("Remove files which end with: ")
            if ends_with == "-":
                print("Operation ended.\nProgram exits")
                exit()
            else:
                for file in os.listdir(file_location):
                    if file.endswith(ends_with):
                        file_path = os.path.join(file_location, file)
                        os.remove(file_path)
                        print(f"Deleted file: {file}")
        else:
            for file in os.listdir(file_location):
                if file.startswith(starts_with):
                    file_path = os.path.join(file_location, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file}")

    multiple_file_remove = input("Do you want to remove multiple files? (y/n) ").lower()
    file_name = input("File's name (don't include extension): ")
    file_location = input("File's location: ")
    file_extension = input("File's extension (don't include '.'): ")
    full_file_name = f"{file_location}{file_name}.{file_extension}"

    if multiple_file_remove == "n":
        single_file_removal()

    if multiple_file_remove == "y":
        multiple_file_removal()

def file_reading():
    file_name = input("File's name (don't include extension): ")
    file_location = input("File's location: ")
    file_extension = input("File's extension (don't include '.'): ")
    file_encoding = input("File's encoding: (default is utf-8)")

    if file_encoding == "-":
        file_encoding = "utf-8"

    full_file_name = f"{file_name}.{file_extension}"
    with open(f"{file_location}{full_file_name}", "r", encoding=file_encoding) as opened_file:
        file_content = opened_file.read()
        print(f"{full_file_name} read in successfully!")
        print(f"{full_file_name}'s content:\n{file_content}")

if operation == "w":
    file_creation()
elif operation == "d":
    file_removal()
elif operation == "r":
    file_reading()
elif operation == "-":
    print("Program exits")
    exit()