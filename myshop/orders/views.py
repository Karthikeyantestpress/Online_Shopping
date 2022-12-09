from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm


def show_empty_orderform_to_place_order(request):
    cart = Cart(request)
    form = OrderCreateForm()
    return render(
        request, "orders/order/create.html", {"cart": cart, "form": form}
    )


def show_order_confirmation_after_placing_the_order(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                price=item["price"],
                quantity=item["quantity"],
            )
        cart.clear()
        return render(request, "orders/order/created.html", {"order": order})


def order_create(request):
    if request.method == "GET":
        Response = show_empty_orderform_to_place_order(request)
    elif request.method == "POST":
        Response = show_order_confirmation_after_placing_the_order(request)
    return Response
