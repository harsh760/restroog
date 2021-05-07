# from django.conf.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/?$', views.login, name='login'),
    re_path(r'^logout/?$', views.logout, name='logout'),
    re_path(r'^home/?$',views.home, name='home'),
    re_path(r'^dbhome/?$',views.home, name='home'),
    re_path(r'^signup/?$', views.signup, name='signup'),
    re_path(r'^search/?$',views.search,name='search'),
    re_path(r'^details/?$',views.details,name='details'),
    re_path(r'^dbdetails/?$',views.details,name='dbdetails'),
    re_path(r'^savedetails/?$',views.editDetails,name='editDetails'),
    re_path(r'^addtocart/cart/?$',views.cart,name='cart'),
    re_path(r'^cart/?$',views.cart,name='cart'),
    re_path(r'^history/?$',views.history,name='history'),
    re_path(r'^addrating/(?P<restname>[a-zA-Z0-9\s]+)/?$',views.restrating,name='restrating'),
    re_path(r'^dbhistory/?$',views.dbhistory,name='dbhistory'),
    re_path(r'^addtocart/?$',views.saveToCart,name='saveToCart'),
    re_path(r'^ratings/?$',views.ratings,name='ratings'),
    re_path(r'^restprofile/?$',views.restprofile,name='restprofile'),
    re_path(r'^resthistory/?$',views.restaurantOrderHistory,name='resthistory'),
    re_path(r'^delivered/?$',views.delivered,name='delivered'),
    re_path(r'^accepted/?$',views.accepted,name='accepted'),
    re_path(r'^declined/?$',views.declined,name='declined'),
    re_path(r'^decide/?$',views.decide,name='decide'),
    re_path(r'^onway/?$',views.onway,name='onway'),
    re_path(r'^addfooditem/?$',views.addfooditem,name='addfooditem'),
    re_path(r'^removefooditem/?$',views.removefooditem,name='removefooditem'),
    # re_path(r'^callback/?$', views.callback, name='callback'),
    # re_path(r'^addtocart/pay/?$', views.initiate_payment, name='pay'),
    #!! url(r'^makepaymenet/?$'.views.makepaymenet,name='makepaymenet'),
    re_path(r'^restaurant/(?P<restname>[a-zA-Z0-9\s]+)/?$',views.restview,name='restview'),
    re_path(r'^about/?$',views.about,name='about'),

    re_path(r'^deleteAccount/?$',views.deleteAccount,name='deleteAccount'),
    re_path(r'^forget_password/?$',views.otp_sent,name='forget_password'),
    re_path(r'^email/?$',views.email,name='email'),
]

# urlpatterns = [
#     re_path(r'^$', views.home, name='home'),
#     re_path(r'^login/?$', views.login, name='login'),
#     re_path(r'^logout/?$', views.logout, name='logout'),
#     re_path(r'^home/?$',views.home, name='home'),
#     re_path(r'^signup/?$', views.signup, name='signup'),
#     re_path(r'^search/?$',views.search,name='search'),
#     re_path(r'^details/?$',views.details,name='details'),
#     re_path(r'^savedetails/?$',views.editDetails,name='editDetails'),
#     re_path(r'^cart/?$',views.cart,name='cart'),
#     re_path(r'^history/?$',views.history,name='history'),
#     re_path(r'^addtocart/?$',views.saveToCart,name='saveToCart'),
#     re_path(r'^restprofile/?$',views.restprofile,name='restprofile'),
#     re_path(r'^resthistory/?$',views.restaurantOrderHistory,name='resthistory'),
#     re_path(r'^delivered/?$',views.delivered,name='delivered'),
#     re_path(r'^addfooditem/?$',views.addfooditem,name='addfooditem'),
#     re_path(r'^removefooditem/?$',views.removefooditem,name='removefooditem'),

#     # url(r'^makepaymenet/?$'.views.makepaymenet,name='makepaymenet'),
#     re_path(r'^restaurant/(?P<restname>[a-zA-Z0-9\s]+)/?$',views.restview,name='restview'),
#     re_path(r'^about/?$',views.about,name='about'),
# ]
