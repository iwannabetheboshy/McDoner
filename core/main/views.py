from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import FeedBack
from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect
from requests import get as tg_get


def main(request):  
    form = FeedBackForm()
    alt_all = ['стрит фуд', 'food truck', 'fast food', 'фуд трак купить', 'стрит фуд', 'фаст фуд', 'купить фудтрак', 'фудтрак купить', 'фудтрак +на колесах' ] 
    name_all = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    photo = zip(alt_all,name_all)
    return render(request, "main/index.html", {'form': form, "photo_list" : photo})

@csrf_exempt    
def sendFeedBack(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        question=request.POST.get('question')
        print('name =', name, 'phone', phone, 'question =', question)
        
        new = FeedBack(name=name, phone=phone, question=question)
        new.save()
        
        # Отправка сообщение на tg
        tg_get("https://api.telegram.org/bot6110667189:AAFgWzCCCg3Sf64bg6oHCZkC5zaSZdi7R1o/sendmessage?chat_id={user_id}&text={text}".format(text=f"Имя: {name}\nТелефон: {phone}\nЗапрос:{question}",user_id=6322918067))
    return HttpResponse('<h2>form submitted.</h2>')
