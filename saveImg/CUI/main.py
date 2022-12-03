# %%
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time
import dictionary.lib as nogilib
import os

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "password":"4646"
}

# メンバー選択
# t_memberName = guiPackage.inputGui()
t_memberName = [
    '遠藤さくら',
    '賀喜遥香',
    '掛橋沙耶香',
    '金川紗耶',
    '佐藤璃果',
    '田村真佑',
    '筒井あやめ',
    '弓木奈於',
    '林瑠奈',
    '一ノ瀬美空',
    '小川彩',
    '川崎桜',
    '中西アルノ',]
# メンバー毎のURLを指定
t_dirName, t_memberUrl = nogilib.getNogiUrl(t_memberName)

# Webページ(先頭)を取得して解析する
for idx_url in range(0,len(t_memberName)):
    load_url_1st = t_memberUrl[idx_url]
    res = session.post(load_url_1st, data=login_info)
    res.raise_for_status() # エラーならここで例外を発生させる
    html = requests.get(load_url_1st)
    soup = BeautifulSoup(res.text, "html.parser")

    # 保存用フォルダを作る
    # Windowsの場合
    if os.name == 'nt':
        out_folder = Path("H:\\マイドライブ\\nogi\\" + str(t_dirName[idx_url]))
    elif os.name == 'posix':
        out_folder = Path("/Users/to106ki/Library/CloudStorage/GoogleDrive-to106ki.hoby@gmail.com/マイドライブ/nogi" + str(t_dirName[idx_url]))
    out_folder.mkdir(exist_ok=True)

    for element in soup.find_all("img"):
        src = element.get("src")

        # 絶対URLを作って、画像データを取得する
        image_url = urllib.parse.urljoin(load_url_1st, src)  # type: ignore
        try:
            imgdata = requests.get(image_url)

            # URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
            filename = image_url.split("/")[-1]
            out_path = out_folder.joinpath(filename)

            # 拡張子「gif」、「png」ファイルを保存しない。
            # ※不要なファイルのため。
            match = re.search("(gif|png)$", filename)
            if match:
                pass
            else:
                # 画像データを、ファイルに書き出す
                with open(out_path, "wb") as f:
                    f.write(imgdata.content)

                # 1回アクセスしたので1秒待つ
                time.sleep(1)
        except:
            print("Error")

    # Webページ(次ページ以降)を取得して解析する
    ## rangeの第二引数を最終ページに変更して使用すること。
    for page in range(2,50,1):
        load_url_next = load_url_1st + "?p=" + str(page)

        # URLが存在しているか確認
        try:
            f = urllib.request.urlopen(load_url_next)  # type: ignore
            print('OK:', load_url_next)
            f.close()
            res = session.post(load_url_next, data=login_info)

            html = requests.get(load_url_next)
            soup = BeautifulSoup(res.text, "html.parser")

            for element in soup.find_all("img"):
                src = element.get("src")

                # 絶対URLを作って、画像データを取得する
                image_url = urllib.parse.urljoin(load_url_1st, src)  # type: ignore
                try:
                    imgdata = requests.get(image_url)

                    # URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
                    filename = image_url.split("/")[-1]
                    out_path = out_folder.joinpath(filename)

                    # 拡張子「gif」、「png」ファイルを保存しない。
                    # ※不要なファイルのため。
                    match = re.search("(gif|png)$", filename)
                    if match:
                        pass
                    else:
                        # 画像データを、ファイルに書き出す
                        with open(out_path, "wb") as f:
                            f.write(imgdata.content)

                        # 1回アクセスしたので1秒待つ
                        time.sleep(1)
                except:
                    print("Error")

        except urllib.request.HTTPError:  # type: ignore
            print('Not found:', load_url_next)

    print("####### End save image !! #######")
    # %%
