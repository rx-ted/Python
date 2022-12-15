import requests
url = "https://www.ximalaya.com/revision/play/album?albumId=19349717&pageNum=1&sort=1&pageSize=30"

# 反爬
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400",
    # 变化的
    "xm-sign": "b39c405c0960fe27476dd3068c79b335(6)1565159881313(13)1565159881783"
    # 上面的  链接网址https://www.ximalaya.com/        寻找getCurenntUser  然后xm-sign后面复制到上面
        }
# text  提取字符串数据""  content得到二进制数据(音频 视频 图片 ……)  010101
# json 得到的字典
response = requests.get(url, headers=header).json()

print("最初的数据",response)

audio_data = response["data"]["tracksAudioPlay"]
print("音频数据列表：",audio_data)

print("\n\n")


# 依次获取每个元素。
for audio in audio_data:
    print("音频信息：",audio)


    music_url = (audio["str"])
    print("音频网址：", music_url)
    music_content = requests.get(music_url).content

    # mp3
    music_name = audio["trackName"]+".m4a"
    print("音频名称：", music_name)

    print("\n")

    with open(str(music_name), "wb") as f:
        f.write(music_content)









# https://www.ximalaya.com/

# https://imagev2.xmcdn.com/group49/M09/16/CF/wKgKl1vtNNfCAyFWAAITMtQComg191.jpg!strip=1&quality=7&magick=jpg&op_type=5&upload_type=album&name=mobile_large&device_type=ios

'''
tracksAudioPlay: [{index: 19, trackId: 146502056, trackName: "爱要怎么说出口-赵传(李宗盛曾为TA下跪，终成经典）",…},…]
0: {index: 19, trackId: 146502056, trackName: "爱要怎么说出口-赵传(李宗盛曾为TA下跪，终成经典）",…}
1: {index: 18, trackId: 145661860, trackName: "乱世巨星-陈小春（热血经典，内附发音）",…}
2: {index: 17, trackId: 144594437, trackName: "你玩够了没有 - 零点乐队（瞬间唤起青春回忆，百听不厌）",…}
3: {index: 16, trackId: 143509511, trackName: "野花-田震（华语歌坛20世纪百大名曲之一）",…}
4: {index: 15, trackId: 142413230, trackName: "小鸟-鲍家街43号 （汪峰“鲍家街”时期的经典之作，穿透心灵的呐喊）",…}
5: {index: 14, trackId: 141547067, trackName: "他一定很爱你-阿杜（一首有点心酸，却让张学友爱不释手的歌）",…}
6: {index: 13, trackId: 140694661, trackName: "那些花儿-朴树（一首越长大越能听懂的歌，情到深处 哀而不伤）",…}
7: {index: 12, trackId: 140130361, trackName: "我愿意- 王菲 （天籁之音，曾让多少人勇敢面对爱情）",…}
8: {index: 11, trackId: 139611184, trackName: "不必在乎我是谁-林忆莲（尘封已久的老歌，曾让多少人流泪）",…}
9: {index: 10, trackId: 138876329, trackName: "白衣飘飘的年代-叶蓓", trackUrl: "/yinyue/19349717/138876329",…}
10: {index: 9, trackId: 138036515, trackName: "故乡-许巍（远离他乡的人都能懂得这种伤痛）",…}
11: {index: 8, trackId: 137785224, trackName: "棋子-王菲", trackUrl: "/yinyue/19349717/137785224",…}
12: {index: 7, trackId: 137060397, trackName: "恋恋风尘-老狼", trackUrl: "/yinyue/19349717/137060397",…}
13: {index: 6, trackId: 137060276, trackName: "那一年-许巍", trackUrl: "/yinyue/19349717/137060276",…}
14: {index: 5, trackId: 137019647, trackName: "同桌的你-老狼", trackUrl: "/yinyue/19349717/137019647",…}
15: {index: 4, trackId: 137018858, trackName: "执着-田震", trackUrl: "/yinyue/19349717/137018858",…}
16: {index: 3, trackId: 137018469, trackName: "天黑-阿杜", trackUrl: "/yinyue/19349717/137018469",…}
17: {index: 2, trackId: 136852907, trackName: "灰姑娘-郑钧（灰姑娘的原型竟是TA？）",…}
18: {index: 1, trackId: 136849355, trackName: "白桦林-朴树", trackUrl: "/yinyue/19349717/136849355",…}
uid: 0
msg: "声音播放数据"
ret: 200

'''