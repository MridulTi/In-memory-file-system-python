import os,shutil
def mv_command(arg):
        try:
            source, destination = arg.split()
            if not os.path.exists(source):
                return(f"Error: Source '{source}' does not exist.")
            if os.path.isdir(destination) and os.path.samefile(source, destination):
                return("Error: Source and destination are the same.")
            shutil.move(source, destination)
            return(f"Moved '{source}' to '{destination}'.")
        except ValueError:
            return("Error: Invalid syntax. Usage: mv <source> <destination>")
        except FileNotFoundError:
            return(f"Error: Destination '{destination}' path does not exist.")
        except PermissionError:
            return(f"Error: Permission denied to move '{source}' to '{destination}'.")
        except Exception as e:
            return(f"Error moving file/directory: {e}")
