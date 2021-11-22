from rest_framework import permissions

class BasePermission(object):

    def has_permission(self,request,view):
        return True
    
    def has_object_permission(self,request,view,obj):
        return True


class IsAutorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author ==request.user
