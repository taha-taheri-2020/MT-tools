import customtkinter
from deep_translator import GoogleTranslator



def new_win():
    main = customtkinter.CTk()
    main.title("ترجمه گر")
    main.geometry("450x250")
    main.resizable(False, False)
    main.configure(fg_color="#0F0359")
    


    entry1 = customtkinter.CTkEntry(main,placeholder_text="متن را وارد کنید",font=("vazirmatn", 22))
    entry1.grid(row=0,column=0,sticky="ew",padx=10,pady=10)

    lable = customtkinter.CTkLabel(main,font=("vazirmatn", 22),text="....")

    lable.grid(row=1,column=0,sticky="ew",padx=10,pady=10)

    btn1 = customtkinter.CTkButton(main,text="انگلیسی به فارسی",font=("vazirmatn", 22),command=lambda: trans("انگلیسی به فارسی"))
    btn1.grid(row=2,column=0,sticky="ew",padx=10,pady=10)

    btn2 = customtkinter.CTkButton(main,text="فارسی به انگلیسی",font=("vazirmatn", 22),command=lambda: trans("فارسی به انگلیسی"))
    btn2.grid(row=3,column=0,sticky="ew",padx=10,pady=10)

    def trans(transtype):
        
        text = entry1.get()
        if not text:
            lable.configure(text="متنی وارد نشده")
            return

        try:
            if transtype == "انگلیسی به فارسی":
                lable.configure(text=GoogleTranslator(source="en", target="fa").translate(text))
            elif transtype == "فارسی به انگلیسی":
                lable.configure(text=GoogleTranslator(source="fa", target="en").translate(text))
        except:
            lable.configure(text="خطا در ترجمه ❌")



    main.mainloop()
