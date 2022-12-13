from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
