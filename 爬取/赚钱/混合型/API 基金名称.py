import requests
import tushare as ts
import os

token_key = 'bad93028dd75b354a77c80e2782786111516f11328d139da403e1654'

class ts_jj:
    # 创建文件夹
    def path(self):
        self.path = 'data/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)


    # get the data of the jjmc 
    def jjmc(self):
        # version = ts.__version__
        # print(version)
        pro =  ts.pro_api(token_key)      
        #查询当前所有正常上市交易的股票列表
        data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        #print(data)
        with open(self.path+'jjmc.txt',mode='w',encoding='utf-8')as fp:
            fp.write(str(data))


    # 读取交易日历
    def tradecal(self):        
        pro = ts.pro_api(token_key)
        # 交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源,IB 银行间,XHKG 港交所
        cal =  pro.query('trade_cal', start_date='20191201', end_date='20191231')
        print(cal)

    # 读取公司信息
    def information_company(self):
        pro = ts.pro_api(token_key)
        #或者
        #pro = ts.pro_api('your token')
        df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
        print(df)

    

def main():
    t = ts_jj()
    #t.path()
    #t.jjmc()
#    t.tradecal()
    t.information_company()

if __name__ == "__main__":
    main()



'''
        ts_code  symbol  name area industry list_date
0     000001.SZ  000001  平安银行   深圳       银行  19910403
1     000002.SZ  000002   万科A   深圳     全国地产  19910129
2     000004.SZ  000004  国农科技   深圳     生物制药  19910114
3     000005.SZ  000005  世纪星源   深圳     环境保护  19901210
4     000006.SZ  000006  深振业A   深圳     区域地产  19920427
...         ...     ...   ...  ...      ...       ...
3749  688368.SH  688368  晶丰明源   上海      半导体  20191014
3750  688369.SH  688369  致远互联   北京     软件服务  20191031
3751  688388.SH  688388  嘉元科技   广东      元器件  20190722
3752  688389.SH  688389  普门科技   深圳     医疗保健  20191105
3753  688399.SH  688399  硕世生物   江苏     医疗保健  20191205
'''