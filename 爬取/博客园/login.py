import requests

login_url = 'https://account.cnblogs.com/signin?returnUrl='
# 客户端
session = requests.session()

login_page = session.get(login_url)

headers = {
    'authority': 'www.cnblogs.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'content-type': 'text/html; charset=utf-8',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'accept-encoding': 'br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_ga=GA1.2.613754223.1572763636; _gid=GA1.2.518770267.1572763636; __gads=ID=9077747d79ea979a:T=1572763636:S=ALNI_MapllR83gQ7pNnl446qjAqkf3jbBA; .Cnblogs.AspNetCore.Cookies=CfDJ8DeHXSeUWr9KtnvAGu7_dX-qP6g48jMxDfMArPv7L0NHLyaIDXnCtxyZ-6v52RURKYMD3-aIJxyjVtMUqghyvz8g-KFxL8z2J6p2A22eromOi0xlaxEZgUC9NdPM9PFaU7bbexSNhq6Y-KlKps9sgr3_leTi_7rp7Om4CLu1tRM9g02v2SrmscIW8bZpKq2NqT4tdJYwHre1p_wS_PwERuANjD_So_QLSTo8RUuRBr55yTbkajVt6oIg2yEUBT-YWtDq2syeH7WAdYPHpLfTAOrTUXC0ouRSOawOEs9haHWjpC9aghvjbiwtSafngG5xCVtUa6jHoyIerMt9LwLayp_IhA0e80ma30oPrPT3DbzvNvCIZzHJ_l3HYpOizWNmJrpe0LWImabO4sOJfvi_Vf1cHQkO-cjezW5XV9ISmFIcAXqNaSaJSTcoKTkIklavcMR25VCR6dGxqC1LviU48lE3CaCnuBrkfB8s6MLwl5uBiv3l2FK1odNUaMTMMdY8XccDBLeebZ4nQUeLe8-DTVsHo6yNTsiE-fUt5jjLNC1z; .CNBlogsCookie=AD5B0BB0580AF0D9C59CAAD666F60CA0C68AE594FA66C714E0FE0AB9507C57AF19E57E0AB0E2119BED7C15C9E3C18C6808B303C50B043053C13B54A795A41665C4FA0D5A889F4C0E0E761969B65171E074324A7D',
    'referer': 'https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F',
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

session.headers.update(headers)

data = {
    "input1": "rx-ted",
    "input2": "G8023@20sui",
    "remember": False
}

res = session.post(url=login_url, headers=headers, data=data)

index_url = 'https://home.cnblogs.com/'
my_url = 'https://home.cnblogs.com/u/rx-ted/'
index_page = session.get(url=my_url)

print(index_page.text)
