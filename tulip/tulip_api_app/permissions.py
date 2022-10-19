from rest_framework import permissions


# creating cutom permission to check user role

class IsStudent(permissions.BasePermission):
    ''' This will validate if user is student and return True or False accordingly'''

    def has_permission(self, request, view):
        if request.user.user_role == 1:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    ''' This will validate if user is Teacher and return True or False accordingly'''

    def has_permission(self, request, view):
        if request.user.user_role == 2:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    ''' This will validate if user is Admin and return True or False accordingly'''

    def has_permission(self, request, view):
        if request.user.user_role == 3:
            return True
        return False





