import os,cmd
def mkdir_command(arg):
        try:
            if not arg:
                return("Error: No directory name provided.")
            else:
                directories = arg.split()
                created_dirs = []
                for directory in directories:
                    if os.path.exists(directory):
                        return(f"Error: Directory '{directory}' already exists.")
                    else:
                        os.makedirs(directory, exist_ok=False)
                        created_dirs.append(directory)
                if created_dirs:
                    return(f"Directories created: {', '.join(created_dirs)}")
        except PermissionError:
            return("Error: Permission denied.")
        except Exception as e:
            return(f"Error creating directory: {e}")
