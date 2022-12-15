import requests
import getpass
from config import *
import urllib

url = 'http://www.taobao.com'
login_url = 'https://login.taobao.com/member/login.jhtml?'
proxy_url = 'http://203.119.175.212:443'

headrs = {
    'euser-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
    'origin': 'https://login.taobao.com',
    'referer': 'https://login.taobao.com/member/login.jhtml?',
    'content-type': 'application/x-www-form-urlencoded'
}



