import os
import shutil
from tkinter import Tk, Button, Label, filedialog, messagebox, ttk, StringVar, PhotoImage
from tkinter.ttk import Progressbar, Style


# Function to organize files based on file types
def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        messagebox.showwarning("No Folder Selected", "Please select a folder!")
        return

    file_types = {
        'Audio': ('.mp3', '.wav', '.flac'),
        'Images': ('.jpg', '.jpeg', '.png', '.gif'),
        'Documents': ('.pdf', '.docx', '.txt', '.xlsx'),
        'Videos': ('.mp4', '.mov', '.avi'),
        'Archives': ('.zip', '.tar', '.gz', '.rar'),
    }

    file_list = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    if not file_list:
        messagebox.showinfo("No Files", "There are no files to organize in the selected folder.")
        return

    progress['maximum'] = len(file_list)
    progress['value'] = 0
    status_var.set("Organizing Files...")

    for index, file_name in enumerate(file_list):
        file_path = os.path.join(folder_path, file_name)
        file_extension = os.path.splitext(file_name)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                folder_dest = os.path.join(folder_path, folder)
                if not os.path.exists(folder_dest):
                    os.makedirs(folder_dest)
                shutil.move(file_path, folder_dest)
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, other_folder)

        progress['value'] += 1
        root.update_idletasks()

    status_var.set("Organization Complete!")
    messagebox.showinfo("Success", "Files have been organized successfully!")


# GUI Setup
def create_gui():
    global progress, status_var, root

    root = Tk()
    root.title("Automated File Organizer")
    root.geometry("600x400")

    # Background image
    # bg_image = PhotoImage(file="background.png")  # Add your image file here
    # background_label = Label(root, image=bg_image)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title Label with Font Customization
    title_label = Label(root, text="File Organizer", font=('Calibri', 24, 'bold'), fg="#ffffff", bg="#34495e")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Instruction Label
    instruction_label = Label(root, text="Select a folder and organize files:", font=('Calibri', 14), bg="#34495e",
                              fg="#ffffff")
    instruction_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    # Custom Style for Buttons
    style = Style()
    style.configure('TButton', font=('Calibri', 14), padding=10)
    style.map('TButton', foreground=[('pressed', 'white'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'lightblue')])

    # Organize Button with Hover Effects
    organize_button = Button(root, text="Select Folder and Organize", command=organize_files, font=('Calibri', 14),
                             bg="#2ecc71", fg="white")
    organize_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Progress Bar
    progress = Progressbar(root, orient="horizontal", length=500, mode="determinate", style="TProgressbar")
    progress.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    # Status Label
    status_var = StringVar()
    status_var.set("Waiting for file organization...")
    status_label = Label(root, textvariable=status_var, font=('Calibri', 12, 'italic'), fg="white", bg="#34495e")
    status_label.grid(row=4, column=0, columnspan=2)

    # Quit Button with Styling
    quit_button = Button(root, text="Quit", command=root.quit, font=('Calibri', 14), bg="#e74c3c", fg="white")
    quit_button.grid(row=5, column=0, columnspan=2, pady=20)

    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    create_gui()
