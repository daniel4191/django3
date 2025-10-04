from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    if request.method == "POST":
        # LoginForm 인스턴스를 만들며, 입력 데이터는 request.POST를 사용
        form = LoginForm(data = request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #username, password 등록 데이터랑 매치하는지
            user = authenticate(username = username, password = password)
            
            # 등록 데이터와 매치가 된다면
            if user:
                login(request, user)
                return redirect("/posts/feeds/")
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")
                
        # 어떤 경우든 실패한 경우 - 데이터검증, 사용자 검사 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {"form":form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form":form}
        return render(request, "users/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("/users/login/")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/posts/feeds/")
        
    else:
        form = SignupForm()
        
    context = {"form": form}
    return render(request, "users/signup.html", context)