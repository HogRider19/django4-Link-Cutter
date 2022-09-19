from rest_framework.permissions import BasePermission


class OnlyOwnObjects(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.user.id == obj.user.id:
            return True

        return False