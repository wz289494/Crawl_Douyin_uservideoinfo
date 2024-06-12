from selenium import webdriver
import time
import json


def browser_initial():
    """"
    进行浏览器初始化
    """
    browser = webdriver.Chrome()
    log_url = 'https://www.douyin.com/user/MS4wLjABAAAA7-glEAE86hgJyjouGifmiAfBvLa7sM_Rh6TTc6QK23ZvS0gcyWHtUfPEECNdvabm'
    return log_url, browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(40)  # 进行扫码
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)

    with open('config_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])