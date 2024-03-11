from commands.load import load
from commands.save import save
from commands.append import append
from commands.clear import clear
from commands.help import help
from commands.character_count import character_count
from commands.word_count import word_count
from commands.line_count import line_count
from commands.count_substring import count_substring
# Import other commands as needed

memory = ""

def main():
    global memory
    commands = {
        'load': load,
        'save': save,
        'append': append,
        'clear': clear,
        'help': help,
        'cc': character_count,
        'wc': word_count,
        'lc': line_count,
        'count': count_substring
    }

    while True:
        user_input = input("Enter command: ")
        parts = user_input.split()
        if len(parts) == 0:
            continue

        command_name = parts[0]
        command_args = parts[1:]

        if command_name == 'load':
            memory = load(command_args[0], memory)
        elif command_name == 'save':
            save(command_args[0], memory)
        elif command_name == 'append':
            memory = append(command_args[0], memory)
        elif command_name == 'clear':
            memory = clear(memory)
        elif command_name == 'help':
            help(commands, *command_args)
        elif command_name == 'cc':
            character_count(memory)
        elif command_name == 'wc':
            word_count(memory)
        elif command_name == 'lc':
            line_count(memory)
        elif command_name == 'count':
            count_substring(command_args[0], memory)

        if command_name.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
