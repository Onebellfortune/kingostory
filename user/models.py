from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class Itemlist(models.Model):
    def __str__(self):
        return self.name
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    weapon=models.TextField()
    create_date=models.DateTimeField()

class Itemlist_monster(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    weapon=models.TextField()
    create_date=models.DateTimeField()

class Itemlist_store(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    weapon=models.TextField()
    create_date=models.DateTimeField()

class Userstatus(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    money = models.IntegerField(default=0)
    damage=models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user=kwargs['instance']
        Userstatus.objects.create(user=user)
post_save.connect(on_post_save_for_user,sender=settings.AUTH_USER_MODEL)


class Itemstatus(models.Model):
    def __str__(self):
        return self.item.name
    item=models.OneToOneField(Itemlist,on_delete=models.CASCADE,primary_key=True)
    price=models.IntegerField()
    itemlevel=models.IntegerField()
    create_date=models.DateTimeField()

class Itemstatus_monster(models.Model):
    def __str__(self):
        return self.item.name
    item=models.OneToOneField(Itemlist_monster,on_delete=models.CASCADE,primary_key=True)
    price=models.IntegerField()
    itemlevel=models.IntegerField()
    create_date=models.DateTimeField()

class Itemstatus_store(models.Model):
    def __str__(self):
        return self.item.name
    item=models.OneToOneField(Itemlist_store,on_delete=models.CASCADE,primary_key=True)
    price=models.IntegerField()
    itemlevel=models.IntegerField()
    create_date=models.DateTimeField()

class Monsterstatus(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    hp = models.IntegerField(default=1)
    boss = models.BooleanField(default=False)
    itemid = models.ForeignKey(Itemlist_monster, on_delete=models.CASCADE)
    probability = models.FloatField()
    create_date=models.DateTimeField()


class User_catch_Monster(models.Model):
    uid = models.ForeignKey(Userstatus, on_delete=models.CASCADE)
    mid = models.ForeignKey(Monsterstatus, on_delete=models.CASCADE)
    catch_date = models.DateField()

    class Meta:
        unique_together = ("uid", "mid")

class weaponlist(models.Model):
    def __str__(self):
        return self.item.name
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Itemlist,on_delete=models.CASCADE)

