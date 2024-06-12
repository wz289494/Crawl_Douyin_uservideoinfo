from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from scrapy.http import HtmlResponse
import time

class DouyinuserDownloaderMiddleware:
    def __init__(self):
        # 配置ChromeOptions以启用无头模式
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # 添加无头参数
        # 创建一个driver对象
        self.driver = webdriver.Chrome(options=chrome_options)

    def process_request(self,request,spider):
        # 访问建立链接
        self.driver.get(request.url)
        # 用于手动过验证码
        time.sleep(5)
        # 刷新页面
        self.log_cookie()
        # 登待初始页面响应
        time.sleep(2)
        # 等待元素出现
        # 等待页面上的特定元素出现
        try:
            # 刷新到底
            self.reflash()
            # 获取页面源码
            page_source = self.driver.page_source
            return HtmlResponse(url=request.url, body=page_source, request=request, encoding='utf-8')
        except Exception as e:
            spider.logger.error(f"Error")
            return HtmlResponse(url=request.url, status=500, request=request)

    def log_cookie(self):
        # 读取cookie登录文件
        with open(r'..\config_cookies.txt', 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())

        # 往browser里添加cookies
        for cookie in listCookies:
            cookie_dict = {
                'domain': '.douyin.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": cookie.get('expiry'),
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }

            self.driver.add_cookie(cookie_dict)

        # 刷新网页,cookies才成功
        self.driver.refresh()

    def reflash(self):
        # 获取当前页面的高度
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        # 模拟下拉操作，直到滑动到底部
        # for i in range(Crawl_Douyin_uservideoinfo):
        while True:
            # 模拟下拉操作
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 等待页面加载
            time.sleep(3)

            # 获取当前页面的高度
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            # 判断是否已经到达页面底部
            if new_height == last_height:
                break

            # 继续下拉操作
            last_height = new_height





