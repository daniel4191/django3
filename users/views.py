from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    if request.method == "POST":
        # LoginForm 인스턴스를 만들며, 입력 데이터는 request.POST를 사용
        form = LoginForm(data = request.POST)
        
        # LoginForm에 들어온 데이터가 적절한지 유효성 검사
        print("form.is_valid():", form.is_valid())
        
        # 유효성 검사 이후에는 cleaned_data에서 데이터를 가져와 사용
        print("form.cleaned_data:", form.cleaned_data)
        context = {"form":form}
    
    else:
        form = LoginForm()
        context = {"form": form}
        
    return render(request, "users/login.html", context)