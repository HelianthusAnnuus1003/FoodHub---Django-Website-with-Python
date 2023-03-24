from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.models import *

def themVaoGioHang(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(float(request.POST.get("product_id")))
            product_check = Product.objects.get(id = prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Sản phẩm đã có trong giỏ hàng!"})
                else:
                    prod_qty = int(float(request.POST.get("product_qty")))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Thêm sản phẩm vào thành công!"})
                    else:
                        return JsonResponse({'status': "Chỉ còn "+ str(product_check.quantity) +" sản phẩm ở trong cửa hàng!"})
            else:
                return JsonResponse({'status': "Không tìm thấy sản phẩm!"})
        else:
            return JsonResponse({'status': "Cần đăng nhập để có thể tiếp tục!"})
        
    return redirect("/")

@login_required(login_url='dangNhap')
def gioHang(request):
    categories = Category.objects.filter(status=0)
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.selling_price * item.product_qty
    cartLength = Cart.objects.count()
    wishListLength = Wishlist.objects.count()
    context = {'cart': cart, 'categories': categories, 'total_price': total_price, 'cartLength': cartLength, 'wishListLength': wishListLength}
    return render(request, "store/giohang.html", context)

def capNhatGioHang(request):
    if request.method == "POST":
        prod_id = int(float(request.POST.get("product_id")))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(float(request.POST.get("product_qty")))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status': "Cập nhật số lượng sản phẩm thành công!"})
    return redirect("/")

def xoaSanphamGioHang(request):
    if request.method == "POST":
        prod_id = int(float(request.POST.get("product_id")))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.delete()
            return JsonResponse({'status': "Xoá sản phẩm khỏi giỏ hàng thành công!"})
        else:
                return JsonResponse({'status': "Không tìm thấy sản phẩm!"})
    else:
        return JsonResponse({'status': "Cần đăng nhập để có thể tiếp tục!"})
    return redirect("/")