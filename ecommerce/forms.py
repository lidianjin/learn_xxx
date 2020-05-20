from django import forms

class SearchConfigForm(forms.Form):
    """京东商品搜索参数配置表单"""
    keyword = forms.CharField(label='搜索关键词', max_length=128, widget=forms.TextInput(attrs={'placeholder': '如“耐克”', 'autofocus': ''}))
    page = forms.IntegerField(label='页数', widget=forms.NumberInput(attrs={'placeholder': '请输入数字'}))


class CommentConfigForm(forms.Form):
    """京东商品评论参数配置表单"""
    site = forms.URLField(label='输入网址', max_length=256, widget=forms.URLInput(attrs={'placeholder': '如https://item.jd.com/100008384344.html', 'autofocus': ''}))
    page = forms.IntegerField(label='翻页次数', widget=forms.NumberInput(attrs={'placeholder': '请输入数字'}))