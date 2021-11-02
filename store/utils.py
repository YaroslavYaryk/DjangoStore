from store.services.get_cart import get_cart_by_user


class DataMixin(object):

    """Mixin for all clases that we have to
    make they shorter and fater"""
    # paginate_by = 10   #needs to be queryset in function(not import tegs '{% load menu_tags %}' )  

    def get_user_context(self, **kwargs):
        context = kwargs
        
        context["cart"] = get_cart_by_user(self.request.user)
        return context