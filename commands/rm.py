import os,shutil
def rm_command(arg):
        try:
            if not arg.strip():
                return("Error: No file or directory specified.")
                return
            if os.path.isdir(arg):
                shutil.rmtree(arg)
            else:
                os.remove(arg)
            return(f"Removed '{arg}'.")
        except FileNotFoundError:
            return(f"Error: '{arg}' does not exist.")
        except PermissionError:
            return(f"Error: Permission denied to remove '{arg}'.")
        except IsADirectoryError:
            return(f"Error: '{arg}' is a directory. Use rm -r <directory> to remove directories.")
        except Exception as e:
            return(f"Error removing file/directory: {e}")
    