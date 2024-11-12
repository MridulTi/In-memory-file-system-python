import cmd
import os
from commands.cat import cat_command
from commands.cd import cd_command
from commands.cp import cp_command
from commands.echo import echo_command
from commands.ls import ls_command
from commands.mkdir import mkdir_command
from commands.mv import mv_command
from commands.rm import rm_command
from commands.touch import touch_command

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
    
    def do_cat(self,arg):
        result=cat_command(arg)
        print(result)
        return
    

    def do_cd(self,arg):
        result=cd_command(arg)
        print(result)
        return
    
    def do_cp(self,arg):
        result=cp_command(arg)
        print(result)
        return
    
    def do_echo(self,arg):
        result=echo_command(arg)
        print(result)
        return
    def do_ls(self,arg):
        result=ls_command(arg)
        print(result)
        return
    
    def do_mkdir(self,arg):
        result=mkdir_command(arg)
        print(result)
        return
    
    def do_mv(self,arg):
        result=mv_command(arg)
        print(result)
        return

    def do_rm(self,arg):
        result=rm_command(arg)
        print(result)
        return

    def do_touch(self,arg):
        result=touch_command(arg)
        print(result)
        return    
    
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
