import customtkinter
from tools import calculator , mtai, searchfile, paint, translate, camscan
import jdatetime




app = customtkinter.CTk()
app.geometry("900x600")
app.resizable(False, False)
app.title("MT Tools | برنامه‌ی کاربردی")


app.configure(fg_color="#130184")
title = customtkinter.CTkLabel(app, text="MT toolsبرنامه ی کاربردی", font=("vazirmatn", 24),text_color="#FFFFFF")

title.grid(row=0,column=0,sticky="ew",padx=20,pady=20)

label = customtkinter.CTkLabel(app, text="", font=("Arial", 24))
label.grid(row=1, column=0, sticky="ew", pady=10, padx=10)

def clock():
    now = jdatetime.datetime.now()
    timestr = now.strftime("%H:%M:%S %p  %Y/%m/%d")  # ساعت و تاریخ شمسی
    label.configure(text=timestr)
    label.after(1000, clock)

clock()



link_frame = customtkinter.CTkFrame(app)
link_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(10,30)) 
link_frame.configure(fg_color="#12046C")

# اگه خواستی همه سلول‌ها همگام بشن
link_frame.grid_columnconfigure((0,1,2), weight=2)

links = [
    ("ماشین حساب", 0, 0, calculator.new_win),("چت بات", 0, 1, mtai.new_win),("جستوجو فایل", 0, 2, searchfile.new_win),
    ("نقاشی", 1, 0, paint.new_win),("ترجمه گر", 1, 1, translate.new_win),("اسکن کامرا", 1, 2, camscan.new_win)
]

for text, row, cul, com in links:
    btn = customtkinter.CTkButton(
                link_frame,
                text=text,
                command=com,   
                font=("vazirmatn", 30)
            )
    btn.grid(row=row, column=cul, padx=5, pady=5, sticky="nsew")
    btn.configure(fg_color="#3A2DEB", hover_color="#402FAF")

bottom_frame = customtkinter.CTkFrame(app)
bottom_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0,10))
bottom_frame.configure(fg_color="#12046C")
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)



def about():
    win = customtkinter.CTk()
    win.geometry("700x500")
    win.title("درباره ما")
    win.resizable(False, False)
    lable = customtkinter.CTkLabel(
        win,
        text="""
برنامه‌ی کاربردی MT Tools

طراحی و توسعه:
محمد طاها طاهری

این نرم‌افزار با تمرکز بر سادگی،
سهولت استفاده و بهره‌گیری از
هوش مصنوعی و ابزارهای کاربردی
توسعه داده شده است.

این برنامه نتیجه‌ی تلاش و خلاقیت
محمد طاها طاهری و متین صادقی می‌باشد.

© تمامی حقوق محفوظ است.
"""
        ,
        font=("vazirmatn", 20)
    )
    lable.pack(padx=10,pady=10,fill="both",expand=True)
    win.mainloop()
    

about_btn = customtkinter.CTkButton(bottom_frame, text="درباره ما", font=("vazirmatn", 30), command=about)
about_btn.grid(row=0, column=0, padx=10, pady=5, sticky="w")
about_btn.configure(fg_color="#3A2DEB", hover_color="#402FAF")

lable_ab = customtkinter.CTkLabel(
    bottom_frame,
    text="""
این برنامه نتیجه‌ی تلاش و خلاقیت
محمد طاها طاهری و متین صادقی می‌باشد.
© تمامی حقوق محفوظ است.
""",
    font=("vazirmatn", 24),
    anchor="w"
)
lable_ab.grid(row=0, column=1, padx=10, pady=5, sticky="e")



app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)  # link_frame وزن بگیرد
app.grid_rowconfigure(3, weight=0)  # bottom_frame ثابت بماند

 # فاصله پایین بیشتر


app.mainloop()
# version 1.0 beta
# The End
# Author: Mohammad Taha Taheri

# این برنامه نتیجه‌ی تلاش و خلاقیت
# محمد طاها طاهری و متین صادقی است.
# © تمامی حقوق محفوظ است.

