import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Portfolio,Service,Teams,Murojat
# Create your views here.

def home(malumot):
    if 'qidiruv' in malumot.POST:
        son = malumot.POST.get('qidiruv')
        text = str(son).strip()
        qidirish = Q(ism__contains=text)| Q(familya__startswith=text)|\
                   Q(lavozim__nomi__contains=text)|Q(yosh__startswith=text)
        loyiha=Portfolio.objects.all()
        loyiha1=Service.objects.all()
        loyiha2 = Teams.objects.filter(qidirish)
        return render(malumot, 'index.html', {'worke':loyiha2,'work':loyiha,'works':loyiha1})
    elif 'qidiruv' in malumot.POST:
        bir = malumot.POST.get('qidiruv')
        text = str(bir).strip()
        qidirish = Q(nomi__startswith=text)| Q(malumot__matn__contains=text)
        loyiha1 = Service.objects.filter(qidirish)
        loyiha=Portfolio.objects.all()
        loyiha2=Teams.objects.all()
        return render(malumot, 'index.html', {'works':loyiha1,'work':loyiha,'worke':loyiha2})
    elif 'qidiruv' in malumot.POST:
        soz = malumot.POST.get('qidiruv')
        text = str(soz).strip()
        qidirish = Q(nomi__startswith=text)| Q(company_name__startswith=text)|\
                   Q(tur__nomi__contains=text)|Q(sana__startswith=text)|Q(link__startswith=text)
        loyiha=Portfolio.objects.filter(qidirish)
        loyiha1=Service.objects.all()
        loyiha2=Teams.objects.all()
        return render(malumot, 'index.html', {'work': loyiha,'works':loyiha1,'worke':loyiha2})
    elif malumot.method=='POST':
        ismi = malumot.POST.get('name')
        gmaili = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        sana = datetime.datetime.now()
        Murojat(ism=ismi,gmail=gmaili,title=mavzu,text=message,vaqt=sana).save()
    loyiha = Portfolio.objects.all()
    loyiha1 = Service.objects.all()
    loyiha2 = Teams.objects.all()
    return render(malumot,'index.html',{'work':loyiha,'works':loyiha1,'worke':loyiha2})

def portfolio(malumot,id):
    loyiha = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':loyiha})

# def gmail(malumot,id):
#     loyihalar = Portfolio.objects.get(id=id)
#     return render(malumot,'portfolio-details.html',{'works':loyihalar})