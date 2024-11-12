import os
def ls_command(arg):
        directory = arg.strip() or os.getcwd()
        try:
            if not os.path.isdir(directory):
                return(f"Error: '{directory}' is not a directory.")
            else:
                items = os.listdir(directory) or ["(empty directory)"]
                for item in items:
                    return(item)
        except FileNotFoundError:
            return(f"Error: Directory '{directory}' does not exist.")
        except PermissionError:
            return(f"Error: Permission denied.")
        except Exception as e:
            return(f"Error listing directory: {e}")
