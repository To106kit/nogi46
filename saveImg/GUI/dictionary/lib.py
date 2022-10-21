# %%
# 初期化
r_memberUrl = "default"
r_dirName = "default"

mydict= {
            # 4期生\
            "遠藤さくら":["EndoSakura","https://nogiboard.blogstation.jp/archives/cat_169593.html"],
            "賀喜遥香":["KakiHaruka","https://nogiboard.blogstation.jp/archives/cat_169510.html"],
            "掛橋沙耶香":["KakehashiSayaka","https://nogiboard.blogstation.jp/archives/cat_169595.html"],
            "金川紗耶":["KanagawaSaya","https://nogiboard.blogstation.jp/archives/cat_169594.html"],
            "佐藤璃果":["SatoRika","https://nogiboard.blogstation.jp/archives/cat_169603.html"],
            "田村真佑":["TamuraMayu","https://nogiboard.blogstation.jp/archives/cat_169599.html"],
            "筒井あやめ":["TsutsuiAyame","https://nogiboard.blogstation.jp/archives/cat_169600.html"],
            "弓木奈於":["YumikiNao","https://nogiboard.blogstation.jp/archives/cat_169607.html"],
            "林瑠奈":["HayashiRuna","https://nogiboard.blogstation.jp/archives/cat_169605.html"],
            # 5期生\
            "一ノ瀬美空":["IchinoseMiku","https://nogiboard.blogstation.jp/archives/cat_279894.html"],
            "小川彩":["OgawaAya","https://nogiboard.blogstation.jp/archives/cat_280365.html"],
            "川崎桜":["KawasakiSakura","https://nogiboard.blogstation.jp/archives/cat_290540.html"],
            "中西アルノ":["NakanishiAruno","https://nogiboard.blogstation.jp/archives/cat_280901.html"],
        }


# 関数定義
def getNogiUrl(t_memberName):

    r_memberUrl, r_dirName = mydict.get(t_memberName)  # type: ignore

    return r_memberUrl,r_dirName

