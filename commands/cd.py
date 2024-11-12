import os
def cd_command(arg):
        try:
            if not arg.strip():
                home_path = os.path.expanduser("~")
                os.chdir(home_path)
                return(f"Changed directory to '{home_path}'")
            elif arg == ".." or arg.startswith("../"):
                os.chdir(os.path.abspath(os.path.join(os.getcwd(), arg)))
                return(f"Changed directory to '{os.getcwd()}'")
            elif arg == "/":
                os.chdir("/")
                return("Changed directory to root '/'")
            else:
                target_path = os.path.abspath(arg)
                if os.path.islink(target_path) and os.path.realpath(target_path) == os.getcwd():
                    return("Error: Circular symbolic link detected.")
                elif not os.path.exists(target_path):
                    return(f"Error: Directory '{target_path}' does not exist.")
                elif not os.access(target_path, os.X_OK):
                    return("Error: Permission denied.")
                else:
                    os.chdir(target_path)
                    return(f"Changed directory to '{os.getcwd()}'")
        except Exception as e:
            return(f"Error changing directory: {e}")
