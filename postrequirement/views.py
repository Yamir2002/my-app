from django.shortcuts import render, redirect, HttpResponse
from member.models import Register
import requests
import datetime
from django.conf import settings

def sendWhastAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {"messaging_product": "whatsapp",
                "recipient_type": "individual",
                 "to": phoneNumber,
                 "type": "text",
                 "text": {"body": message}
                }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response. json()
    return ans
    
def requirement(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['require']
        
        message = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nRequirement: {text}'
        
        numbers = []
        num = Register.objects.values_list('phone')
        
        for n in num:
            numbers.append(f'91{n[0]}')
        
        for number in numbers:
            ans = sendWhastAppMessage(number, message)
            print(ans)
            
        return render(request, 'postrequirement/requirement.html')
    else:
        return render(request, 'postrequirement/requirement.html')
