import os
def cat_command(arg):
        if not arg.strip():
            return ("Error: No file specified.")
        try:
            if not os.path.isfile(arg):
                return(f"Error: '{arg}' does not exist or is not a file.")
            else:
                with open(arg, 'rb') as file:
                    chunk = file.read(1024)
                    if not chunk:
                        return(f"The file '{arg}' is empty.")
                    try:
                        print(chunk.decode('utf-8'), end="")
                        while chunk := file.read(4096):
                            print(chunk.decode('utf-8'), end="")
                    except UnicodeDecodeError:
                        return("Error: File appears to be binary.")
        except FileNotFoundError:
            return(f"Error: File '{arg}' does not exist.")
        except PermissionError:
            return("Error: Permission denied.")
        except Exception as e:
            return(f"Error reading file: {e}")
