import tkinter as tk
from selenium import webdriver

def open_webpage():
    url = entry.get()
    chrome_driver_path = "C:/Users/82105/Desktop/polarbear/chromedriver/chromedriver.exe"
    chrome_service = webdriver.chrome.service.Service(chrome_driver_path)
    chrome_service.start()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)
    root.wait_window()

#enter key binding BY jihyun
def on_enter(event):
    if event.keysym == "Return":
        open_webpage()
        print("Press Enter Key")

root = tk.Tk()
root.title("Webpage Opener")
icon_path = "C:/Users\82105/Desktop/polarbear/bear_icon.ico"
root.iconbitmap(icon_path)

label = tk.Label(root, text="Enter webpage URL:")
label.pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

#enter key binding BY jihyun
root.bind("<Return>", on_enter)

button = tk.Button(root, text="Open Webpage", command=open_webpage)
button.pack(pady=5)

root.mainloop()
