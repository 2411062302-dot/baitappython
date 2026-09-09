import math

print("--- Bài tập 4.1 - Khai báo & tính bất biến ---")
toa_do = (3, 5)
print(toa_do, type(toa_do))

print("\n--- Bài tập 4.2 - Unpacking tuple ---")
x, y = toa_do
print("x =", x, "- y =", y)

a, b = 10, 20
a, b = b, a
print("a =", a, "b =", b)

print("\n--- Bài tập 4.3 - Trả về nhiều giá trị từ một biểu thức ---")
c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du
print(f"{c} chia {d} duoc {thuong} du {du}")

print("\n--- Hoạt động 5: Vận dụng Tuple - Tọa độ điểm & khoảng cách ---")
diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b
khoang_cach = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

print("\n--- Yêu cầu thêm: Khoảng cách từ danh sách điểm đến gốc tọa độ ---")
cac_diem = [(0, 0), (3, 4), (6, 8)]
x0, y0 = (0, 0)

for diem in cac_diem:
    x, y = diem
    kc = math.sqrt((x - x0)**2 + (y - y0)**2)
    print(f"Khoang cach tu {diem} den goc toa do (0, 0) la: {round(kc, 2)}")