from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from firstgame.models import * # 커리큘럼 클래스 사용
import random

# Create your views here.

def game1(request):
     rand = random.randint(1,10)
     result = ""
     #sangsick = 상식.objects.all()
     sangsick = 상식.objects.get(고유번호 = rand)
     result = '%s.%s --------- %s < %s >' % (sangsick.고유번호, sangsick.문제, sangsick.정답, sangsick.카테고리)
     return HttpResponse(result)

def test(request):

    rand = random.randint(1,10)
    sang = 상식.objects.get(고유번호 = rand)

    return render(
        request, 'firstgame/test.html',
        {'data': sang}

    )
