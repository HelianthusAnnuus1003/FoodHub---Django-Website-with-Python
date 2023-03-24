from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *

# Trang chu
def trangChu(request):
    trending_products = Product.objects.filter(trending=1)
    products = Product.objects.filter(status=0)
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.filter(status=0)
    cartLength = Cart.objects.count()
    wishListLength = Wishlist.objects.count()
    context = {'products':products, 'categories':categories, 'cartLength': cartLength, 'wishListLength': wishListLength, 'trending_products': trending_products, 'page_obj': page_obj}
    return render(request, 'store/trangchu.html', context)

# Tin tuc
def tinTuc(request):
    products = Product.objects.filter(status=0)
    categories = Category.objects.filter(status=0)
    context = {'products':products, 'categories':categories}
    return render(request, 'store/tintuc.html', context)

# Lien he
def lienHe(request):
    products = Product.objects.filter(status=0)
    categories = Category.objects.filter(status=0)
    context = {'products':products, 'categories':categories}
    return render(request, 'store/lienhe.html', context)  

# Danh muc
def danhMuc(request):
    categories = Category.objects.filter(status=0)
    cartLength = Cart.objects.count()
    wishListLength = Wishlist.objects.count()
    context = {'categories':categories, 'cartLength': cartLength, 'wishListLength': wishListLength}
    return render(request, 'store/danhmuc.html', context)

# San pham theo danh muc
def sanPhamTheoDanhMuc(request, slug):
    if(Category.objects.filter(slug = slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        categories = Category.objects.filter(status=0)
        category_name = Category.objects.filter(slug=slug).first()
        cartLength = Cart.objects.count()
        wishListLength = Wishlist.objects.count()    
        context = {'products': products, 'category_name': category_name, 'categories': categories, 'cartLength': cartLength, 'wishListLength': wishListLength, 'page_obj': page_obj}
        return render(request, "store/products/sanphamtheodanhmuc.html", context)
    else:
        messages.warning(request, "Không tìm thấy danh mục!")
        return redirect('danhMuc')

# Chi tiet san pham
def chiTietSanPham(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug = cate_slug, status = 0)):
        if(Product.objects.filter(slug = prod_slug, status = 0)):
            categories = Category.objects.filter(status=0)
            products = Product.objects.filter(category__slug=cate_slug)
            paginator = Paginator(products, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            product = Product.objects.filter(slug = prod_slug, status = 0).first()
            cartLength = Cart.objects.count()
            wishListLength = Wishlist.objects.count()    
            context = {'product': product, 'products': products, 'categories': categories, 'cartLength': cartLength, 'wishListLength': wishListLength, 'page_obj': page_obj}
        else:
            messages.error(request, "Không tìm thấy sản phẩm!")
            return redirect('sanPhamTheoDanhMuc')
    else:
        messages.error(request, "Không tìm thấy danh mục!")
        return redirect('sanPhamTheoDanhMuc')        
    return render(request, "store/products/chitietsanpham.html", context)

def danhSachSanPhamAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)
    return JsonResponse(productsList, safe=False)

def timKiemSanPham(request):
    if request.method == 'POST':
        searchProductValue = request.POST.get('searchProductValue')
        if searchProductValue == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name=searchProductValue).first()
            if product:
                return redirect('danh-muc/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, "Không tìm thấy sản phẩm nào trùng khớp!")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))    