from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
# Create your views here.
from firstgame.models import *  # 커리큘럼 클래스 사용
import random

# Create your views here.


def game1(request):
    rand = random.randint(1, 10)
    result = ""
    #sangsick = 상식.objects.all()
    sangsick = 상식.objects.get(고유번호=rand)
    result = '%s.%s --------- %s < %s >' % (
        sangsick.고유번호, sangsick.문제, sangsick.정답, sangsick.카테고리)
    return HttpResponse(result)


def test(request):
    global count
    global lis
    lis2 = []

    for i in lis[0]:
        lis2.append(i)

    del lis[0]

    count += 1

    if count < 5:
        return render(request, 'firstgame/test.html', {
            'lis': lis2, 'cnt': count
        })
    else:
        count = 0
        return render(request, 'firstgame/testLast.html', {
            'lis': lis2, 'cnt': count
        })


def start(request):
    global lis
    global count

    lis = [[None for i in range(4)]for j in range(5)]
    rand = random.sample(range(1, 11), 5)

    for i in range(5):
        sangsick = 상식.objects.get(고유번호=rand[i])
        lis[i][0] = sangsick.고유번호
        lis[i][1] = sangsick.문제
        lis[i][2] = sangsick.정답
        lis[i][3] = sangsick.카테고리
    count = 0

    return render(request, 'firstgame/start.html')


def testmusic(request):

    return render(
        request, 'firstgame/testmusic.html'

    )


def quiz(request):
    datas = 상식.objects.order_by('고유번호')
    p = Paginator(datas, 1)

    if request.method == 'POST':
        str = request.POST.get("rand")
        rand = str.split(" ")
        id = request.POST.get('id')
        count = request.POST.get('count')
        result = request.POST.get('result')
    elif request.method == 'GET':
        count = 1
        result = ""
        rand = random.sample(range(1, p.count), 10 + 1)
        str = ""
        str += "%s" % rand[0]
        for i in range(1, len(rand)):
            str += " %s" % rand[i]
    else:
        id = 1
    if count is None:
        count = 1
    num = 2

    info = p.page(int(rand[int(count) - 1]))
    print("quiz에서 받음 : /%s/%s/ " % (rand, str))
    if int(count) > 10:
        context = {
            'result': result,
        }
        return render(request, 'firstgame/result.html', context)
    else:
        context = {
            'info': info,
            'count': count,
            'result': result,
            'rand': str,
        }
    return render(request, 'firstgame/quiz.html', context)


def answer(request):
    if request.method == 'POST':
        num2 = request.POST.get('id')
        info = request.POST.get('info')
        a = request.POST.get('a')
        count = request.POST.get('count')
        result = request.POST.get('result')
        str = request.POST.get('rand')
        print("/" + str + "/")
        rand = str.split(" ")
        answer = 상식.objects.get(고유번호=int(rand[int(count)]))
        print("answer에서 받음 : /%s/%s/ " % (rand, str))
        if answer.정답 == a:
            answer = count + "번 문제는 정답입니다."
            result += "1"
        else:
            answer = count + "번 문제는 오답입니다."
            result += "0"
        data = {
            'info': answer,
            'id': num2,
            'count': count,
            'result': result,
            'rand': str,
        }

    return render(request, 'firstgame/answer.html', data)


def home(request):
    return render(request, 'firstgame/index.html', {})
