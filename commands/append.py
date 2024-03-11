def append(file_name, memory):
    try:
        with open(file_name, 'r') as file:
            memory += file.read()
            print(f"File '{file_name}' appended to memory.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

    return memory
