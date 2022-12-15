from aip import AipOcr


app_id = '17626750'
app_key = 'oFFfwGQlhqeUKT6TRspjsDyo'
secret_key = 'GDQF0fACbGo9wXGqQPkofsidPVnX95hA'
client = AipOcr(app_id, app_key, secret_key)


'''读取图片'''
def get_file_content(filepath):
    with open(filepath, 'rb')as fp:
        return fp.read()


def get_content(filepath):
    image = get_file_content(filepath)
    '''调用文字识别'''
    content = client.basicGeneral(image)

    # print(content)
    # 打码平台
    image_content = content['words_result'][0]['words']
    # print(image_content)
    return image_content
