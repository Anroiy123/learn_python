import tkinter as tk
from tkinter import messagebox

def tinh_toan(phep_tinh):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if phep_tinh == '+':
            kq = a + b
        elif phep_tinh == '-':
            kq = a - b
        elif phep_tinh == '*':
            kq = a * b
        elif phep_tinh == '/':
            if b == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0")
                return
            kq = a / b
        entry_kq.delete(0, tk.END)
        entry_kq.insert(0, str(kq))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def thoat():
    root.destroy()

# Cửa sổ chính
root = tk.Tk()
root.title("Cộng trừ nhân chia")
root.geometry("260x160")
root.resizable(False, False)

# Tiêu đề
lbl_title = tk.Label(root, text="Cộng trừ nhân chia",fg = "blue", font=("Arial", 16, "bold"))
lbl_title.grid(row=0, column=0, columnspan=3, pady=5)

# Các nút phép tính5
btn_cong = tk.Button(root, text="Cộng", width=8, command=lambda: tinh_toan('+'))
btn_cong.grid(row=1, column=0, padx=5, pady=2)

btn_tru = tk.Button(root, text="Trừ", width=8, command=lambda: tinh_toan('-'))
btn_tru.grid(row=2, column=0, padx=5, pady=2)

btn_nhan = tk.Button(root, text="Nhân", width=8, command=lambda: tinh_toan('*'))
btn_nhan.grid(row=3, column=0, padx=5, pady=2)

btn_chia = tk.Button(root, text="Chia", width=8, command=lambda: tinh_toan('/'))
btn_chia.grid(row=4, column=0, padx=5, pady=2)

# Nhập liệu và kết quả
tk.Label(root, text="số a:").grid(row=1, column=1, sticky='e')
entry_a = tk.Entry(root, width=10)
entry_a.grid(row=1, column=2, padx=5)

tk.Label(root, text="số b:").grid(row=2, column=1, sticky='e')
entry_b = tk.Entry(root, width=10)
entry_b.grid(row=2, column=2, padx=5)

tk.Label(root, text="kết quả:").grid(row=3, column=1, sticky='e')
entry_kq = tk.Entry(root, width=10)
entry_kq.grid(row=3, column=2, padx=5)

# Nút thoát
btn_thoat = tk.Button(root, text="thoát", width=8, command=thoat)
btn_thoat.grid(row=4, column=2, pady=5)

root.mainloop()
