import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # ウィンドウの設定
        self.master.title("じゃんけん")
        self.master.geometry("1000x500")
        self.master.resizable(False, False)
        # ウィジェットの配置
        self.set_widgets()

    def set_widgets(self):
        # ******** ヘッダーゾーン *************
        self.header_zone = tk.Frame(self.master)
        self.header_zone.config(width=1000, height=50, background="green")
        self.header_zone.pack()
        # ******** ゲームゾーン *************
        self.game_zone = tk.Frame(self.master)
        self.game_zone.config(width=1000, height= 450, background="skyblue")
        self.game_zone.pack()
        # ******* 成績ゾーン **********
        # self.info_zone = tk.Frame(self.master)
        # self.info_zone.config(width=200, height=100, background="red")
        # self.info_zone.pack(anchor=tk.W)


if __name__ == "__main__":
    root = tk.Tk()
    App = Application(root)
    App.mainloop()