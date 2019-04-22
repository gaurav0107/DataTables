from django.db.models import Q

from beam.models import AmplifyUser


def validate_user(username, password):
    if AmplifyUser.objects.filter(Q(username=username) | Q(email_id=username)).exists():
        if AmplifyUser.objects.filter(password=password).exists():
            user_details = AmplifyUser.objects.get(username=username)
            return {"user_id": user_details.id,
                    "email_address": user_details.first_name,
                    "username": user_details.username,
                    "success": True}
        else:
            return {"error": "Oops!! Username and Password do not match",
                    "success": False}
    else:
        return {"error": "Oops!! This Username do not exist", "success": False}
