import os

# creation of files
""" for i in range(1, 11):
    with open(f"./{i} file.txt", "w") as new_file:
        new_file.write("Content")
    print("File created successfully") """

# remove files whiches number can be divided by 2
""" for i in range(1, 11):
    if i % 2 == 0:
        os.remove(f"./{i} file.txt")
        print(f"Successfully deleted file") """

# delete files with a condition    
""" directory_path = './'
unnecesarry_countries = ["Hungary", "Germany"]

for file in os.listdir(directory_path):
    if file.endswith('.txt'):
        for country in unnecesarry_countries:
            if file.startswith(country):
                file_path = os.path.join(directory_path, file)
                os.remove(file_path)
                print(f"Deleted file: {file}") """

unnecesarry_file_types = ['.fpa', '.fjw', '.fsp']

for file in os.listdir('./'):
    for file_type in unnecesarry_file_types:
        if file.endswith(file_type):
            os.remove(f"./{file}")
            print(f"Removed {file}")