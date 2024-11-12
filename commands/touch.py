import os
def touch_command(arg):
        if not arg:
            return("Error: No filename specified.")
        try:
            with open(arg, 'a'):
                os.utime(arg, None)
            return(f"File '{arg}' created.")
        except PermissionError:
            return("Error: Permission denied.")
        except Exception as e:
            return(f"Error creating file: {e}")