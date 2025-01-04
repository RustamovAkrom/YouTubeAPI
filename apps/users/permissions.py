from graphql_jwt.exceptions import PermissionDenied


class BasePermission:
    def has_permission(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to access this data.")
        
        if not request.user.is_active:
            raise PermissionDenied("You must be activate your account.")
        return True


class IsAuthenticatedPermission(BasePermission):
    pass


class IsOwnerPermission(BasePermission):
    def has_permission(self, request, user_id):
        if request.user.id != int(user_id):
            raise PermissionDenied("You cannot update another user`s profile.")
        return True


class IsSuperuserPermission(BasePermission):
    def has_permission(self, request):
        if not request.user.is_sueruser:
            raise PermissionDenied("You cannot update another user`s profile. You not superuser")
        return super().has_permission(request)
