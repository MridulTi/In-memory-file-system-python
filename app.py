import cmd
import os
import shutil

class MyCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Welcome to In-Memory File System. Type 'help' for available commands."

    
    def do_hello(self, line):
        print("HELLO, WORLD")
    
    def do_help(self, arg):
        help_text = """
        Available Commands:

        1. hello
        - Usage: hello
        - Description: Prints "HELLO, WORLD" as a greeting message.

        2. mkdir
        - Usage: mkdir <directory_name>
        - Description: Creates a new directory with the specified name.
        - Example: mkdir my_folder

        3. cd
        - Usage: cd <directory_path>
        - Description: Changes the current directory to the specified path.
            - Use '..' to move up one level in the directory tree.
            - Use '/' to move to the root directory.
        - Examples:
            - cd my_folder       (moves into 'my_folder')
            - cd ..              (moves up one directory level)
            - cd /               (moves to the root directory)

        4. ls
        - Usage: ls [directory_path]
        - Description: Lists the contents of the current directory. If a path is specified, lists the contents of that directory.
        - Example: ls /home/user

        5. cat
        - Usage: cat <file_name>
        - Description: Displays the contents of a specified file.
        - Example: cat example.txt

        6. touch
        - Usage: touch <file_name>
        - Description: Creates a new empty file with the specified name. Updates the file's last modified time if it already exists.
        - Example: touch newfile.txt

        7. echo
        - Usage: echo 'text' > <file_name>
        - Description: Writes the specified text to the specified file. Use single quotes for the text and > to specify the file.
        - Example: echo 'Hello, world!' > example.txt

        8. mv
        - Usage: mv <source> <destination>
        - Description: Moves a file or directory from the source path to the destination path.
        - Example: mv file.txt /new_folder/

        9. cp
        - Usage: cp <source> <destination>
        - Description: Copies a file or directory from the source path to the destination path.
        - Example: cp file.txt /new_folder/

        10. rm
            - Usage: rm <file_or_directory_name>
            - Description: Removes the specified file or directory. For directories, all contents are deleted.
            - Example: rm oldfile.txt
            - Caution: This action is irreversible.

        11. exit
            - Usage: exit
            - Description: Exits the CLI.

        """
        print(help_text)
    
    def do_mkdir(self, arg):
        #Create a new directory.
        try:
            if arg==None or arg=="":
                print("Mention the directory name")
                return
            if "," in arg:
                print("Don't include ',' in directory specification use space instead")
                return
            filenames=arg.split(" ")
            listedname=""
            for file in filenames:
                listedname+=file+","
                if file in os.listdir(path="."):
                    print("File Already Exists")
                    return
                os.makedirs(file, exist_ok=False)
            print(f"Directory {listedname[:-1]} created.")
        except FileNotFoundError:
            print(f"Error: File '{arg}' does not exist.")
        
        except PermissionError:
            print(f"Error: Permission denied to read '{arg}'.")
        except Exception as e:
            print(f"Error creating directory: {e}")
    
    def do_cd(self, arg):
        try:
            # If no argument is provided, change to the home directory
            if not arg.strip():
                home_path = os.path.expanduser("~")
                os.chdir(home_path)
                print(f"Changed directory to '{home_path}' (home)")
            
            # If argument is "..", go up one directory
            elif arg == "..":
                new_path = os.path.dirname(os.getcwd())
                os.chdir(new_path)
                print(f"Changed directory to '{new_path}'")
            
            # If argument is "/", go to the root directory
            elif arg == "/":
                os.chdir("/")
                print("Changed directory to '/' (root)")

            else:
                target_path = os.path.abspath(arg)
                
                # Check if the directory exists
                if not os.path.exists(target_path):
                    print(f"Error: Directory '{target_path}' does not exist.")
                elif not os.access(target_path, os.X_OK):
                    print("Error: Permission denied to access this directory.")
                else:
                    os.chdir(target_path)
                    print(f"Changed directory to '{os.getcwd()}'")

        except Exception as e:
            print(f"Error changing directory: {e}")

        
    
    def do_ls(self, arg):
        #List the contents of the current or specified directory.
        directory = arg.strip() or os.getcwd()
    
        try:
            if not os.path.isdir(directory):
                print(f"Error: '{directory}' is not a directory.")
                return

            items = os.listdir(directory)

            # Edge case: Handle empty directory
            if not items:
                print(f"The directory '{directory}' is empty.")
                return

            for item in items:
                print(item)

        except FileNotFoundError:
            print(f"Error: Directory '{directory}' does not exist.")
        
        except PermissionError:
            print(f"Error: Permission denied to access '{directory}'.")
        
        except Exception as e:
            print(f"Error listing directory: {e}")
    
    def do_cat(self, arg):
        #Display the contents of a file.
        if not arg.strip():
            print("Error: No file specified.")
            return
    
        try:
            # Check if the path is a file and exists
            if not os.path.isfile(arg):
                print(f"Error: '{arg}' does not exist or is not a file.")
                return
            
            # Handle large files by reading in chunks
            with open(arg, 'rb') as file:  # Open in binary mode to check for binary content
                # Attempt to read a small chunk to determine if file is binary
                first_chunk = file.read(1024)
                try:
                    # Check if the chunk contains non-text characters, indicating a binary file
                    first_chunk.decode('utf-8')
                except UnicodeDecodeError:
                    print("Error: File appears to be binary and may contain unreadable content.")
                    return
                
                # If the file is empty, notify the user
                if not first_chunk:
                    print(f"The file '{arg}' is empty.")
                    return

                # Display the file content in chunks to handle large files
                file.seek(0)  # Reset to the beginning of the file
                while chunk := file.read(4096):
                    print(chunk.decode('utf-8'), end="")

        except FileNotFoundError:
            print(f"Error: File '{arg}' does not exist.")
        
        except PermissionError:
            print(f"Error: Permission denied to read '{arg}'.")
        
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def do_touch(self, arg):
        #Create a new empty file.
        try:
            with open(arg, 'a'):
                os.utime(arg, None)
            print(f"File '{arg}' created.")
        except Exception as e:
            print(f"Error creating file: {e}")
    
    def do_echo(self, arg):
        #Write text to a file.
        if '>' in arg:
            text, filename = arg.split('>', 1)
            text = text.strip().strip("'\"")
            filename = filename.strip()
            try:
                with open(filename, 'w') as file:
                    file.write(text)
                print(f"Text written to '{filename}'.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("Invalid syntax. Use: echo 'text' > filename")
    
    def do_mv(self, arg):
        #Move a file or directory to another location.
        try:
            source, destination = arg.split()
            shutil.move(source, destination)
            print(f"Moved '{source}' to '{destination}'.")
        except Exception as e:
            print(f"Error moving file/directory: {e}")
    
    def do_cp(self, arg):
        #Copy a file or directory to another location.
        try:
            source, destination = arg.split()
            if os.path.isdir(source):
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)
            print(f"Copied '{source}' to '{destination}'.")
        except Exception as e:
            print(f"Error copying file/directory: {e}")
    
    def do_rm(self, arg):
        #Remove a file or directory.
        try:
            if os.path.isdir(arg):
                shutil.rmtree(arg)
            else:
                os.remove(arg)
            print(f"Removed '{arg}'.")
        except Exception as e:
            print(f"Error removing file/directory: {e}")
    
    def do_exit(self, arg):
        #Exit the CLI.
        return True

    def preloop(self):
        print(f"Starting in directory: {os.getcwd()}")
        print("="*50)

    def postloop(self):
        print("="*50)
        print("Exiting CLI... Goodbye!")

    def precmd(self, line):
        if line.strip().lower() == "exit":
            return line
        print(f"\nExecuting command: {line}")
        print("="*50)
        return line

    def postcmd(self, stop, line):
        if line.strip().lower() == "exit":
            return stop
        print("="*50)
        print("Command execution completed.")
        return stop

if __name__ == "__main__":
    MyCLI().cmdloop()