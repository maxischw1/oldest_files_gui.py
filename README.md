# Oldest Files Finder

A Python GUI application that finds the 10 files on your computer that haven't been used for the longest time.

## Features

- **Graphical User Interface:** Easy-to-use GUI built with Tkinter.
- **Progress Bar:** Visual indication of search progress.
- **Customizable Search Directory:** Easily change the directory to search.
- **Multithreading:** The search runs in a separate thread to keep the GUI responsive.

## Requirements

- **Python 3.x**  
  Download and install Python from [python.org](https://www.python.org/downloads/) if you don't have it installed.

- **Tkinter Library**  
  Tkinter usually comes pre-installed with Python on most systems.

  For Ubuntu/Debian-based systems:
  ```bash
  sudo apt-get install python3-tk
  For Fedora:

```bash
sudo dnf install python3-tkinter
```

For Windows and macOS, Tkinter is included with the standard Python installer.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/oldest-files-finder.git
```

### Navigate to the Directory

```bash
cd oldest-files-finder
```

## Usage

### Run the Script

On Windows:

```bash
python oldest_files_gui.py
```

On macOS/Linux:

```bash
python3 oldest_files_gui.py
```

## Using the Application

- Click the "Start Search" button to begin searching.
- The progress bar will indicate the progress of the search.
- Once complete, the 10 oldest files will be displayed in the text area.

## Customization

### Changing the Search Directory

By default, the script searches your home directory. To change the directory:

1. Open `oldest_files_gui.py` in a text editor.
2. Locate the line:
   ```python
   self.start_path = os.path.expanduser('~')
   ```
3. Replace it with the desired path. For example:
   ```python
   self.start_path = r'C:\Users'
   ```

### Excluding Specific Directories

Modify the `search_files` method to exclude directories if needed.

## Notes

### Permissions

Ensure you have the necessary permissions to access the files in the directories you're searching. Running the script as an administrator may be necessary for certain directories.

### Performance

Searching large directories can take a significant amount of time. Be patient as the progress bar updates.
