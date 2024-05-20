from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self,request,view):
        return bool(
                    request.method in SAFE_METHODS and
                    request.user and request.user.is_staff
                    or
                    request.user and request.user.is_superuser

                )


