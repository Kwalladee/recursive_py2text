import os

def scan_and_dump(folder_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as input_file:
                            content = input_file.read()
                            output_file.write(f"===== Start of {file_path} =====\n")
                            output_file.write(content)
                            output_file.write(f"\n===== End of {file_path} =====\n\n")
                    except UnicodeDecodeError as e:
                        print(f"Skipping {file_path} due to Unicode decoding error: {e}")

