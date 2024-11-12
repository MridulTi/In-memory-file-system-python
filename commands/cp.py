import os,shutil
def cp_command(arg):
        try:
            source, destination = arg.split()
            if not os.path.exists(source):
                return(f"Error: Source '{source}' does not exist.")
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)
            return(f"Copied '{source}' to '{destination}'.")
        except ValueError:
            return("Error: Invalid syntax. Usage: cp <source> <destination>")
        except FileNotFoundError:
            return(f"Error: Destination '{destination}' path does not exist.")
        except PermissionError:
            return(f"Error: Permission denied to copy '{source}' to '{destination}'.")
        except Exception as e:
            return(f"Error copying file/directory: {e}")
