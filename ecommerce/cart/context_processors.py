from .cart import Cart


# Create context processors so that cart can work in all pages
def cart(request):
    # Return the default value from the cart
    return {'cart': Cart(request)}
