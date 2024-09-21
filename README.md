# Script Launcher

A versatile and user-friendly CLI tool for managing and launching your scripts and applications with custom arguments.

## Features

- 🚀 Launch multiple scripts or applications with a single command
- 🎨 Colorful and intuitive CLI interface
- ✏️ Quick edit functionality for scripts
- 🔧 Support for custom arguments for each script/app
- 🖥️ Opens each script in a new terminal window

## Requirements

- Python 3.6+
- Rich library (`pip install rich`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/script-launcher.git
   cd script-launcher
   ```

2. Install the required Python library:
   ```
   pip install rich
   ```

3. Configure your scripts in `script_config.py`.

## Configuration

Edit the `script_config.py` file to add your scripts and applications. Here's an example configuration:

```python
SCRIPTS = [
    {
        "name": "My Python Script",
        "path": "~/projects/myscript.py",
        "working_dir": "~/projects",
        "is_python": True,
        "args": "-v --output result.txt"
    },
    {
        "name": "Custom App",
        "path": "~/apps/myapp",
        "working_dir": "~/apps",
        "is_python": False,
        "args": "-t 0 -d 1 -gpu"
    },
]
```

## Usage

Run the script launcher:

```
python3 script_launcher.py
```

- Enter the numbers of the scripts you want to launch, separated by spaces.
- Append * to a number to open the script for editing instead of launching.
- Enter 'q' to quit the application.

Example:
```
1 2 3*
```
This will launch scripts 1 and 2, and open script 3 for editing.

## Creating a Desktop Shortcut

To create a desktop shortcut:

1. Create a `.desktop` file named `script-launcher.desktop` with the following content:

   ```
   [Desktop Entry]
   Version=1.0
   Type=Application
   Name=Script Launcher
   Comment=Launch custom scripts
   Exec=/usr/bin/python3 /path/to/your/script_launcher.py
   Icon=/path/to/your/icon.png
   Terminal=true
   Categories=Utility;Development;
   ```

2. Replace `/path/to/your/script_launcher.py` with the actual path to your script.
3. Choose an icon and replace `/path/to/your/icon.png` with its path.
4. Make the file executable: `chmod +x script-launcher.desktop`
5. Move the file to your desktop: `mv script-launcher.desktop ~/Desktop/`

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/script-launcher/issues).

## License

[GNU v3.0](https://choosealicense.com/licenses/gpl-3.0/)
