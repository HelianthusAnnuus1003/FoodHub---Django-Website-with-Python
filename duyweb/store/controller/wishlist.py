from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.models import *

@login_required(login_url='dangNhap')
def index(request):
    categories = Category.objects.filter(status=0)
    cartLength = Cart.objects.count()
    wishListLength = Wishlist.objects.count()
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {'wishlists': wishlists, 'categories': categories, 'cartLength': cartLength, 'wishListLength': wishListLength}
    return render(request, 'store/yeuthich.html', context)

def themVaoYeuThich(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(float(request.POST.get("product_id")))
            product_check = Product.objects.get(id = prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status': "Sản phẩm này đã được yêu thích rồi!"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Yêu thích sản phẩm thành công!"})
            else:
                return JsonResponse({'status': "Không tìm thấy sản phẩm!"})
        else:
            return JsonResponse({'status': "Cần đăng nhập để có thể tiếp tục!"})
        
    return redirect("/")

def xoaSanphamYeuThich(request):
    if request.method == "POST":
        prod_id = int(float(request.POST.get("product_id")))
        if (Wishlist.objects.filter(user=request.user, product_id=prod_id)):
            wishlist = Wishlist.objects.get(product_id=prod_id, user=request.user)
            wishlist.delete()
            return JsonResponse({'status': "Xoá sản phẩm khỏi danh sách yêu thích thành công!"})
        else:
            return JsonResponse({'status': "Không tìm thấy sản phẩm!"})
    else:
        return JsonResponse({'status': "Cần đăng nhập để có thể tiếp tục!"})
    return redirect("/")