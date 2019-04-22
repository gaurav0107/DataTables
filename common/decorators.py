from functools import wraps

from django.shortcuts import redirect, reverse


def is_logged_in(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect(reverse('beam:login'))
        return f(request, *args, **kwargs)
    return decorated
