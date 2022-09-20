# %%
# 初期化
r_memberUrl = "default"
r_dirName = "default"

mydict= {
            # 4期生\
            "掛橋沙耶香":["KakehashiSayaka","https://nogiboard.blog.jp/archives/cat_169595.html"],
            "佐藤璃果":["SatoRika","https://nogiboard.blog.jp/archives/cat_169603.html"],
            "弓木奈於":["YumikiNao","https://nogiboard.blog.jp/archives/cat_169607.html"],
            "林瑠奈":["HayashiRuna","https://nogiboard.blog.jp/archives/cat_169603.html"],
            # 5期生\
            "一ノ瀬美空":["IchinoseMiku","https://nogiboard.blog.jp/archives/cat_279894.html"],
            "小川彩":["OgawaAya","https://nogiboard.blog.jp/archives/cat_280365.html"],
            "川崎桜":["KawasakiSakura","https://nogiboard.blog.jp/archives/cat_290540.html"],
            "中西アルノ":["NakanishiAruno","https://nogiboard.blog.jp/archives/cat_280901.html"],
        }


# 関数定義
def getNogiUrl(t_memberName):

    r_memberUrl, r_dirName = mydict.get(t_memberName)  # type: ignore

    return r_memberUrl,r_dirName

