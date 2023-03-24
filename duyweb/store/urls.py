from django.urls import path
from . import views
from store.controller import authview, cart, wishlist, checkout

urlpatterns = [
    path('', views.trangChu, name = 'trangChu'),
    path('tin-tuc', views.trangChu, name = 'tinTuc'),
    path('lien-he', views.trangChu, name = 'lienHe'),

    path('danh-muc', views.danhMuc, name = 'danhMuc'),
    path('danh-muc/<str:slug>', views.sanPhamTheoDanhMuc, name = 'sanPhamTheoDanhMuc'),
    path('danh-muc/<str:cate_slug>/<str:prod_slug>', views.chiTietSanPham, name = 'chiTietSanPham'),

    path('dang-ky/', authview.dangKy, name = 'dangKy'),
    path('dang-nhap/', authview.dangNhap, name = 'dangNhap'),
    path('dang-xuat/', authview.dangXuat, name = 'dangXuat'),

    path('gio-hang/', cart.gioHang, name = 'gioHang'),
    path('them-vao-gio-hang/', cart.themVaoGioHang, name = 'themVaoGioHang'),
    path('cap-nhat-gio-hang/', cart.capNhatGioHang, name = 'capNhatGioHang'),
    path('xoa-sanpham-gio-hang/', cart.xoaSanphamGioHang, name = 'xoaSanphamGioHang'),

    path('yeu-thich/', wishlist.index, name = 'yeuThich'),
    path('them-vao-yeu-thich/', wishlist.themVaoYeuThich, name = 'themVaoYeuThich'),
    path('xoa-sanpham-yeu-thich/', wishlist.xoaSanphamYeuThich, name = 'xoaSanphamYeuThich'),

    path('thanh-toan', checkout.index, name = 'thanhToan'),
    path('dat-hang', checkout.datHang, name = 'datHang'),


    path('danh-sach-san-pham', views.danhSachSanPhamAjax),
    path('tim-kiem-san-pham', views.timKiemSanPham, name = 'timKiemSanPham'),
]