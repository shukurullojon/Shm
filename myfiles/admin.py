from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)

class AdminPort(admin.ModelAdmin):
    list_display = ['id','nomi','company_name','rasm','tur','sana']

admin.site.register(Portfolio,AdminPort)

class Adminmalumot(admin.ModelAdmin):
    list_display = ['id', 'matn']

admin.site.register(Malumot,Adminmalumot)

class AdminSer(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'rasm', 'malumot']

admin.site.register(Service,AdminSer)

class Adminlavozim(admin.ModelAdmin):
    list_display = ['id', 'nomi']

admin.site.register(Lavozim,Adminlavozim)

class AdminTeam(admin.ModelAdmin):
    list_display = ['ism','familya','yosh','telegram','twitter','facebook','instagram','lavozim','rasm']

admin.site.register(Teams,AdminTeam)

class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','ism','gmail','title','text','vaqt']

admin.site.register(Murojat,AdminMurojat)


# class Admingmail(admin.ModelAdmin):
#     list_display = ['id','gmail']
#
# admin.site.register(Gmail,Admingmail)