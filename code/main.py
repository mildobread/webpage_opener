import requests
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


ICON_URL = "https://github.com/mildobread/webpage_opener/blob/main/bear_icon.png?raw=true"
ICON_PATH = "bear_icon.png"
PADY = 5


class WebPageOpener:
    def __init__(self, root):
        self.master = root
        self.master.title("HeavyChild")
        self._create_widgets()
        self._download_icon()

    def _download_icon(self):
        print("bear_icon downloading...")
        response = requests.get(ICON_URL)
        if response.status_code == 200:
            with open(ICON_PATH, 'wb') as f:
                f.write(response.content)
        else:
            print("can not download image.")
        icon = tk.PhotoImage(file=ICON_PATH)
        self.master.iconphoto(True, icon)

    def _open_webpage(self):
        url = self.entry.get()
        print(f"Webpage opening: {url}")
        driver = ChromeDriver.getDriver()
        driver.get(url)
        self.master.wait_window()

    def _button_clicked(self):
        print("Button Clicked.")
        self._open_webpage()

    def _create_widgets(self):
        print("creating widgets...")
        self._create_label()
        self._create_entry()
        self._create_button()
        self._register_key_event()

    def _create_button(self):
        print("creating button...")
        self.button = tk.Button(self.master, text="Open Webpage", command=self._button_clicked)
        self.button.pack(pady=PADY)

    def _create_label(self):
        print("creating label...")
        label = tk.Label(self.master, text="Enter webpage URL :")
        label.pack(pady=PADY)

    def _create_entry(self):
        print("creating entry...")
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=PADY)

    def _register_key_event(self):
        print("register key events...")
        self.master.bind("<Return>", self._key_event_enter)

    def _key_event_enter(self, event):
        if event.keysym == "Return":
            print("ENTER.")
            self._open_webpage()


class ChromeDriver:
    driver = None
    chrome_service = None
    chrome_options = None

    @classmethod
    def download_chromedriver(cls):
        print("chromedriver downloading...")
        cls.chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        cls.chrome_service.start()
        cls.chrome_options = webdriver.ChromeOptions()
        cls.chrome_options.add_experimental_option("prefs", {
            "profile.managed_default_content_settings.javascript": 2
        })
        print("chromedriver download is finished!")

    @classmethod
    def getDriver(cls):
        if cls.chrome_service == None:
            ChromeDriver.download_chromedriver()
        cls.driver = webdriver.Chrome(service=cls.chrome_service, options=cls.chrome_options)
        return cls.driver


def main():
    ChromeDriver.download_chromedriver()

    root = tk.Tk()
    app = WebPageOpener(root)
    root.mainloop()


if __name__ == "__main__":
    main()
