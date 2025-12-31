import customtkinter as ctk
from tkinter import colorchooser
def new_win():
    # 🖌️ پنجره اصلی
    main = ctk.CTk()
    main.title("Mini Paint")
    main.geometry("800x600")
    main.resizable(False, False)
    main.configure(fg_color="#0F0359")
    

    frame = ctk.CTkFrame(main)
    frame.pack(pady=10)

    pen_defult = "black"

    def change_color():
        
        color = colorchooser.askcolor()[1]
        canvas.configure(bg=color)
        # color_button.configure(fg_color="#2A0D9F")
    def change_color_pen():
        nonlocal pen_defult
        color = colorchooser.askcolor()[1]
        if color:
            pen_defult= color

    btn = ctk.CTkButton(frame,text="Background color",command=change_color)
    btn.pack(pady=10,padx=10,side="left")

    btn1 = ctk.CTkButton(frame,text="Pen color",command=change_color_pen)
    btn1.pack(pady=10,padx=10,side="right")

    # 🖼️ Canvas برای نقاشی
    canvas = ctk.CTkCanvas(main, bg="white", width=800, height=500)
    canvas.pack(pady=10)

    # 🖍️ متغیر برای دنبال کردن آخرین موقعیت ماوس
    last_x, last_y = None, None

    # تابع شروع نقاشی
    def start_paint(event):
        global last_x, last_y
        last_x, last_y = event.x, event.y

    # تابع کشیدن نقاشی
    def paint(event):
        global last_x, last_y
        if last_x and last_y:
            canvas.create_line(last_x, last_y, event.x, event.y, width=3, fill=pen_defult, capstyle="round", smooth=True)
        last_x, last_y = event.x, event.y

    # تابع پایان نقاشی
    def reset(event):
        global last_x, last_y
        last_x, last_y = None, None

    # اتصال ماوس به توابع
    canvas.bind("<Button-1>", start_paint)
    canvas.bind("<B1-Motion>", paint)
    canvas.bind("<ButtonRelease-1>", reset)

    main.mainloop()
