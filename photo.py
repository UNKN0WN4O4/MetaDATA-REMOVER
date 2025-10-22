import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def clear_all_metadata(image_path, output_path=None):
    with Image.open(image_path) as img:
        data = list(img.getdata())
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)
        output = output_path or image_path
        clean_img.save(output,optimize=True,progressive=True)

def browse_files_bulk():
    filetypes = [
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
        ("All files", "*.*")
    ]
    file_paths = filedialog.askopenfilenames(
        title="Select Images to Clean",
        filetypes=filetypes
    )
    if file_paths:
        cleaned = 0
        for path in file_paths:
            filename = os.path.basename(path)
            directory = os.path.dirname(path)
            save_path = os.path.join(directory, f"cleaned_{filename}")
            clear_all_metadata(path, save_path)
            cleaned += 1
        messagebox.showinfo("Done", f"Successfully cleaned metadata from {cleaned} images!")

def main():
    root = tk.Tk()
    root.title("Bulk Image Metadata Cleaner")
    root.geometry("400x180")
    root.resizable(False, False)

    label = tk.Label(root, text="Select one or more images to remove metadata:")
    label.pack(pady=15)

    browse_btn = tk.Button(root, text="Browse Multiple Images", command=browse_files_bulk, width=25, height=2)
    browse_btn.pack()

    exit_btn = tk.Button(root, text="Exit", command=root.quit, width=25, height=2)
    exit_btn.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()

