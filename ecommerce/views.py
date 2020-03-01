from django.shortcuts import render
from django.shortcuts import redirect

from . import forms

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


def jdsearchconfig(request):
    """京东商品搜索参数配置"""
    if request.method == 'POST':
        search_config_form = forms.SearchConfigForm(request.POST)
        message = '请检查填写的内容'
        if search_config_form.is_valid():
            keyword = search_config_form.cleaned_data.get('keyword')
            page = search_config_form.cleaned_data.get('page')

            # 已获取用户输入的参数，如何传递给爬虫

            return render(request, 'ecommerce/jdsearchresult.html', locals())
        else:
            # 表单数据无效
            return render(request, 'ecommerce/jdsearchconfig.html', locals())

    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    search_config_form = forms.SearchConfigForm()
    return render(request, 'ecommerce/jdsearchconfig.html', locals())


def jdsearchresult(request):
    """京东搜索采集预览"""
    return render(request, 'ecommerce/jdsearchresult.html')