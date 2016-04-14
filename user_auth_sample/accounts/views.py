from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    template = 'accounts/user_profile.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)
