from rest_framework.permissions import BasePermission


class OnlyAdminDelete(BasePermission):
    message = "فقط مدیر اجازه حذف دارد."

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_staff
        return True
