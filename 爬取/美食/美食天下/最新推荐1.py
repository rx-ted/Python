import urllib.request
from bs4 import BeautifulSoup
import re

url_part = 'https://home.meishichina.com/recipe-494446.html'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36"
}
url = urllib.request.Request(url=url_part, headers=headers)

proxies = {"http": "183.230.179.164:8060"}
hander = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(hander)
resp = opener.open(url)
html = resp.read().decode('utf-8')

soup = BeautifulSoup(html, 'lxml')

# 爬取标题
content_title = soup.select('body > div.wrap > div > div.space_left > div.space_box_home > div #recipe_title')
for n in content_title:
    title = n.get('value')

# 爬取图片
content_img = soup.select('#recipe_De_imgBox > a > img')
for n in content_img:
    alt = n.get('alt')
    img_src = n.get('src')

# 爬取主料
content_main_menu = soup.select(
    'body > div.wrap > div > div.space_left > div.space_box_home > div > fieldset:nth-child(6)')
legend = re.findall('<legend>(.*)</legend>', str(content_main_menu[0]))
material = re.findall('<b>(.*)</b>', str(content_main_menu[0]))
size = re.findall('<span class="category_s2">(.*)</span>', str(content_main_menu[0]))


# 爬取辅料
content_accessories = soup.select(
    'body > div.wrap > div > div.space_left > div.space_box_home > div > fieldset:nth-child(7) > div')
material_a = re.findall('<b>(.*)</b>', str(content_accessories[0]))
size_a = re.findall('<span class="category_s2">(.*)</span>', str(content_accessories[0]))

# 爬取难点
content_aporia = soup.select(
    'body > div.wrap > div > div.space_left > div.space_box_home > div > div.recipeCategory_sub_R.mt30.clear')
# 前面补充"口味、工艺、耗时、难度"，四个元素固定
aporias = re.findall('target="_blank" title=".*">(.*)</a>', str(content_aporia[0]))

# 做法步骤
step_imgs = []
step_titles = []
content_step = soup.select(
    'body > div.wrap > div > div.space_left > div.space_box_home > div > div.recipeStep > ul > li > div.recipeStep_img > img')
for n in content_step:
    step_title = n.get('alt')
    step_img = n.get('src')
    step_titles.append(step_title)
    step_imgs.append(step_img)

step_re = '<div class="recipeStep_word"><div class="recipeStep_num">.*</div>(.*)</div>'
content_step_name = soup.select('body > div.wrap > div > div.space_left > div.space_box_home > div > div.recipeStep > ul > li')
step_name = re.findall(step_re, str(content_step_name))


content_tool = soup.select('body > div.wrap > div > div.space_left > div.space_box_home > div > div:nth-child(12)')
tool_re = '<div[^>]*>([\s\S]*?)<\/div>'
tool = re.findall(tool_re, str(content_tool[0]))

print(title,alt,img_src)
print(legend,material,size)
print(material_a,size_a)
print(aporias)
print(step_titles,step_imgs)
print(step_name)
print(tool[0])
