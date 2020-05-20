from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse

# 创建Excel表格文件
import xlwt

from . import forms
from . import crawler

# Create your views here.

def index(request):
    """主页"""
    return render(request, 'ecommerce/index.html')


def jd(request):
    """京东"""
    return  render(request, 'ecommerce/jd.html')


def jdsearch(request):
    """京东商品搜索"""
    return render(request, 'ecommerce/jdsearch.html')


def jdcomment(request):
    """京东商品评论"""
    return render(request, 'ecommerce/jdcomment.html')


def jdsearchconfig(request):
    """京东商品搜索参数配置"""
    if request.method == 'POST':
        search_config_form = forms.SearchConfigForm(request.POST)
        message = '请检查填写的内容'
        if search_config_form.is_valid():
            keyword = search_config_form.cleaned_data.get('keyword')
            page = search_config_form.cleaned_data.get('page')

            # 已获取用户输入的参数，如何传递给爬虫
            request.session['jdsearch_keyword'] = keyword
            request.session['jdsearch_page'] = page

            return redirect('/ecommerce/jdsearchresult/')
        else:
            # 表单数据无效
            return render(request, 'ecommerce/jdsearchconfig.html', locals())

    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    search_config_form = forms.SearchConfigForm()
    return render(request, 'ecommerce/jdsearchconfig.html', locals())


def jdcommentconfig(request):
    """京东商品评论参数配置"""
    if request.method == 'POST':
        comment_config_form = forms.CommentConfigForm(request.POST)
        message = '请检查填写的内容'
        if comment_config_form.is_valid():
            site = comment_config_form.cleaned_data.get('site')
            page = comment_config_form.cleaned_data.get('page')

            # 将获取的参数传递给爬虫
            request.session['jdcomment_site'] = site
            request.session['jdcomment_page'] = page

            return redirect('/ecommerce/jdcommentresult/')
        else:
            # 表单数据无效
            return render(request, 'ecommerce/jdcommentconfig.html', locals())

    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    comment_config_form = forms.CommentConfigForm()
    return render(request, 'ecommerce/jdcommentconfig.html', locals())


def jdsearchexcel(jdsearch_data):
    """
    京东搜索生成excel表格文件
    :param jdsearch_data:
    :return:
    """
    # 新建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 新建sheet
    sheet = workbook.add_sheet('jdsearch_data')
    # 添加行列数据
    # 表头
    thead = ['搜索关键词', '商家店名', '商品名称', '评价人数', '价格', '商品详情页链接', '页码', '店铺链接', '商品评论链接',
             '封面图链接']
    keys = ['keyword', 'product_store_name', 'product_name', 'product_comment_number', 'product_price',
            'product_detail_url', 'page', 'product_store_url', 'product_comment_url', 'product_image_url']
    for i in range(0, len(jdsearch_data)):
        for j in range(0, len(thead)):
            if i == 0:
                sheet.write(i, j, thead[j])
            else:
                sheet.write(i, j, jdsearch_data[i - 1].get(keys[j]))
    # xlsx格式打不开
    workbook.save('ecommerce/data/jdsearch_data.xls')


def jdcommentexcel(jdcomment_data):
    """
    京东商品评论生成excel表格文件
    :param jdcomment_data:
    :return:
    """
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('jdcomment_data')
    thead = ['用户名', '评价星级', '评价内容', '评价时间', '点赞数', '评论数', '页面标题', '页面网址']
    keys = ['username', 'star', 'content', 'time', 'thumb', 'comment', 'title', 'site']
    for i in range(0, len(jdcomment_data)):
        for j in range(0, len(thead)):
            if i == 0:
                sheet.write(i, j, thead[j])
            else:
                sheet.write(i, j, jdcomment_data[i - 1].get(keys[j]))
    workbook.save('ecommerce/data/jdcomment_data.xls')


def jdsearchresult(request):
    """京东搜索采集预览"""
    # 通过session取得keyword, page
    keyword = request.session.get('jdsearch_keyword')
    page = request.session.get('jdsearch_page')

    # 调用爬虫，生成结果预览
    jdsearch_data = crawler.jdSearchCrawler(keyword, page)
    # 需要时间去获取数据

    # xls
    jdsearchexcel(jdsearch_data)
    # 测试xls文件是否生成
    try:
        with open('ecommerce/data/jdsearch_data.xls', 'rb') as xls:
            print('xls文件已生成')
    except FileNotFoundError:
        print('xls文件不存在')

    return render(request, 'ecommerce/jdsearchresult.html', locals())


def jdcommentresult(request):
    """京东商品评论采集预览"""
    # 通过session取得site, page
    site = request.session.get('jdcomment_site')
    page = request.session.get('jdcomment_page')

    # 调用爬虫，生成结果预览
    # 需要时间去获取数据
    jdcomment_data = crawler.jdCommentCrawler(site, page)

    # xls
    jdcommentexcel(jdcomment_data)
    # 测试xls文件是否生成
    try:
        with open('ecommerce/data/jdcomment_data.xls', 'rb') as xls:
            print('xls文件已生成')
    except FileNotFoundError:
        print('xls文件不存在')

    return render(request, 'ecommerce/jdcommentresult.html', locals())


def downloadfile(request):
    """
    京东搜索xls文件下载
    :param request:
    :return:
    """
    # try:
    #     with open('ecommerce/data/jdsearch_data.xls', 'rb') as file:
    #         response = FileResponse(file)
    # except FileNotFoundError:
    #     print('文件下载时打开文件失败')

    # ValueError: read of closed file
    # django会关闭文件
    file = open('ecommerce/data/jdsearch_data.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="jdsearch_data.xls"'
    return response


def jdcommentdownload(request):
    """
    京东商品评论xls文件下载
    :param request:
    :return:
    """
    file = open('ecommerce/data/jdcomment_data.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=jdcomment_data.xls'
    return response