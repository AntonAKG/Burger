$(document).ready(function () {
    var successMessage = $("#jq-notification");

    $(document).on("submit", ".add-to-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#shop-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        var form = $(this);
        var product_id = form.find("[name='product_id']").val();
        var add_to_cart_url = "{% url 'cart_add' %}";

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                cartCount++;
                goodsInCartCount.text(cartCount);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Помилка під час додавання товару в кошик");
            },
        });
    });

    // $(document).on("click", ".remove-from-cart", function (e) {
    //     e.preventDefault();
    //
    //     var goodsInCartCount = $("#goods-in-cart-count");
    //     var cartCount = parseInt(goodsInCartCount.text() || 0);
    //
    //     var cart_id = $(this).data("cart-id");
    //     var remove_from_cart = $(this).attr("href");
    //
    //     $.ajax({
    //
    //         type: "POST",
    //         url: remove_from_cart,
    //         data: {
    //             cart_id: cart_id,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },
    //         success: function (data) {
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //             setTimeout(function () {
    //                 successMessage.fadeOut(400);
    //             }, 7000);
    //
    //             cartCount -= data.quantity_deleted;
    //             goodsInCartCount.text(cartCount);
    //
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);
    //
    //         },
    //
    //         error: function (data) {
    //             console.log("Помилка під час видалення товару з кошик");
    //         },
    //     });
    // });
    //
    //
    //
    //
    // $(document).on("click", ".decrement", function () {
    //     var url = $(this).data("cart-change-url");
    //     var cartID = $(this).data("cart-id");
    //     var $input = $(this).closest('.input-group').find('.number');
    //     var currentValue = parseInt($input.val());
    //     if (currentValue > 1) {
    //         $input.val(currentValue - 1);
    //         updateCart(cartID, currentValue - 1, -1, url);
    //     }
    // });
    //
    // $(document).on("click", ".increment", function () {
    //     var url = $(this).data("cart-change-url");
    //     var cartID = $(this).data("cart-id");
    //     var $input = $(this).closest('.input-group').find('.number');
    //     var currentValue = parseInt($input.val());
    //
    //     $input.val(currentValue + 1);
    //
    //     updateCart(cartID, currentValue + 1, 1, url);
    // });
    //
    // function updateCart(cartID, quantity, change, url) {
    //     $.ajax({
    //         type: "POST",
    //         url: url,
    //         data: {
    //             cart_id: cartID,
    //             quantity: quantity,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },
    //
    //         success: function (data) {
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //             setTimeout(function () {
    //                  successMessage.fadeOut(400);
    //             }, 7000);
    //
    //             var goodsInCartCount = $("#goods-in-cart-count");
    //             var cartCount = parseInt(goodsInCartCount.text() || 0);
    //             cartCount += change;
    //             goodsInCartCount.text(cartCount);
    //
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);
    //
    //         },
    //         error: function (data) {
    //             console.log("Помилка під час зміни кількості товару в кошику");
    //         },
    //     });
    // }
});