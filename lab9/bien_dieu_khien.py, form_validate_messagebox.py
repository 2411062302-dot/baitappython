import tkinter as tk
from tkinter import messagebox

# Danh sách lưu trữ công việc dưới dạng tuple: (nội_dung_công_việc, trạng_thái_hoàn_thành)
danh_sach_cong_viec = []

# --- CÁC HÀM XỬ LÝ LỘGIC ---

def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)
    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        tien_to = "[Da xong] " if da_hoan_thanh else "[Chua xong] "
        listbox_cong_viec.insert(tk.END, tien_to + noi_dung)

def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()
    if noi_dung == "":
        messagebox.showerror("Lỗi", "Vui lòng nhập nội dung công việc trước khi thêm.")
        return
    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")
    lam_moi_listbox()

def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn một công việc trong danh sách để xóa.")
        return
    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)
    lam_moi_listbox()

def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn một công việc để đánh dấu.")
        return
    vi_tri = lua_chon[0]
    noi_dung, da_hoan_thanh = danh_sach_cong_viec[vi_tri]
    # Cập nhật trạng thái thành True (Đã hoàn thành)
    danh_sach_cong_viec[vi_tri] = (noi_dung, True)
    lam_moi_listbox()


# --- PHẦN XÂY DỰNG GIAO DIỆN (GUI) ---

cua_so = tk.Tk()
cua_so.title("Ứng Dụng Quản Lý Công Việc")
cua_so.geometry("400x400")

# Biến để lấy dữ liệu từ ô nhập
bien_cong_viec_moi = tk.StringVar()

# Khu vực nhập liệu
frame_nhap = tk.Frame(cua_so)
frame_nhap.pack(pady=15)

tk.Entry(frame_nhap, textvariable=bien_cong_viec_moi, width=35).pack(side=tk.LEFT, padx=5)
tk.Button(frame_nhap, text="Thêm", command=them_cong_viec, bg="lightblue").pack(side=tk.LEFT)

# Khu vực hiển thị danh sách
listbox_cong_viec = tk.Listbox(cua_so, width=50, height=12, selectmode=tk.SINGLE)
listbox_cong_viec.pack(pady=10)

# Khu vực nút chức năng
frame_chuc_nang = tk.Frame(cua_so)
frame_chuc_nang.pack(pady=5)

tk.Button(frame_chuc_nang, text="Đánh dấu hoàn thành", command=danh_dau_hoan_thanh, bg="lightgreen").pack(side=tk.LEFT, padx=10)
tk.Button(frame_chuc_nang, text="Xóa công việc", command=xoa_cong_viec, bg="salmon").pack(side=tk.LEFT, padx=10)

# Khởi chạy vòng lặp giao diện
cua_so.mainloop()