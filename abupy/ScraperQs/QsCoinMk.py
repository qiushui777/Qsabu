#coding=utf-8

"""
    爬取CoinMarket网站加密货币价格的爬虫
"""

import datetime
import calendar
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


class QsCoinMkScraper(object):
    def __init__(self):
        self.targetcoin = "bitcoin"
        self.start = "20130428"
        self.end = self.getdate()
        self.url = "https://coinmarketcap.com/currencies/%s/historical-data/?start=%s&end=%s"

    def getdate(self):
        """获得当日日期"""
        today = datetime.date.today()
        return today.strftime('%Y%m%d')

    def format_date(self, datestring):
        """
        输入'Apr 28, 2013' 转换为 2013-04-28
        """
        month_day = datestring.split(',')[0]
        year = datestring.split(',')[1].strip()
        month = str(list(calendar.month_abbr).index(month_day.split(' ')[0]))
        if(len(month) == 1):
            month = '0' + month
        day = month_day.split(' ')[1]
        formated_date = "%s-%s-%s" % (year,month,day)
        print(formated_date)

    def get_kline_data(self, cointype="bitcoin", startdate=None, enddate=None):
        """日K线接口，CoinMartket暂时无法获取更短间隔的数据"""
        self.targetcoin = cointype
        if startdate is not None:
            self.start = startdate
        if enddate is not None:
            self.end = enddate
        self.url = self.url % (self.targetcoin, self.start, self.end)
        self.parse_page(self.url)
        
    def parse_page(self,url):
        """从页面中提取出想要的数据，保存为一个DataFrame"""
        df = pd.DataFrame(columns = ['date','open','high','low','close','volume'])
        line1 = np.array([1,2,3,4,5,6])
        df.loc['new'] = line1
        
        html = requests.get(url)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_tr = Soup.find_all('tr', class_ = 'text-right')

        # 每个tr中包含有含有具体数据的td标签
        for tr in all_tr:
            tds = tr.find_all('td')
            # 每个td标签依次对应一个数据
            td_date = tds[0].string
            td_open = tds[1].string
            td_high = tds[2].string
            td_low = tds[3].string
            td_close = tds[4].string
            td_volume = tds[5].string

