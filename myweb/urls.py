from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$',views.index,name='index' ),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),

    url(r'^check_email/$', views.check_email, name='check_email'),
    url(r'^check_name/$', views.check_name, name='check_name'),
    url(r'^get_code/$', views.get_code, name='get_code'),

    url(r'^check_code/$', views.check_code, name='check_code'),

    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^userAgreement/$', views.userAgreement, name='userAgreement'),

    url(r'^siteNotice/$', views.siteNotice, name='siteNotice'),
    url(r'^aboutJadeJade/$', views.aboutJadeJade, name='aboutJadeJade'),
    url(r'^helpCenter/$', views.helpCenter, name='helpCenter'),
    url(r'^userdetail/$', views.userdetail, name='userdetail'),

    url(r'^logout/$', views.logout, name='logout'),
    url(r'^findpassword/$', views.findpassword, name='findpassword'),
    url(r'^modifypassword/$', views.modifypassword, name='modifypassword'),

    url(r'^modifyemail/$', views.modifyemail, name='modifyemail'),


]
