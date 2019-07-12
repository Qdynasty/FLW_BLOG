from django.contrib import admin

# Register your models here.

from blog.models import DocInfo, TypeInfo, UserInfo


"""
注册 模型类到  站点管理
"""
admin.site.register(DocInfo)
admin.site.register(TypeInfo)
admin.site.register(UserInfo)