import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# 手のアイコン
LOGIN_USER = "test_user"
ROCK = "./data/グー.png"
SCISSORS = "./data/チョキ.png"
PAPER = "./data/パー.png"
ROTATED_ROCK = Image.open("./data/グー.png").rotate(180) # 180度回転
ROTATED_SCISSORS = Image.open("./data/チョキ.png").rotate(180) # 180度回転
ROTATED_PAPER = Image.open("./data/パー.png").rotate(180) # 180度回転

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # ウィンドウの設定
        self.master.title("じゃんけん")
        self.master.geometry("800x500")
        self.master.resizable(False, False)
        # ウィジェットの配置
        self.set_widgets()

    # ウィジェットの配置
    def set_widgets(self):
        # ******** ヘッダーゾーン *************
        # ヘッダーフレーム作成
        self.header_zone = tk.Frame(self.master)
        self.header_zone.config(width=800, height=50, background="LightSkyBlue1")
        self.header_zone.grid(row=0, column=0, columnspan=2)
        
        # ユーザーの管理
        self.users_btn = ttk.Button(self.header_zone, text="ユーザー管理", command=self.user_manager)
        self.users_btn.place(x=30, y=10)
        
        # ログインボタン
        self.login_btn = ttk.Button(self.header_zone, text="ログイン", command=self.login)
        self.login_btn.place(x=500, y=10)
        
        # ログインユーザー名
        self.login_user_name = ttk.Label(self.header_zone, text=f"ユーザー：  {LOGIN_USER}", font=12, relief=tk.FLAT, background="LightSkyBlue1")
        self.login_user_name.place(x=590, y=10, width=200, height=30)

        # ******** ゲームゾーン *************
        # ゲームゾーン作成
        self.game_zone = tk.Frame(self.master)
        self.game_zone.config(width=600, height= 450, background="")
        self.game_zone.grid(row=1, column=0)
        
        # 敵の手（グー）
        self.enemy_rock_img = ROTATED_ROCK.resize((ROTATED_ROCK.width // 3, ROTATED_ROCK.height // 3))
        self.enemy_rock_img = ImageTk.PhotoImage(self.enemy_rock_img)
        self.enemy_rock = ttk.Button(self.game_zone, image=self.enemy_rock_img, padding=0)
        self.enemy_rock.place(x=250, y=10)
        
        # 敵の手（チョキ）
        self.enemy_scissors_img = ROTATED_SCISSORS.resize((ROTATED_SCISSORS.width // 3, ROTATED_SCISSORS.height // 3))
        self.enemy_scissors_img = ImageTk.PhotoImage(self.enemy_scissors_img)
        self.enemy_scissors = ttk.Button(self.game_zone, image=self.enemy_scissors_img, padding=0)
        self.enemy_scissors.place(x=320, y=10)
        
        # 敵の手（パー）
        self.enemy_paper_img = ROTATED_PAPER.resize((ROTATED_PAPER.width // 3, ROTATED_PAPER.height // 3))
        self.enemy_paper_img = ImageTk.PhotoImage(self.enemy_paper_img)
        self.enemy_paper = ttk.Button(self.game_zone, image=self.enemy_paper_img, padding=0)
        self.enemy_paper.place(x=390, y=10)
        
        # 自分の手（グー）
        self.rock_img = tk.PhotoImage(file=ROCK)
        self.rock_img = self.rock_img.subsample(3, 3)
        self.my_rock = ttk.Button(self.game_zone, image=self.rock_img, padding=0, command=lambda:self.my_hand("rock"))
        self.my_rock.place(x=250, y=320)
        
        # 自分の手（チョキ）
        self.scissors_img = tk.PhotoImage(file=SCISSORS)
        self.scissors_img = self.scissors_img.subsample(3, 3)
        self.my_scissors = ttk.Button(self.game_zone, image=self.scissors_img, padding=0, command=lambda:self.my_hand("scissors"))
        self.my_scissors.place(x=320, y=320)
        
        # 自分の手（パー）
        self.paper_img = tk.PhotoImage(file=PAPER)
        self.paper_img = self.paper_img.subsample(3, 3)
        self.my_paper = ttk.Button(self.game_zone, image=self.paper_img, padding=0, command=lambda:self.my_hand("paper"))
        self.my_paper.place(x=390, y=320)
        
        # リトライボタン
        self.retry_btn = ttk.Button(self.game_zone, text="リトライ", command=self.retry)
        self.retry_btn.place(x=320, y=410)

        # ******* 成績ゾーン **********
        # 成績ゾーン作成
        self.score_zone = tk.Frame(self.master)
        self.score_zone.config(width=200, height=450, background="light yellow")
        self.score_zone.grid(row=1, column=1)
        # Excel出力ボタン
        self.export_excel_btn = ttk.Button(self.score_zone, text="EXCEL", command=self.export_excel)
        self.export_excel_btn.place(x=10, y=380)
        # CSV出力ボタン
        self.export_csv_btn = ttk.Button(self.score_zone, text="CSV", command=self.export_csv)
        self.export_csv_btn.place(x=110, y=380)
        # 成績更新ボタン
        self.upd_score_btn = ttk.Button(self.score_zone, text="更新", command=self.upd_score)
        self.upd_score_btn.place(x=55, y=5)
        # プレイ回数
        self.play_cnt = ttk.Label(self.score_zone, text=f"試合数：", background="light yellow", font=12)
        self.play_cnt.place(x=10, y= 80)
        # 勝利数
        self.win_cnt = ttk.Label(self.score_zone, text="勝利数：", background="light yellow", font=12)
        self.win_cnt.place(x=10, y=110)
        # 敗北数
        self.lose_cnt = ttk.Label(self.score_zone, text="敗北数：", background="light yellow", font=12)
        self.lose_cnt.place(x=10, y=140)
        # あいこ数
        self.draw_cnt = ttk.Label(self.score_zone, text="分け数：", background="light yellow", font=12)
        self.draw_cnt.place(x=10, y=170)
        # ポイント数
        self.point = ttk.Label(self.score_zone, text="ポイント数：", background="light yellow", font=12)
        self.point.place(x=10, y=200)
    
    # ********* ヘッダーゾーン ************
    # ユーザー管理画面
    def user_manager(self):
        user_manager = SubWindow(self, "user_manager")

    # ログイン処理
    def login(self):
        login = SubWindow(self, "login")
    
    # ********* 成績ゾーン *************
    # 成績更新処理
    def upd_score(self):
        print("成績更新")
    
    # EXCEL出力
    def export_excel(self):
        print("excel出力")
    
    # CSV出出力
    def export_csv(self):
        print("CSV出力")
    # ********* ゲームゾーン **********
    # 自分の手を選択
    def my_hand(self, hand):
        print(f"{hand}を出した")

    # リトライ
    def retry(self):
        print("リトライ")

"""
別ウィンドウ
"""
class SubWindow():
    def __init__(self, master, mode):
        # パラメーターの受け取り
        self.master = master
        self.mode = mode
        
        # サブウィンドウとウィジェットの描画
        if mode == "login":
            self.sub_window = tk.Toplevel()
            self.sub_window.title("ログイン画面")
            self.sub_window.geometry("300x200")
            self.sub_window.resizable(False, False)
            self.sub_window.grab_set()
            self.set_login()
        elif mode == "user_manager":
            self.sub_window = tk.Toplevel()
            self.sub_window.title("ユーザー管理画面")
            self.sub_window.geometry("480x250")
            self.sub_window.resizable(False, False)
            self.sub_window.grab_set()
            self.set_user_manager()
        
    # ログインウィジェット配置
    def set_login(self):
        # ログインユーザー名入力
        self.user_label = ttk.Label(self.sub_window, text="ユーザー名")
        self.user_label.place(x=60, y=40)
        self.stvar_user_entry = tk.StringVar()
        self.user_entry = ttk.Entry(self.sub_window, textvariable=self.stvar_user_entry)
        self.user_entry.place(x=120, y=40)

        # パスワード入力
        self.pass_label = ttk.Label(self.sub_window, text="パスワード")
        self.pass_label.place(x=60, y=90)
        self.stvar_pass_entry = tk.StringVar()
        self.pass_entry = ttk.Entry(self.sub_window, textvariable=self.stvar_pass_entry, show="*")
        self.pass_entry.place(x=120, y=90)
        
        # ログイン
        self.login = ttk.Button(self.sub_window, text="ログイン", command=self.login_process)
        self.login.place(x=140, y= 150)
    
    # ユーザー管理ウィジェット配置
    def set_user_manager(self):
        # ***** 表領域 *****
        # 表の設置
        user_table_columns = ("ID", "ユーザー名", "管理権限", "備考")
        self.table = ttk.Treeview(self.sub_window, columns=user_table_columns, selectmode="browse", show="headings", height=10)
        self.table.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W, padx=5)
        # 列の設定
        self.table.column("ID", anchor="center", width=50, stretch=False)
        self.table.column("ユーザー名", anchor="center", width=100, stretch=False)
        self.table.column("管理権限", anchor="center", width=70, stretch=False)
        self.table.column("備考", anchor="center", width=200, stretch=False)
        # ヘッダー設定
        self.table.heading("ID", text="ID", anchor="center")
        self.table.heading("ユーザー名", text="ユーザー名", anchor="center")
        self.table.heading("管理権限", text="管理権限", anchor="center")
        self.table.heading("備考", text="備考", anchor="center")

        # 縦スクロールバー
        vscrollbar = ttk.Scrollbar(self.sub_window, orient=tk.VERTICAL)
        vscrollbar.config(command=self.table.yview)
        vscrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.table.config(yscrollcommand=vscrollbar.set)

        # 横スクロールバー
        hscrollbar = ttk.Scrollbar(self.sub_window, orient=tk.HORIZONTAL)
        hscrollbar.config(command=self.table.xview)
        hscrollbar.grid(row=1, column=0, sticky=tk.EW)
        self.table.config(xscrollcommand=hscrollbar.set)

        # TODO ダミーデータ
        self.table.insert(parent="", index="end", iid=0, values=(
            "1", "test_user", "0", "ダミーデータです。これはテストの為のデータになります。"
        ))

    # ログイン実行
    def login_process(self):
        self.user_name = self.stvar_user_entry.get()
        self.password = self.stvar_pass_entry.get()
        print("ユーザー名：" + self.user_name)
        print("パスワード:" + self.password)

if __name__ == "__main__":
    root = tk.Tk()
    App = Application(root)
    App.mainloop()