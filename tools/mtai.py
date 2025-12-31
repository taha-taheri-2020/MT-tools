# استفاده از سرویس گپ جی‌پی‌تی با Python
import openai
from openai import OpenAI
import customtkinter



# ایجاد یک نمونه از کلاینت با کلید API
client = OpenAI(
    api_key='API',
    base_url='https://api.gapgpt.app/v1'
)
def new_win():
    main = customtkinter.CTk()
    main.geometry("800x550")
    main.title("چت بات")
    main.resizable(False, False)
    main.configure(fg_color="#0F0359")
    

    text = customtkinter.CTkTextbox(main, font=("vazirmatn", 24),width=800, height=450)

    text.grid(row=0, column=0, sticky="nsew", columnspan=2)

    input = customtkinter.CTkEntry(main, font=("vazirmatn", 24))
    input.grid(row=1, column=0, sticky="nsew",padx=10, pady=10)

    SYSTEM_PROMPT = """
تو یک چت‌بات فارسی هستی.
نام تو «هوشنگ» است.
اگر کاربر به هر شکلی درباره نام تو سؤال کرد
(مستقیم، غیرمستقیم، شوخی، کنایه، یا با جمله‌های متفاوت)،
باید بفهمی منظورش نام توست و پاسخ بده که نامت هوشنگ است.
"""

    def send_message(message):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content

 
    text = customtkinter.CTkTextbox(
    main, font=("vazirmatn", 24), width=800, height=450
    )
    text.grid(row=0, column=0, sticky="nsew", columnspan=2)

    text.tag_config("right", justify="right")

    def send():
        message = input.get()
        response = send_message(message)
        text.insert("end", f"شما: {message}\n\n", "right")
        text.insert("end", f"بات: {response}\n\n", "right")
        input.delete(0, "end")

    button = customtkinter.CTkButton(main, text="ارسال", font=("vazirmatn", 24), command=send)
    button.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    main.mainloop()