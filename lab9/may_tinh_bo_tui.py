import tkinter as tk
from tkinter import messagebox

# Các hàm xử lý
def nhan_nut(gia_tri):
    hien_tai = bien_man_hinh.get()
    bien_man_hinh.set(hien_tai + str(gia_tri))

def xoa_man_hinh():
    bien_man_hinh.set("")

def tinh_ket_qua():
    try:
        bieu_thuc = bien_man_hinh.get()
        # Đổi dấu ^ thành ** để Python hiểu là lũy thừa
        bieu_thuc = bieu_thuc.replace('^', '**')
        # Hàm eval() giúp tự động tính toán chuỗi phép tính
        ket_qua = str(eval(bieu_thuc))
        bien_man_hinh.set(ket_qua)
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0!")
        bien_man_hinh.set("")
    except Exception:
        messagebox.showerror("Lỗi", "Phép tính không hợp lệ!")
        bien_man_hinh.set("")

# --- TẠO GIAO DIỆN ---
cua_so = tk.Tk()
cua_so.title("Máy Tính Bỏ Túi")
cua_so.geometry("320x420")
cua_so.resizable(False, False)

# Màn hình hiển thị
bien_man_hinh = tk.StringVar()
man_hinh = tk.Entry(cua_so, textvariable=bien_man_hinh, font=('Arial', 24), bd=8, justify='right')
man_hinh.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Cấu hình các nút bấm
danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Tạo các nút bấm bằng vòng lặp
for (ky_tu, hang, cot) in danh_sach_nut:
    if ky_tu == '=':
        tk.Button(cua_so, text=ky_tu, font=('Arial', 18, 'bold'), bg='lightblue', 
                  command=tinh_ket_qua).grid(row=hang, column=cot, sticky="nsew", padx=5, pady=5)
    elif ky_tu == 'C':
        tk.Button(cua_so, text=ky_tu, font=('Arial', 18, 'bold'), bg='salmon', 
                  command=xoa_man_hinh).grid(row=hang, column=cot, sticky="nsew", padx=5, pady=5)
    else:
        tk.Button(cua_so, text=ky_tu, font=('Arial', 18), 
                  command=lambda t=ky_tu: nhan_nut(t)).grid(row=hang, column=cot, sticky="nsew", padx=5, pady=5)

# Chỉnh cho các cột/hàng đều nhau
for i in range(4):
    cua_so.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    cua_so.grid_rowconfigure(i, weight=1)

# Chạy vòng lặp giao diện
cua_so.mainloop()