def load(file_name, memory):
    try:
        with open(file_name, 'r') as file:
            memory = file.read()
            print(f"File '{file_name}' loaded into memory.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

    return memory
