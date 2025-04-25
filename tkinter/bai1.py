import tkinter as tk
from tkinter import messagebox

def giai_pt():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            if b == 0:
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, "Vô số nghiệm")
            else:
                entry_kq.delete(0, tk.END)
                entry_kq.insert(0, "Vô nghiệm")
        else:
            x = -b / a
            entry_kq.delete(0, tk.END)
            entry_kq.insert(0, f"x = {x}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def tiep_tuc():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_kq.delete(0, tk.END)

def thoat():
    root.destroy()

# Giao diện chính
root = tk.Tk()
root.title("PTB1")
root.geometry("230x160")
root.resizable(False, False)

# Tiêu đề
label_title = tk.Label(root, text="Phương Trình Bậc 1", fg="red", font=("Arial", 16, "bold"))
label_title.pack(pady=5)

# Frame nhập hệ số
frame_inputs = tk.Frame(root)
frame_inputs.pack()

tk.Label(frame_inputs, text="Hệ số a:").grid(row=0, column=0,)
entry_a = tk.Entry(frame_inputs)
entry_a.grid(row=0, column=1)

tk.Label(frame_inputs, text="Hệ số b:").grid(row=1, column=0,)
entry_b = tk.Entry(frame_inputs).grid(row=1, column=1)

# Nút chức năng
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=1)

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
entry_kq = tk.Entry(frame_kq, width=25)
entry_kq.grid(row=0, column=1)

root.mainloop()
