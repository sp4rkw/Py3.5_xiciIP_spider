__author__ = "GETF"
# -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import pymysql

'''自己BP抓取即可'''
header = {

}


''''' 
获取所有代理IP地址,并调用函数进行可用性测试，再调用函数将可用的写入数据库
'''
def getProxyIp(header):
    for x in range(1,2):#这里自行根据需要改变
        url = "http://www.xicidaili.com/nn/{0}".format(x)
        html = requests.get(url=url,headers=header).text
        soup = BeautifulSoup(html,"html.parser")
        ips = soup.findAll('tr')
        num = 0
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]#ip
            protocal = tds[5].contents[0]#协议
            place = tds[3].find('a').contents[0]#服务器地址
            value = validateIp(ip_temp,protocal)
            if(value == True):
                WriteMysql(ip_temp,place,protocal)
                num = num +1
            elif(value == False):
                pass
            else:
                print("IP："+ip_temp+'出现异常问题')
    return num

''''' 
将可用代理ip写入数据库
'''
def WriteMysql(ip,place,protocal):
    db = pymysql.connect(db='ip', host='localhost', port=3306, user='root', passwd='xxxxx',
                              charset='utf8')
    cursor = db.cursor()
    sql = "insert into `xiciip` VALUE('%s','%s','%s')"%(ip,protocal,place)
    cursor.execute(sql)
    db.commit()



''''' 
验证获得的代理IP地址是否可用 
'''
def validateIp(ip,protocol):
    url = "http://ip.chinaz.com/getip.aspx"#站长查ip
    try:
        proxy_host = protocol+"://"+ip
        html = requests.get(url,proxies = proxy_host,timeout=3)
        if(html.status_code == 200):
            return True
        else:
            return False
    except:
        return 'error'





if __name__ == '__main__':
    num = getProxyIp(header)
    print("本次成功入库有效代理IP"+str(num)+"条")