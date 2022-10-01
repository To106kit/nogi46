# %%
# 初期化
r_memberUrl = []
r_dirName = []

mydict= {
            # 4期生\
            "遠藤さくら":["EndoSakura","https://nogiboard.blog.jp/archives/cat_169593.html"],
            "賀喜遥香":["KakiHaruka","https://nogiboard.blog.jp/archives/cat_169510.html"],
            "掛橋沙耶香":["KakehashiSayaka","https://nogiboard.blog.jp/archives/cat_169595.html"],
            "金川紗耶":["KanagawaSaya","https://nogiboard.blog.jp/archives/cat_169594.html"],
            "佐藤璃果":["SatoRika","https://nogiboard.blog.jp/archives/cat_169603.html"],
            "田村真佑":["TamuraMayu","https://nogiboard.blog.jp/archives/cat_169599.html"],
            "筒井あやめ":["TsutsuiAyame","https://nogiboard.blog.jp/archives/cat_169600.html"],
            "弓木奈於":["YumikiNao","https://nogiboard.blog.jp/archives/cat_169607.html"],
            "林瑠奈":["HayashiRuna","https://nogiboard.blog.jp/archives/cat_169605.html"],
            # 5期生\
            "一ノ瀬美空":["IchinoseMiku","https://nogiboard.blog.jp/archives/cat_279894.html"],
            "小川彩":["OgawaAya","https://nogiboard.blog.jp/archives/cat_280365.html"],
            "川崎桜":["KawasakiSakura","https://nogiboard.blog.jp/archives/cat_290540.html"],
            "中西アルノ":["NakanishiAruno","https://nogiboard.blog.jp/archives/cat_280901.html"],
        }


# 関数定義
def getNogiUrl(t_memberName):
    for member_idx in t_memberName:
        r_memberUrl.append(mydict.get(member_idx)[0])  # type: ignore
        r_dirName.append(mydict.get(member_idx)[1])  # type: ignore

    return r_memberUrl,r_dirName

