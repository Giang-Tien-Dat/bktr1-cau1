import tkinter as tk
from tkinter import messagebox

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính đơn giản")
window.geometry("400x500")

# Hàm kiểm tra số tự nhiên hợp lệ
def is_valid_number(num_str):
    try:
        num = int(num_str)
        return num >= 0  # Kiểm tra số tự nhiên (>= 0)
    except ValueError:
        return False

# Hàm thực hiện phép tính
def calculate(operation):
    # Lấy giá trị từ ô nhập liệu
    num1_str = entry_num1.get()
    num2_str = entry_num2.get()
    
    # Kiểm tra đầu vào hợp lệ
    if not is_valid_number(num1_str) or not is_valid_number(num2_str):
        messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên hợp lệ!")
        return
    
    # Chuyển đổi sang số
    num1 = int(num1_str)
    num2 = int(num2_str)
    
    # Thực hiện phép tính
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:  # operation == "/"
            if num2 == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            result = num1 / num2
        
        # Hiển thị kết quả
        result_label.config(text=f"Kết quả: {result}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo và đặt vị trí các thành phần giao diện
# Hướng dẫn sử dụng
guide_label = tk.Label(window, text="Nhập hai số tự nhiên và chọn phép tính", font=("Arial", 12))
guide_label.pack(pady=20)

# Khung nhập số thứ nhất
frame_num1 = tk.Frame(window)
frame_num1.pack(pady=10)
tk.Label(frame_num1, text="Số thứ nhất:").pack(side=tk.LEFT)
entry_num1 = tk.Entry(frame_num1)
entry_num1.pack(side=tk.LEFT, padx=5)

# Khung nhập số thứ hai
frame_num2 = tk.Frame(window)
frame_num2.pack(pady=10)
tk.Label(frame_num2, text="Số thứ hai:  ").pack(side=tk.LEFT)
entry_num2 = tk.Entry(frame_num2)
entry_num2.pack(side=tk.LEFT, padx=5)

# Khung chứa các nút phép tính
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Tạo các nút phép tính
button_add = tk.Button(button_frame, text="+", command=lambda: calculate("+"), width=10)
button_sub = tk.Button(button_frame, text="-", command=lambda: calculate("-"), width=10)
button_mul = tk.Button(button_frame, text="×", command=lambda: calculate("*"), width=10)
button_div = tk.Button(button_frame, text="÷", command=lambda: calculate("/"), width=10)

# Đặt vị trí các nút
button_add.pack(side=tk.LEFT, padx=5)
button_sub.pack(side=tk.LEFT, padx=5)
button_mul.pack(side=tk.LEFT, padx=5)
button_div.pack(side=tk.LEFT, padx=5)

# Nhãn hiển thị kết quả
result_label = tk.Label(window, text="Kết quả: ", font=("Arial", 14))
result_label.pack(pady=20)

# Chạy chương trình
window.mainloop()