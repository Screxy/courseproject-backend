from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import VkUser


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class VkUserInline(admin.StackedInline):
    model = VkUser
    can_delete = False
    verbose_name_plural = "vk_user"


class VkUserAdmin(admin.ModelAdmin):
    list_display = ["user", "vk_user_id", "access_token"]


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [VkUserInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(VkUser, VkUserAdmin)
