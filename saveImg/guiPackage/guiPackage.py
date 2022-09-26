
# GUI作成
import PySimpleGUI as sg

# 日付取得用
import datetime

# データベース管理
import sqlite3
from contextlib import closing

# 関数定義
def inputGui():

# デザインテーマの設定
    sg.theme('BlueMono')

    # ウィンドウに配置するコンポーネント
    # layout = [  [sg.Text('メンバー名をフルネームで記入してください。')],
    #             [sg.Text('記入欄'), sg.InputText(key='-InputText-')],
    #             [sg.Button('決定'), sg.Button('終了')] ]    # ウィンドウに配置するコンポーネント
    layout = [  [sg.Text('メンバー名を選択してください。')],
                [sg.Text('記入欄'), sg.Combo(values=[\
                    # 4期生\
                    '掛橋沙耶香',\
                    '佐藤璃果',\
                    '田村真佑',\
                    '筒井あやめ',\
                    '林瑠奈',\
                    '弓木奈於',\
                    # 5期生\
                    '一ノ瀬美空',\
                    '小川彩',\
                    '川崎桜',\
                    '中西アルノ',\

                        ], size=(10,1), key='-InputText-')],
                [sg.Button('決定'), sg.Button('終了')]]

    # ウィンドウの生成
    window = sg.Window('メンバー選択', layout)

    # 追加日を取得
    # d_today = datetime.date.today()
    d_today = datetime.date.today().strftime('%Y/%m/%d')

    # イベントループ
    while True:
        event, values = window.read()  # type: ignore
        if event == sg.WIN_CLOSED:
            break
        elif event == '決定':
            r_name = values['-InputText-']
            break


            # アプリ終了時の処理
        elif event == '終了':
            print('アプリを終了します。')
            break
    window.close()
    return r_name
# %%
