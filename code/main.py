import requests
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


ICON_URL = "https://github.com/mildobread/webpage_opener/blob/main/bear_icon.png?raw=true"
ICON_PATH = "bear_icon.png"


class WebPageOpener:
    def __init__(self, root):
        self.master = root
        self.master.title("HeavyChild")
        self._create_widgets()
        self._download_icon()
        self._download_chromedriver()

    def _download_icon(self):
        response = requests.get(ICON_URL)
        if response.status_code == 200:
            with open(ICON_PATH, 'wb') as f:
                f.write(response.content)
        else:
            print("이미지를 다운로드할 수 없습니다.")
        icon = tk.PhotoImage(file=ICON_PATH)
        self.master.iconphoto(True, icon)

    def _download_chromedriver(self):
        print("chromedriver downloading...")
        self.chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        self.chrome_service.start()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.javascript": 2})
        print("chromedriver download is finished!")

    def _open_webpage(self):
        url = self.entry.get()
        driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
        driver.get(url)
        self.master.wait_window()

    def _button_clicked(self):
        self._open_webpage()

    def _create_widgets(self):
        print("creating widgets...")
        self._create_label()
        self._create_entry()
        self._create_button()
        self._register_key_event()

    def _create_button(self):
        button = tk.Button(self.master, text="Open Webpage", command=self._button_clicked)
        button.pack(pady=5)

    def _create_label(self):
        label = tk.Label(self.master, text="Enter webpage URL :")
        label.pack(pady=5)

    def _create_entry(self):
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=5)

    def _register_key_event(self):
        self.master.bind("<Return>", self._key_event_enter)

    def _key_event_enter(self, event):
        if event.keysym == "Return":
            self._button_clicked()


def main():
    root = tk.Tk()
    app = WebPageOpener(root)
    root.mainloop()

if __name__ == "__main__":
    main()
