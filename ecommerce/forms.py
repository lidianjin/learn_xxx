from django import forms

class SearchConfigForm(forms.Form):
    """京东商品搜索参数配置表单"""
    keyword = forms.CharField(label='搜索关键词', max_length=128, widget=forms.TextInput(attrs={'placeholder': '如“耐克”', 'autofocus': ''}))
    page = forms.IntegerField(label='页数', widget=forms.NumberInput(attrs={'placeholder': '请输入数字'}))