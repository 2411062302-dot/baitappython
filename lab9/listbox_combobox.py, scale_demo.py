import tkinter as tk
from tkinter import ttk

# 1. Tạo 1 cửa sổ duy nhất
cua_so = tk.Tk()
cua_so.title("Demo Combobox và Scale")
cua_so.geometry("300x400")

# 2. Các phần tử của Combobox (Code cũ của bạn từ dòng 23)
tk.Label(cua_so, text="Chọn thành phố:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Bạn chọn: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xác nhận", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

# 3. Các phần tử của Scale (Code cũ của bạn từ dòng 39)
def khi_keo_thanh_truot(gia_tri):
    nhan_gia_tri.config(text=f"Giá trị hiện tại: {gia_tri}")

thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal", command=khi_keo_thanh_truot)
thanh_truot.pack(pady=20, padx=20, fill="x")

nhan_gia_tri = tk.Label(cua_so, text="Giá trị hiện tại: 0")
nhan_gia_tri.pack()

# 4. Gọi mainloop MỘT LẦN DUY NHẤT ở cuối file
cua_so.mainloop()