from rest_framework import permissions

class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_authenticated)

class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, object):     
        return (request.user == object or request.user.is_superuser)