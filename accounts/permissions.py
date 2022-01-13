from rest_framework.permissions import SAFE_METHODS, BasePermission


class AccountViewSetPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj == request.user or request.user.is_superuser
