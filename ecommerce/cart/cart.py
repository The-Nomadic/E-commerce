class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, Create new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all the pages
        self.cart = cart
