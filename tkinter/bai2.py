import tkinter as tk
from tkinter import messagebox
import math

def giai_pt():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            if b == 0:
                if c == 0:
                    entry_kq.delete(0, tk.END)
                    entry_kq.insert(0, "Vô số nghiệm")
                else:
                    entry_kq.delete(0, tk.END)
                    entry_kq.insert(0, "Vô nghiệm")
            else:
                x = -c / b
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, f"PT bậc 1: x = {x}")
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, "Vô nghiệm")
            elif delta == 0:
                x = -b / (2*a)
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, f"x = {x}")
            else:
                sqrt_delta = math.sqrt(delta)
                x1 = (-b + sqrt_delta) / (2*a)
                x2 = (-b - sqrt_delta) / (2*a)
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def tiep_tuc():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_kq.delete(0, tk.END)

def thoat():
    root.destroy()

# Giao diện
root = tk.Tk()
root.title("PTB2")
root.geometry("250x180")
root.resizable(True,True)

# Tiêu đề
label_title = tk.Label(root, text="Phương Trình Bậc 2", fg="red", font=("Arial", 16, "bold"))
label_title.pack(pady=5)

# Frame nhập hệ số
frame_inputs = tk.Frame(root)
frame_inputs.pack()

tk.Label(frame_inputs, text="Hệ số a:").grid(row=0, column=0, sticky='e')
entry_a = tk.Entry(frame_inputs)
entry_a.grid(row=0, column=1)

tk.Label(frame_inputs, text="Hệ số b:").grid(row=1, column=0, sticky='e')
entry_b = tk.Entry(frame_inputs)
entry_b.grid(row=1, column=1)

tk.Label(frame_inputs, text="Hệ số c:").grid(row=2, column=0, sticky='e')
entry_c = tk.Entry(frame_inputs)
entry_c.grid(row=2, column=1)

# Nút chức năng
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_giai = tk.Button(frame_buttons, text="Giải", width=4, command=giai_pt)
btn_giai.grid(row=0, column=0)

btn_tiep = tk.Button(frame_buttons, text="Tiếp", width=4, command=tiep_tuc)
btn_tiep.grid(row=0, column=1)

btn_thoat = tk.Button(frame_buttons, text="Thoát", width=4, command=thoat)
btn_thoat.grid(row=0, column=2)

# Kết quả
frame_kq = tk.Frame(root)
frame_kq.pack(pady=5)

tk.Label(frame_kq, text="Kết quả:").grid(row=0, column=0)
entry_kq = tk.Entry(frame_kq, width=30)
entry_kq.grid(row=0, column=1)

root.mainloop()
