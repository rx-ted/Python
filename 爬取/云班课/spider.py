import requests


#url = "https://office-cn-hangzhou.imm.aliyuncs.com/office/w/1181156421819355_previewdoc_f2851c1ca9445e0dafed08b380e3d677665581ac9606d0ceda1f589e3174822d?hidecmb=1&simple=1&_w_tokentype=1"
url='https://office-cn-hangzhou.imm.aliyuncs.com/api/events/collect'
'''
https://viewer.mosoteach.cn/index.php/viewer/refresh_token?token=2dd36b9b9e3d156badd99fa24b5314b9&app_id=MTWEB&app_version=5.1.5
"https://office-cn-hangzhou.imm.aliyuncs.com/office/w/1181156421819355_previewdoc_f2851c1ca9445e0dafed08b380e3d677665581ac9606d0ceda1f589e3174822d?hidecmb=1&simple=1&_w_tokentype=1";

'''


data={
    'action': "metric",
    'category': "pc_wps",
    'channel': "web",
    #"refresh_token":"02f52dfd1b3f4ba6987eaf0a84e306b8",
    #"token": "748fa2efee0d40e690e59ce56053fae1",
    "download": "31",
    "download_start": "180",
    "filesize": "34268",
    "host": "office-cn-hangzhou.imm.aliyuncs.com",
    "html_time": "29",
    "init_core": "213",
    "js_loaded": "660",
    "network_total": "657",
    "open_file": "58",
    "parent_time":"0",
    "parse_file_data": "756",
    "render": "1682",
    "total": "3340",
    "websocket_open": "388",
    "websocket_start": "751",
    "device": "windows",
    "project": "wps",


}


res = requests.post(url=url,data=data)

if res.status_code==200:
    text = res.text
    print(text)
else:
    print(res.status_code)
    print('错误')
    print(res.text)