from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def admin_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='/logintosite/login'):
    actual_decorator=user_passes_test(
        lambda user: user.is_active and user.IsAdmin,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorator
    return actual_decorator

def doctor_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='/logintosite/login'):
    actual_decorator=user_passes_test(
        lambda user: user.is_active and user.IsDoctor,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorator
    return actual_decorator