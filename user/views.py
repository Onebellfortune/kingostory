from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from random import *

# Create your views here.


def index(request):
    item_list = Itemlist.objects.order_by('-create_date')
    context = {'item_list': item_list}
    return render(request, 'user/Item_list.html', context)


def detail(request, itemlist_id):
    itemstatus = Itemstatus.objects.get(item=itemlist_id)
    itemlist=Itemlist.objects.get(id=itemlist_id)
    context = {'itemstatus': itemstatus,'itemlist':itemlist}
    return render(request, 'user/Item_detail.html', context)

def detail_shop(request,itemlist_id):
    itemstatus = Itemstatus_store.objects.get(item=itemlist_id)
    itemlist = Itemlist_store.objects.get(id=itemlist_id)
    context = {'itemstatus': itemstatus, 'itemlist': itemlist}
    return render(request, 'user/shop_detail.html', context)


def item_sell(request,itemlist_id):
    itemstatus=Itemstatus.objects.get(item=itemlist_id)
    context={'itemstatus':itemstatus}
    return render(request,'user/Item_detail.html',context)

def equip(request,username,item_id):
    try:
        person=User.objects.get(username=username)
        status=Userstatus.objects.get(user=person)

        personweapon=Itemlist.objects.get(owner=person,id=item_id)
        equipweapon=weaponlist.objects.get(user=person)
        status.damage = status.level * 100 + personweapon.itemstatus.itemlevel * 100
        equipweapon.item=personweapon
        equipweapon.save()
        status.save()
        return redirect('user:index')
    except weaponlist.DoesNotExist:
        equipweapon = weaponlist(user=person, item=personweapon)
        status.damage=status.level*100
        equipweapon.save()
        return redirect('user:index')

def mypage(request,username):
    try:
        person=User.objects.get(username=username)
        itemlist = Itemlist.objects.filter(owner=person)
        equipped_item=weaponlist.objects.get(user=person)
        person.userstatus.damage = person.userstatus.level * 100 + equipped_item.item.itemstatus.itemlevel * 100
        context = {'person': person, 'itemlist': itemlist, 'equipped_item': equipped_item}
        return render(request, 'user/mypage.html', context)
    except weaponlist.DoesNotExist:
        context = {'person': person, 'itemlist': itemlist}
        person.userstatus.damage = person.userstatus.level * 100
        return render(request,'user/mypage.html',context)


def shop(request,username):
    person=User.objects.get(username=username)
    itemlist=Itemlist.objects.filter(owner=person)
    context={'person':person, 'itemlist':itemlist}
    return render(request,'user/shop.html',context)


def shop_sell(request,item_id):
    item=get_object_or_404(Itemlist,pk=item_id)
    itemprice=Itemstatus.objects.get(item=item).price
    itemowner=item.owner
    ownerstatus=Userstatus.objects.get(user=itemowner)
    ownerstatus.money+=itemprice
    ownerstatus.damage=ownerstatus.level*100
    ownerstatus.save()
    item.delete()
    return redirect('user:index')

def buy(request,username):
    itemlist=Itemlist_store.objects.all()
    person=User.objects.get(username=username)
    context={'itemlist':itemlist,'person':person}
    return render(request,'user/buy.html',context)

def shop_buy(request,item_id,username):
    person=User.objects.get(username=username)
    buyitem=Itemlist_store.objects.get(id=item_id)
    buyitemstatus=Itemstatus_store.objects.get(item=buyitem)
    if person.userstatus.money<buyitemstatus.price:
        return redirect('user:index')
    item=Itemlist(owner=person,name=buyitem.name,weapon=buyitem.weapon,create_date=timezone.now())
    itemstatus=Itemstatus(item=item,price=buyitemstatus.price,itemlevel=buyitemstatus.itemlevel,create_date=timezone.now())
    item.save()
    itemstatus.save()
    person.userstatus.money-=buyitemstatus.price
    person.userstatus.save()
    return redirect('user:index')


def monster(request):
    monster_list=Monsterstatus.objects.order_by('-create_date')
    context={'monster_list':monster_list}
    return render(request, 'user/monster.html', context)

def catch_monster(request,monster_id,username):
    attacker=User.objects.get(username=username)
    monster=Monsterstatus.objects.get(id=monster_id)
    monster.hp-=attacker.userstatus.damage
    monster.save()
    drop=monster.probability*100
    random=randint(1,100)
    if monster.boss==True:
        drop=100
    if monster.hp<=0:
        item = monster.itemid
        itemid=item.id
        monsteritem = Itemlist_monster.objects.get(id=itemid)
        monsteritemstatus=Itemstatus_monster.objects.get(item=item)
        person=User.objects.get(username=username)
        if random<=drop:
            getitem = Itemlist(owner=person, name=monsteritem.name, weapon=monsteritem, create_date=timezone.now())
            getitemstatus = Itemstatus(item=getitem, price=monsteritemstatus.price,
                                       itemlevel=monsteritemstatus.itemlevel, create_date=timezone.now())
            getitem.save()
            getitemstatus.save()
        monster.delete()
    return redirect('user:index')

def reinforce(request,username):
    person = User.objects.get(username=username)
    itemlist = Itemlist.objects.filter(owner=person)
    context = {'person': person, 'itemlist': itemlist}
    return render(request, 'user/reinforce.html', context)


def reinforce_item(request,item_id):
    reinforceitem=Itemlist.objects.get(id=item_id)
    item=Itemstatus.objects.get(item=item_id)
    random=randint(1,100)
    prob = 100-item.itemlevel*10
    if random<=prob:
        item.itemlevel+=1
        item.save()
    else:
        reinforceitem.delete()
        item.delete()
    return redirect('user:index')