from store.services.get_cart import get_cart_by_user


class DataMixin(object):

    """Mixin for all clases that we have to
    make they shorter and fater"""
    paginate_by = 12   #needs to be queryset in function(not import tegs '{% load menu_tags %}' )  

    
    def __init__(self) -> None:
        
        self.choice_order = {
            "most popular 👇": "-ip",
            "most popular 👆": "ip",
            "most liked 👆": "likes",
            "most liked 👇": "-likes"
            }

        self.order_list = ["newest", "most popular 👇",
                    "most popular 👆", "most liked 👆", "most liked 👇"]

    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context["cart"] = get_cart_by_user(self.request.user)
            context["user"] = self.request.user
            context["order_list"] = self.order_list
        return context