def file_word_count(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}")

        print(f"Word count written to '{output_file}'")

    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")

input_file = 'input.txt'
output_file = 'output.txt'
file_word_count(input_file, output_file)
