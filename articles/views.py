from django.shortcuts import render

# Create your views here.
def index(request):
    # url로부터 호출되면
    # 메인 페이지 응답 객체를 만들어서 반환
    return render(request, 'articles/index.html')