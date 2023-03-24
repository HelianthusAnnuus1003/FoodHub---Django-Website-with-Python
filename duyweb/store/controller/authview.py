from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from store.forms import CustomUserForm

def dangKy(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công, đăng nhập ngay nào!")
            return redirect("/dang-nhap")
    context = {'form':form}
    return render(request, "store/auth/dangky.html", context)

def dangNhap(request):
    if request.user.is_authenticated:
        messages.warning(request, "Người dùng này đã đăng nhập rồi!")
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Đăng nhập thành công!")
                return redirect("/")
            else:
                messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
                return redirect("/dang-nhap")
        return render(request, "store/auth/dangnhap.html")

def dangXuat(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Đăng xuất thành công!")
        return redirect("/")