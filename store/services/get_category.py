from store.models import IpModel


def get_client_ip(request):  # get current ip address

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip



def add_view_of_post(request, post):
    if not IpModel.objects.filter(ip=get_client_ip(request), product=post):
            IpModel.objects.create(ip=get_client_ip(
                request), product=post)