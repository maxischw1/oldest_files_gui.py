import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

class OldestFilesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oldest Files Finder")
        self.root.geometry("600x400")

        self.start_path = 'C:\\Users'

        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label = tk.Label(self.root, text="Find the 10 files that haven't been used for the longest time", font=("Arial", 12))
        self.label.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient='horizontal', mode='determinate', length=400)
        self.progress.pack(pady=20)

        # Start Button
        self.start_button = tk.Button(self.root, text="Start Search", command=self.start_search)
        self.start_button.pack(pady=10)

        # Result display
        self.result_box = tk.Text(self.root, wrap='word', height=10)
        self.result_box.pack(pady=10, padx=20, fill='both', expand=True)

    def start_search(self):
        # Disable the Start button during the search
        self.start_button.config(state='disabled')
        self.progress['value'] = 0
        self.result_box.delete('1.0', tk.END)

        # Start the search in a separate thread to keep the GUI responsive
        threading.Thread(target=self.search_files).start()

    def search_files(self):
        file_access_times = []
        total_files = 0

        # Count total number of files for progress bar
        for dirpath, dirnames, filenames in os.walk(self.start_path):
            total_files += len(filenames)

        files_processed = 0

        for dirpath, dirnames, filenames in os.walk(self.start_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    atime = os.stat(filepath).st_atime  # Last access time
                    file_access_times.append((atime, filepath))
                except Exception:
                    continue

                files_processed += 1

                # Update the progress bar
                progress_percent = (files_processed / total_files) * 100
                self.progress['value'] = progress_percent
                self.root.update_idletasks()

        # Sort and display the results
        file_access_times.sort()
        oldest_files = file_access_times[:10]

        result_text = ""
        for atime, filepath in oldest_files:
            result_text += f"{time.ctime(atime)} - {filepath}\n"

        self.result_box.insert(tk.END, result_text)

        # Reset the progress bar and enable the Start button
        self.progress['value'] = 100
        self.start_button.config(state='normal')

        # Show a message
        messagebox.showinfo("Done", "The search is complete.")

def main():
    root = tk.Tk()
    app = OldestFilesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
