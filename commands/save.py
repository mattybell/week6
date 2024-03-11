def save(file_name, memory):
    try:
        with open(file_name, 'w') as file:
            file.write(memory)
            print(f"Contents saved to file '{file_name}'.")
    except Exception as e:
        print(f"Error saving file: {e}")
