import os
import subprocess
from typing import List, Dict
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Import the configuration
from script_config import SCRIPTS

console = Console()

def display_scripts(scripts: List[Dict[str, str]]) -> None:
    text = Text()
    for index, script in enumerate(scripts, start=1):
        if index > 1:
            text.append("   ")  # Add spacing between items
        color = "bright_green" if script['is_python'] else "bright_yellow"
        text.append(f"{index}. ", style="bold bright_white")
        text.append(f"{script['name']}", style=f"bold {color}")
    
    console.print(Panel(text, expand=False, border_style="bright_blue"))

def launch_script(script: Dict[str, str]) -> None:
    script_path = os.path.expanduser(script['path'])
    working_dir = os.path.expanduser(script['working_dir'])
    
    if not os.path.exists(script_path):
        console.print(f"Error: Script/app not found at {script_path}", style="bold bright_red")
        return

    if not os.path.exists(working_dir):
        console.print(f"Error: Working directory not found at {working_dir}", style="bold bright_red")
        return

    if script['is_python']:
        run_command = f"python3 '{script_path}' {script['args']}"
    else:
        run_command = f"'{script_path}' {script['args']}"
    
    shell_script = f"""#!/bin/bash
cd '{working_dir}'
trap 'echo -e "\\n\\nScript or app interrupted. Exiting to command line..."; exec bash' INT
{run_command}
echo -e "\\n\\nScript or app finished. Exiting to command line..."
exec bash
"""
    
    tmp_script_path = f"/tmp/run_script_{script['name']}.sh"
    with open(tmp_script_path, 'w') as f:
        f.write(shell_script)
    os.chmod(tmp_script_path, 0o755)
    
    if os.system('which gnome-terminal') == 0:
        subprocess.Popen(['gnome-terminal', '--geometry=100x30', '--', 'bash', tmp_script_path])
    elif os.system('which xterm') == 0:
        subprocess.Popen(['xterm', '-geometry', '100x30', '-e', f"bash {tmp_script_path}"])
    else:
        console.print("No supported terminal found. Please install gnome-terminal or xterm.", style="bold bright_red")
    
    console.print(f"Launched: {script['name']}", style="bold bright_green")

def edit_script(script: Dict[str, str]) -> None:
    script_path = os.path.expanduser(script['path'])
    
    if not os.path.exists(script_path):
        console.print(f"Error: Script/app not found at {script_path}", style="bold bright_red")
        return

    editor_command = 'code'
    
    try:
        subprocess.Popen([editor_command, script_path])
        console.print(f"Opened for editing: {script['name']}", style="bold bright_blue")
    except FileNotFoundError:
        console.print(f"Error: Editor '{editor_command}' not found. Please install it or change the editor command.", style="bold bright_red")

def main():
    while True:
        console.clear()
        console.print("[bold bright_cyan]Script Launcher[/bold bright_cyan]", justify="center")
        console.print()
        display_scripts(SCRIPTS)
        console.print("\nAppend * to a number to open the script for editing instead of launching", style="italic bright_white")
        console.print()
        choice = Prompt.ask("Enter the numbers of the scripts to launch/edit (space-separated) or 'q' to quit")
        
        if choice.lower() == 'q':
            break

        try:
            choices = choice.split()
            for c in choices:
                if c.endswith('*'):
                    script_num = int(c[:-1])
                    if 1 <= script_num <= len(SCRIPTS):
                        edit_script(SCRIPTS[script_num-1])
                    else:
                        console.print(f"Invalid choice: {c}. Skipping.", style="bold bright_red")
                else:
                    script_num = int(c)
                    if 1 <= script_num <= len(SCRIPTS):
                        launch_script(SCRIPTS[script_num-1])
                    else:
                        console.print(f"Invalid choice: {c}. Skipping.", style="bold bright_red")
        except ValueError:
            console.print("Invalid input. Please enter numbers (optionally followed by *) separated by spaces.", style="bold bright_red")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()