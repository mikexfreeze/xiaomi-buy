from selenium import webdriver
import datetime
import time

#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()

def login(url):
    '''
    登陆函数

    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)

    driver.implicitly_wait(10)
    time.sleep(2)

    #找到并点击天猫的登陆按钮
    driver.find_element_by_link_text("登录").click()

    print("请在30秒内完成登录")
    #用户扫码登陆
    time.sleep(30)

def buy(buy_time):
    '''
    购买函数

    buy_time:购买时间
    mall:商城类别

    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    #"加入购物车"的css_selector
    btn_buy='#J_buyBtnBox .J_proBuyBtn'
    # "立即下单"的css_selector
    # btn_order='#submitOrder_1 > div.wrapper > a'

    while True:
        #现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
            print("时间到，抢购开始")
            try:
                #找到“立即购买”，点击
                btn_buy_object = driver.find_element_by_css_selector(btn_buy)
                if btn_buy_object:
                    print("购买按钮定位：",btn_buy_object)
                    btn_buy_object.click()
                    break
                time.sleep(0.1)
            except:
                time.sleep(0.3)

if __name__ == "__main__":
    url=input("请输入小米商城商品链接:")
    bt=input("请输入开售时间【2019-02-15（空格）12:55:50】")
    login(url)
    buy(bt)