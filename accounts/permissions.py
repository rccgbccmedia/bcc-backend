from rest_framework import permissions

class isAdminOrReadOnly(permissions.BasePermission):
    """
    permission check for admin or readonly.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff 
