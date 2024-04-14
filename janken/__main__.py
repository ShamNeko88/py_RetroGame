import tkinter as tk
from tkinter import ttk
from data import data_test as dtest

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
        # ヘッダーフレーム作成
        self.header_zone = tk.Frame(self.master)
        self.header_zone.config(width=1000, height=50, background="gray")
        self.header_zone.grid(row=0, column=0, columnspan=2)
        # ログインボタン
        self.login_btn = ttk.Button(self.header_zone, text="ログイン")
        self.login_btn.place(x=800, y=10)
        # ログインユーザー名
        self.login_user_name = ttk.Label(self.header_zone, text="test_user1", font=10)
        self.login_user_name.place(x=880, y=10)

        # ******** ゲームゾーン *************
        # ゲームゾーン作成
        self.game_zone = tk.Frame(self.master)
        self.game_zone.config(width=800, height= 450, background="skyblue")
        self.game_zone.grid(row=1, column=0)

        # ******* 成績ゾーン **********
        # 成績ゾーン作成
        self.score_zone = tk.Frame(self.master)
        self.score_zone.config(width=200, height=450, background="green")
        self.score_zone.grid(row=1, column=1)
        # Excel出力ボタン
        self.export_excel_btn = ttk.Button(self.score_zone, text="EXCEL", command=self.export_excel)
        self.export_excel_btn.place(x=10, y=420)
        # CSV出力ボタン
        self.export_csv_btn = ttk.Button(self.score_zone, text="CSV", command=self.export_csv)
        self.export_csv_btn.place(x=110, y=420)
        # 成績更新ボタン
        self.upd_score_btn = ttk.Button(self.score_zone, text="更新", command=self.upd_score)
        self.upd_score_btn.place(x=55, y=5)
        # プレイ回数
        self.play_cnt = ttk.Label(self.score_zone, text=f"プレイ回数：{dtest.test1}")
        self.play_cnt.place(x=10, y= 50)

    # 成績更新処理
    def upd_score(self):
        print("更新")

    # EXCEL出力
    def export_excel(self):
        print("excel出力")
    
    # CSV出出力
    def export_csv(self):
        print("CSV出力")

if __name__ == "__main__":
    root = tk.Tk()
    App = Application(root)
    App.mainloop()