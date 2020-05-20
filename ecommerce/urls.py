from django.urls import path

from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('index/', views.index),
    path('jd/', views.jd),
    path('jdsearch/', views.jdsearch),
    path('jdsearchconfig/', views.jdsearchconfig),
    path('jdsearchresult/',views.jdsearchresult),
    path('download/', views.downloadfile, name='download'),
    path('jdcomment/', views.jdcomment),
    path('jdcommentconfig/', views.jdcommentconfig),
    path('jdcommentresult/', views.jdcommentresult),
    path('jdcommentdownload/', views.jdcommentdownload, name='jdcommentdownload'),
]