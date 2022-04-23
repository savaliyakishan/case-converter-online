from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def answer(request):
    # using GET and POST Method in djengo site
    text = request.POST.get('textarea', 'default')
    lower = request.POST.get('lowercase', 'off')
    Sentence = request.POST.get('Sentencecase', 'off')
    UPPER = request.POST.get('UPPERCASE', 'off')
    Capitalized = request.POST.get('CapitalizedCase', 'off')
    aLtErNaTiNg = request.POST.get('aLtErNaTiNgcAsE', 'off')
    Title = request.POST.get('TitleCase', 'off')
    InVeRsE = request.POST.get('InVeRsECaSe', 'off')

    textcount = len(text)

    if lower == 'on':
        text = text.lower()
        past = {'textarea': text,'Type_case':'lower case','count':textcount}
        return render(request, "answer.html", past)
    elif Sentence == 'on':
        text = text
        text = text.capitalize()
        past = {'textarea': text, 'Type_case': 'Sentence case','count':textcount}
        return render(request, "answer.html", past)
    elif UPPER == 'on':
        text = text.upper()
        past = {'textarea': text,'Type_case':'UPPER CASE','count':textcount}
        return render(request, "answer.html", past)
    elif Capitalized == 'on':
        text = text.capitalize()
        past = {'textarea': text,'Type_case':'Capitalized Case','count':textcount}
        return render(request, "answer.html", past)
    elif aLtErNaTiNg == 'on':
        text = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(text)]
        text = "".join(text)
        past = {'textarea': text,'Type_case':'aLtErNaTiNg cAsE','count':textcount}
        return render(request, "answer.html", past)
    elif Title == 'on':
        text = text.title()
        past = {'textarea': text,'Type_case':'Title Case','count':textcount}
        return render(request, "answer.html", past)
    elif InVeRsE == 'on':
        text =text.swapcase()
        past = {'textarea': text,'Type_case':'InVeRsE CaSe','count':textcount}
        return render(request, "answer.html", past)
    else:
        return HttpResponse('error aave che bhai')
