from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    data = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    op = data
    purpose = ""

    if removepunc == "on":
        tempStr = ""
        puns = '''!@#$%^&*();'.,/:?>'''
        for i in op:
            if i not in puns:
                tempStr += i
        params = {"purpose": "remove punctuations", "answer": tempStr}
        op = tempStr
        purpose += "| remove punctuations "

    if fullcaps == "on":
        print("2", op)
        op = op.upper()
        params = {"purpose": "fullcaps", "answer": op}
        purpose += "| caps "

    if newlineremover == "on":
        tempStr = ""
        for i in op:
            if i != '\n':
                tempStr += i

        params = {'purpose': 'New Line remove', 'answer': tempStr}
        op = tempStr
        purpose += "| remove new line "

    if extraspaceremover == 'on':
        tempStr = ""
        for index, ch in enumerate(op):
            if not (op[index] == " " and op[index+1] == " "):
                tempStr += ch
        params = {'purpose': 'spaces remove', 'answer': tempStr}
        op = tempStr
        purpose += "| spaces removed "

    params = {"purpose": purpose, "answer": op}

    if removepunc == "on" or fullcaps == "on" or newlineremover == "on" or extraspaceremover == "on":
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Select something!")
