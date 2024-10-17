def sort_text_file(input_file, output_file):
    # Read the contents of the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Sort the lines based on the first character of each line
    sorted_lines = sorted(lines, key=lambda x: x[0])

    # Write the sorted lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)

if __name__ == "__main__":
    # Replace 'input.txt' and 'output.txt' with your file names
    input_file_name = input("Kérem a fájl nevét a kiterjesztés nélkül --> ") + '.txt'
    output_file_name = 'sorted-'+input_file_name

    sort_text_file(input_file_name, output_file_name)

    print(f"Sorting complete. Check '{output_file_name}' for the sorted data.")
