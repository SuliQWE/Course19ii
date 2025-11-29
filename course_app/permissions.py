from rest_framework.permissions import BasePermission



class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'student'

class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'teacher'