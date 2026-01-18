import os

def remove_empty_folders(path):
    # Duyệt theo thứ tự từ dưới lên (bottom-up)
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            full_path = os.path.join(root, dir)
            # Nếu thư mục rỗng thì xóa
            if not os.listdir(full_path):
                os.rmdir(full_path)
                print(f"Đã xóa thư mục rỗng: {full_path}")

if __name__ == "__main__":
    user_input = input("Nhập đường dẫn thư mục cần kiểm tra và xóa thư mục rỗng (ví dụ: D:\\du_lieu):\n")
    if os.path.isdir(user_input):
        remove_empty_folders(user_input)
        print("Hoàn tất!")
    else:
        print("Đường dẫn không hợp lệ. Vui lòng kiểm tra lại.")
