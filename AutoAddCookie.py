from selenium import webdriver


#手工添加cookie
def add_cookie_str(cookie_str):
    for item in cookie_str.split(';'):  # cookie字符串转list
        cookie = dict()
        itemname = item.split('=')[0]
        itemvalue = item.split('=')[1]
        cookie.update({
            'name': itemname.strip(' '),  #去除首尾空格（复制浏览器的会在最开头有空格）
            'value': itemvalue.strip(' '),
            "domain": "",
            "expires": "",
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'secure': False,
        })
        driver.add_cookie(cookie)
    return 1

def go(driver,url,cookie):
    #driver.implicitly_wait(10)
    #目标网址
    driver.get(url)
    driver.delete_all_cookies()
    #手工添加cookie
    add_cookie_str(cookie)

    #write something here ...

#调试webUI自动化专用
if __name__ =='__main__':
    driver = webdriver.Chrome()
    go(driver,url,cookie)