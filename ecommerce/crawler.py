"""
网站爬虫程序，封装成函数，由视图函数调用。
"""

# import requests
# from lxml import etree
# from urllib.parse import quote
#
#
# def jdSearchCrawler(keyword='华为', pages='5'):
#     """
#     京东商品搜索爬虫
#     :param keyword:
#     :param pages:
#     :return:
#     """
#     # 对搜索关键字进行URL编码
#     quote_keyword = quote(keyword)
#     # 构造URL
#     # 页码奇数，偶数页内容在奇数页后，由JavaScript动态渲染
#     url = 'https://search.jd.com/Search?keyword=' + quote_keyword + '&enc=utf-8&wq=' + quote_keyword + '&page=' + str(1)
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
#     # 评价数需要javascript渲染
#     data = requests.get(url, headers=headers)
#     # 乱码问题
#     data.encoding = 'utf8'
#     html = etree.HTML(data.text)
#
#     # 0.5, ::after == $0
#     goods = html.xpath('//*[@id="J_goodsList"]/ul/li')
#
#     for good in goods:
#         # 搜索关键字
#         good_store_name = good.xpath('./div/div[7]/span/a/text()')
#         good_name = good.xpath('./div/div[4]/a/em/text()')
#         good_comment_number = good.xpath('./div/div[5]/strong/a/text()')
#         good_price = good.xpath('./div/div[3]/strong/i/text()')
#         good_detail_url = good.xpath('./div/div[4]/a/@href')
#         # 页码
#         good_store_url = good.xpath('./div/div[7]/span/a/@href')
#         good_comment_url = good.xpath('./div/div[5]/strong/a/@href')
#         good_image_url = good.xpath('./div/div[1]/a/img/@source-data-lazy-img')[0].strip()
#         good_image_url = 'https:' + good_image_url
#
#         print(good_store_name)
#         print(good_name)
#         print(good_comment_number)
#         print(good_price)
#         print(good_detail_url)
#         print(good_store_url)
#         print(good_comment_url)
#         print(good_image_url)
#         print()
#         print()

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 使用XPath解析
from lxml import etree
from urllib.parse import quote

options = webdriver.ChromeOptions()
# 不加载图片，只获取图片URL，动态加载，模拟执行JavaScript获取
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
# Chrome Headless模式，无界面模式
# todo: ubuntu需要安装Chrome、chromedriver
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

# 调试：不加载配置，性能优化
# browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)

jdsearch_data = []
jdcomment_data = []


def jdSearchGetProducts(keyword, page):
    """
    京东商品搜索爬虫解析商品列表
    :param keyword:
    :param page:
    :return:
    """
    # 使用XPath解析
    html = etree.HTML(browser.page_source, etree.HTMLParser())
    items = html.xpath('//*[@id="J_goodsList"]/ul/li')
    for item in items:
        # todo: 数据清洗，空值处理，URL优化，产品名字只有一半
        product = {
            # 搜索关键字
            'keyword': keyword,
            'product_store_name': item.xpath('./div/div[7]/span/a/text()')[0].strip() if item.xpath('./div/div[7]/span/a/text()') else '',
            'product_name': item.xpath('./div/div[4]/a/em/text()'),
            'product_comment_number': item.xpath('./div/div[5]/strong/a/text()'),
            'product_price': item.xpath('./div/div[3]/strong/i/text()'),
            'product_detail_url': item.xpath('./div/div[4]/a/@href'),
            # 页码
            'page': str(page),
            'product_store_url': item.xpath('./div/div[7]/span/a/@href'),
            'product_comment_url': item.xpath('./div/div[5]/strong/a/@href'),
            'product_image_url': item.xpath('./div/div[1]/a/img/@src')
        }
        print(product)

        # todo: save to somewhere
        # 本地采集[]暂存
        # 分布式采集数据库保存
        jdsearch_data.append(product)


def jdCommentGetComments(site, page):
    """
    京东商品评论爬虫解析评论列表
    :param site:
    :param page:
    :return:
    """
    # 使用XPath解析
    html = etree.HTML(browser.page_source, etree.HTMLParser())
    items = html.xpath('//*[@id="comment-0"]/div[position()<11]')
    title = html.xpath('/html/body/div[6]/div/div[2]/div[1]/text()')[0].strip()
    for item in items:
        star = item.xpath('./div[2]/div[1]/@class')[0].strip()
        star = int(star[-1])
        star = star * '★'
        comment = {
            'username': item.xpath('./div[1]/div[1]/text()')[1].strip(),
            'star': star,
            'content': item.xpath('./div[2]/p/text()')[0],
            'time': item.xpath('./div[2]/div[5]/div[1]/span[51]/text()'),
            'thumb': item.xpath('./div[2]/div[5]/div[2]/a[2]/text()'),
            'comment': item.xpath('./div[2]/div[5]/div[2]/a[3]/text()'),
            'title': title,
            # 页面网址
            'site': site + '#comment'
        }
        print(comment)

        # []暂存
        jdcomment_data.append(comment)


def document_body_scroll(scroll_height):
    """
    模拟运行JavaScript，每次将进度条下拉500，显示全部商品信息，包括图片
    :return:
    """
    height = 0
    times = scroll_height // 500 + 1
    for i in range(0, times):
        height += 500
        browser.execute_script('window.scrollTo(0, {})'.format(height))
        sleep(1)


def jdSearchIndexPage(keyword, page):
    """
    京东商品搜索爬虫抓取索引页
    :param keyword:
    :param page:
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        # 对搜索关键字进行URL编码
        quote_keyword = quote(keyword)
        url = 'https://search.jd.com/Search?keyword=' + quote_keyword + '&enc=utf-8&wq=' + quote_keyword
        browser.get(url)
        # todo: 设置合理的等待时间，先抓取到信息，再提高效率
        # sleep(WAITFORIMAGE)
        # print('before height: ', browser.execute_script('return document.body.scrollHeight'))
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(3)
        # print('after height: ', browser.execute_script('return document.body.scrollHeight'))
        # sleep(WAITFORIMAGE)
        # 直接用跳转的方式来爬取页面，而不是直接点击下一页
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_bottomPage"]/span[2]/input')))
            submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_bottomPage"]/span[2]/a')))
            input.clear()
            input.send_keys(page)
            submit.click()
            # sleep(WAITFORIMAGE)
            # # 模拟运行JavaScript，将进度条下拉到最底部，显示全部商品信息
            # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # sleep(WAITFORIMAGE)
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(3)


        scroll_height = int(browser.execute_script('return document.body.scrollHeight'))
        # 模拟运行JavaScript，将进度条下拉到最底部，显示全部商品信息
        document_body_scroll(scroll_height)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page)))
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_goodsList"]/ul/li')))
        jdSearchGetProducts(keyword, page)

    except TimeoutException:
        jdSearchIndexPage(keyword, page)


def jdCommentIndexPage(site, page):
    """
    京东商品评论爬虫抓取索引页
    :param site:
    :param page:
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        browser.get(site)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(3)
        # 直接用跳转的方式来爬取页面，而不是直接点击下一页
        if page > 1:
            xpath = '//*[@id="comment-0"]/div[13]/div/div/a[' + str(page) + ']'
            next = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            next.click()
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(3)

        scroll_height = int(browser.execute_script('return document.body.scrollHeight'))
        # 模拟运行JavaScript，将进度条下拉到最底部，显示全部商品信息
        document_body_scroll(scroll_height)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#comment-0 > div.com-table-footer > div > div > a.ui-page-curr'), str(page)))
        # 前10个div为评论内容
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="comment-0"]/div[position()<11]')))
        jdCommentGetComments(site, page)

    except TimeoutException:
        jdCommentIndexPage(site, page)


def jdSearchCrawler(keyword='华为', page=3):
    """
    京东商品搜索爬虫主函数
    :param keyword:
    :param page:
    :return:
    """
    for i in range(1, page + 1):
        jdSearchIndexPage(keyword, i)

    # browser.close()

    return jdsearch_data


def jdCommentCrawler(site='https://item.jd.com/100008384344.html', page=3):
    """
    京东商品评论爬虫主函数
    :param site:
    :param page:
    :return:
    """
    for i in range(1, page + 1):
        jdCommentIndexPage(site, i)

    # 连续启动2不同爬虫，浏览器关闭未启动
    # todo: 关闭策略，或者自动释放
    # browser.close()

    return jdcomment_data


if __name__ == "__main__":
    # jdSearchCrawler('华为', 2)
    jdCommentCrawler('https://item.jd.com/100008384344.html', 2)