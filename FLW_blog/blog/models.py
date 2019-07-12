from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """用户表"""
    id = models.AutoField(primary_key=True, verbose_name="主键")
    uname = models.CharField(max_length=20,verbose_name="用户昵称")

    class Meta:
        db_table = "user_info"
        verbose_name = "用户表"

    def __str__(self):
        return self.uname







class DocInfo(models.Model):
    """ 文档表 """
    id = models.AutoField(primary_key=True, verbose_name="主键")
    dname = models.CharField(max_length=20, verbose_name="文档名称")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    """
    用户 文档  一对多
    """
    user_id = models.ForeignKey("UserInfo",
                                on_delete=models.CASCADE,
                                related_name="docs",
                                verbose_name="文档外键"
                                )
    """
    技术文档类型 文档  多对多
    """
    class Meta:
        db_table = 'doc_info'
        verbose_name = '文档信息'

    def __str__(self):
        return self.dname






class TypeInfo(models.Model):
    """ 文档 类型表 """
    id = models.AutoField(primary_key=True, verbose_name="主键")
    tname = models.CharField(max_length=20, verbose_name="文档类型 名称")
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')

    """
    技术文档类型 文档  多对多
    """
    did = models.ManyToManyField(DocInfo)

    class Meta:
        db_table = 'type_info'
        verbose_name = '类型信息'

    def __str__(self):
        return self.tname
