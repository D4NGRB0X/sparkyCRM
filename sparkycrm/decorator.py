from django.http import HttpResponseRedirect
from django.urls import reverse

def login_check(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            #return to home page url
            return HttpResponseRedirect(reverse('sparkycrm:'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func