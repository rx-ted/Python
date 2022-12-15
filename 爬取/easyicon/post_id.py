import requests
from bs4 import BeautifulSoup

main_url=  "https://www.easyicon.net/" 
parse_url='https://www.easyicon.net/1273827-google_plus_icon.html'
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
def get_img(url):
    t = requests.get(url,headers=headers)
    soup = BeautifulSoup(t.text,'html.parser')

    img_url = (soup.find_all('div', class_='icon_img_one')[0])
    for i in img_url:
        url = main_url+i.find('img')['src']
        alt = i.find('img')['alt']
        name = alt.replace(' ','_')+'.png'

    
    return url,name

def downloads( url,name ):
    path = 'e:/workers/ico'
    # url,name =get_img(parse_url) 
    content = requests.get(url).content
    with open(path+'/'+name,'wb')as f:
        f.write(content)
    print('{0},完成下载保存'.format(name))


def sousuo_url(): 
    name = input("请输入你要搜索的名字:\n>")
    #name = 'hello'
    murl = 'https://www.easyicon.net'
    url ='https://www.easyicon.net/iconsearch/{0}/{1}/?m=yes&f=_all&s=addtime_DESC'.format(name,1)
    '//*[@id="result_right_layout"]/div[3]/div[1]'

    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    search_icon_detail = soup.findAll('div',class_='pd_img')
    hrefs = []
    for i in search_icon_detail:
        href = murl+i.find('a')['href']
        url,name = get_img(href)
        downloads( url,name)

    
sousuo_url()