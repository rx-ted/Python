import requests
import base64  # 编码算法 伪加密
import csv

# -------------------------------------------------------
# 获取access_token示例代码
root = 'https://aip.baidubce.com/oauth/2.0/token'
tokendata = {
    'grant_type': 'client_credentials',
    'client_id': 'z4NK4g0a8ndujrlKwONQzBqd',
    'client_secret': 'gbgVPUimKGB4DDfGVGnpVARhg70bwycN'
}
response = requests.post(root, data=tokendata)
access_token = response.json()['access_token']

# -------------------------------------------------------
# 对图片进行颜值获取
url = f'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token={access_token}_'
headers = {
    'Content-Type': 'application/json'
}

data = {
    'image': '',
    'image_type	': 'BASE64',
    'face_field': 'beauty'
}
ll = []
with open('../files/wzly.csv', encoding='utf-8')as file:
    reader = csv.DictReader(file)
    for r in reader:
        fname = f'../images/{r["username"]}.png'
        try:
            with open(fname, 'rb')as f:
                data['image'] = base64.b64encode(f.read())  # 将图片通过base64
                response = requests.post(url, headers=headers, data=data)
                beauty = response.json()['result']['face_list'][0]['beauty']
                print(r["username"], beauty)
                ll.append([r["username"], beauty])
        except:
            pass
sorted(ll, lambda x: x[1])
with open('../files/yzly.csv', 'w', encoding='utf-8', newline='')as f:
    write = csv.writer(f)
    write.writerow(['username', 'beauty'])
    write.writerow(112)
