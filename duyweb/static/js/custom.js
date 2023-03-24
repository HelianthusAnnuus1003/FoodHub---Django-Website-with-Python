$(document).ready(function () {
    $(".btn-cong").click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest(".product-data").find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest(".product-data").find('.qty-input').val(value);
        }
    });

    $(".btn-tru").click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest(".product-data").find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest(".product-data").find('.qty-input').val(value);
        }
    });

    $(".addToCartBtn").click(function (e) {
        e.preventDefault();

        var prod_id = $(this).closest(".product-data").find('.prod_id').val();
        var prod_qty = $(this).closest(".product-data").find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/them-vao-gio-hang/",
            data: {
                'product_id': prod_id,
                'product_qty': prod_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
            }
        })
    });

    $(".addToWishListBtn").click(function (e) {
        e.preventDefault();

        var prod_id = $(this).closest(".product-data").find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/them-vao-yeu-thich/",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status)
            }
        })
    });

    $(".changeQuantity").click(function (e) {
        e.preventDefault();

        var prod_id = $(this).closest(".product-data").find('.prod_id').val();
        var prod_qty = $(this).closest(".product-data").find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/cap-nhat-gio-hang/",
            data: {
                'product_id': prod_id,
                'product_qty': prod_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
            }
        })
    });

    $(".deleteCartItemBtn").click(function (e) {
        e.preventDefault();

        var prod_id = $(this).closest(".product-data").find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/xoa-sanpham-gio-hang/",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
                $('.card-data').load(location.href + " .card-data");
            }
        })
    });

    $(".deleteWishListItemBtn").click(function (e) {
        e.preventDefault();

        var prod_id = $(this).closest(".product-data").find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/xoa-sanpham-yeu-thich/",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status)
                $('.card-data').load(location.href + " .card-data");
            }
        })
    });
});
