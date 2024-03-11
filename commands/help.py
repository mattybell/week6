def help(commands, command_name=None):
    """Print this menu count of contents."""
    if command_name:
        command = commands.get(command_name)
        if command:
            print(f"Help for '{command_name}': {command.__doc__}")
        else:
            print(f"Error: Command '{command_name}' not found.")
    else:
        print("Available commands:")
        for name, func in commands.items():
            print(f"{name}: {func.__doc__}")

    return commands
