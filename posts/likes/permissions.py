from rest_framework.permissions import BasePermission
from likes.models import Like

class LikeExistsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        super().has_object_permission(request, view, obj)
        if not Like.objects.filter(post_id=str(obj.id), user__user_id=request.user.user_id):
            return True
        return False
    
class LikeNotExistsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        super().has_object_permission(request, view, obj)
        if Like.objects.filter(post_id=str(obj.id), user__user_id=request.user.user_id):
            return True
        return False