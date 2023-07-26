from django.contrib.auth.models import Group

def user_groups(request):
    if request.user.is_authenticated:
        groups = Group.objects.filter(user=request.user)
    else:
        groups = []
    return {'user_groups': groups}