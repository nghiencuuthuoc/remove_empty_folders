import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def remove_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            full_path = os.path.join(root, dir)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                print(f"Đã xóa thư mục rỗng: {full_path}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_selected)

def start_cleaning():
    path = entry_path.get()
    if os.path.isdir(path):
        remove_empty_folders(path)
        messagebox.showinfo("Hoàn tất", "Đã xóa xong các thư mục rỗng.")
    else:
        messagebox.showerror("Lỗi", "Đường dẫn không hợp lệ.")

root = tk.Tk()
root.title("NCT - Xóa thư mục rỗng")
root.configure(bg="#ffffff")

frame = tk.Frame(root, padx=10, pady=10, bg="#ffffff")
frame.pack()

# Hiển thị logo trên đầu giao diện
try:
    logo_image = Image.open("nct_logo.png")
    logo_image = logo_image.resize((200, 200))
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(frame, image=logo, bg="#ffffff")
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
except Exception as e:
    print("Không thể tải logo:", e)

label = tk.Label(frame, text="Chọn thư mục gốc:", bg="#ffffff", font=("Arial", 11))
label.grid(row=1, column=0, sticky="w")

entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=2, column=0, pady=5)

browse_button = tk.Button(frame, text="Duyệt...", command=browse_folder)
browse_button.grid(row=2, column=1, padx=5)

start_button = tk.Button(frame, text="Xóa thư mục rỗng", command=start_cleaning)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()