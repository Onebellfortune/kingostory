from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name='user'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:itemlist_id>/',views.detail,name='detail'),
    path('mypage/<str:username>/',views.mypage,name='mypage'),
    path('mypage/<str:username>/equip/<int:item_id>/',views.equip,name='equip'),
    path('shop/<str:username>/',views.shop,name='shop'),
    path('buy/<str:username>/',views.buy,name='buy'),
    path('shop/buy/<str:username>/<int:item_id>/',views.shop_buy,name='shop_buy'),
    path('shop/detail/<int:itemlist_id>/',views.detail_shop,name='detail_shop'),
    path('shop/sell/<int:item_id>/',views.shop_sell,name='shop_sell'),
    path('monster/',views.monster,name='monster'),
    path('monster/catch/<int:monster_id>/<str:username>/',views.catch_monster,name='catch_monster'),
    path('reinforce/<str:username>/',views.reinforce,name='reinforce'),
    path('reinforce/item/<int:item_id>/',views.reinforce_item,name='reinforce_item'),
]