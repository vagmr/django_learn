"""
@文件        :permission.py
@说明        :自定义权限类 
@时间        :2024/02/02 00:50:33
@作者        :vagmr
@版本        :1.1
"""


from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS


class CustomIsAdminUser(IsAdminUser):
    message = {
        'message': '你没有执行该操作的权限 （You do not have permission to perform this action.)',
        'code': 403,
        'author': 'vagmr'
    }


class IsOnlyOwner(BasePermission):
    message = {
        'message': '你没有执行该操作的权限 （You do not have permission to perform this action.)',
        'code': 403,
        'author': 'vagmr'
    }

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.teacher
