import os
def echo_command(arg):
        if '>' in arg:
            text, filename = arg.split('>', 1)
            text = text.strip().strip("'\"")
            filename = filename.strip()
            try:
                if not filename:
                    return("Error: No filename specified.")
                with open(filename, 'w') as file:
                    file.write(text)
                return(f"Text written to '{filename}'.")
            except FileNotFoundError:
                return(f"Error: File '{filename}' path does not exist.")
            except PermissionError:
                return(f"Error: Permission denied to write to '{filename}'.")
            except Exception as e:
                return(f"Error writing to file: {e}")
        else:
            return("Invalid syntax. Use: echo 'text' > filename")
