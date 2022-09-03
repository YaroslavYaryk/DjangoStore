from users.models import NewUser


def get_user_by_id(user_id):
    return NewUser.objects.get(pk=user_id)
