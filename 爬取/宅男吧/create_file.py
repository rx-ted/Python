import os 


if __name__ == "__main__":
    filename = '测试1.txt'
    path = 'd:\data'
    if not os.path.exists(path):
        os.makedirs(path)
    text = 'cd {} && type nul> {}'.format(path,filename)
    os.system(str(text))
    