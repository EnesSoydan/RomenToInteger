import tkinter as tk
from tkinter import messagebox

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding=2, bg="#2980b9", fg="white", text="", command=None):
        super().__init__(parent, borderwidth=0, relief="flat", highlightthickness=0)
        self.command = command
        if cornerradius > 0.5*width:
            raise ValueError("cornerradius cannot be greater than half width")
        if cornerradius > 0.5*height:
            raise ValueError("cornerradius cannot be greater than half height")

        self.width = width
        self.height = height
        self.cornerradius = cornerradius
        self.padding = padding
        self.bg = bg
        self.fg = fg
        self.text = text

        self.configure(width=width, height=height)

        self.create_rounded_rect(padding, padding, width - padding, height - padding, cornerradius, fill=bg, outline=bg)
        self.text_id = self.create_text(width//2, height//2, text=text, fill=fg, font=("Segoe UI", 14, "bold"))

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def create_rounded_rect(self, x1, y1, x2, y2, r=25, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_press(self, event):
        self.scale("all", self.width//2, self.height//2, 0.95, 0.95)
        self.configure(cursor="hand2")

    def _on_release(self, event):
        self.scale("all", self.width//2, self.height//2, 1/0.95, 1/0.95)
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.configure(cursor="hand2")

    def _on_leave(self, event):
        self.configure(cursor="")

def convert_roman_to_int():
    romen_format = entry.get().strip().upper()
    romen_to_int_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    if not romen_format:
        messagebox.showwarning("Uyarı", "Lütfen bir Roma rakamı girin.")
        return

    arabic_value = 0
    prev_value = 0
    prev_char = ""
    repeat_count = 0
    failure = False

    for i in reversed(romen_format):
        if i not in romen_to_int_dict:
            messagebox.showerror("Hata", f"Geçersiz karakter: {i}")
            return

        value = romen_to_int_dict[i]

        if i == prev_char:
            repeat_count += 1
            if repeat_count > 3:
                failure = True
                break
        else:
            repeat_count = 1

        if value < prev_value:
            arabic_value -= value
        else:
            arabic_value += value
            prev_value = value

        prev_char = i

    if failure:
        result_label.config(text="Bir rakam en fazla 3 kez tekrar edebilir!", fg="#d9534f")
    else:
        result_label.config(text=f"Sayısal değer: {arabic_value}", fg="#5cb85c")

BG_COLOR = "#f2f4f7"
ENTRY_BG = "#ffffff"
ENTRY_BORDER = "#ced4da"
BUTTON_BG = "#6c757d"
BUTTON_FG = "#ffffff"
LABEL_FG = "#343a40"

root = tk.Tk()
root.title("Roma Rakamı Çevirici")
root.geometry("480x280")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

title_label = tk.Label(root, text="Roma Rakamını Sayısal Değere Çevir",
                       font=("Segoe UI", 16, "bold"), fg=LABEL_FG, bg=BG_COLOR)
title_label.pack(pady=(20, 15))

entry_shadow = tk.Frame(root, bg="#adb5bd")
entry_shadow.pack(pady=12)

entry_canvas = tk.Canvas(entry_shadow, width=360, height=44, bg=BG_COLOR, highlightthickness=0)
entry_canvas.pack()

r = 15
w = 360
h = 44
x1, y1, x2, y2 = 2, 2, w-2, h-2
points = [
    x1+r, y1,
    x2-r, y1,
    x2, y1,
    x2, y1+r,
    x2, y2-r,
    x2, y2,
    x2-r, y2,
    x1+r, y2,
    x1, y2,
    x1, y2-r,
    x1, y1+r,
    x1, y1,
]
entry_canvas.create_polygon(points, smooth=True, fill=ENTRY_BG, outline=ENTRY_BORDER)

entry = tk.Entry(entry_canvas, font=("Segoe UI", 14), bd=0, bg=ENTRY_BG, fg=LABEL_FG, justify="center")
entry.place(x=15, y=8, width=w-30, height=h-16)

def on_button_click():
    convert_roman_to_int()

button = RoundedButton(root, width=160, height=50, cornerradius=25,
                       bg=BUTTON_BG, fg=BUTTON_FG, text="Çevir", command=on_button_click)
button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg=BG_COLOR, fg=LABEL_FG)
result_label.pack(pady=15)

root.mainloop()
