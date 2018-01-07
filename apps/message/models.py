# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 继承于django.db.models.Model
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, max_length=50,default="", verbose_name="主键")
    # 设置最大长度，verbose_name在后台显示字段会用到
    name = models.CharField(max_length=20,null=True,blank=True,default="", verbose_name=u"用户名")
    # Django提供内置的邮箱字段会帮忙验证` default_validators = [validators.validate_email]`
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"

        # 指明复数信息，否则后台显示"用户留言s"
        verbose_name_plural = verbose_name

        # 这里我们让它自动生成所以不用指定db-table
        # db_table = user_message

        # ordering指定默认排序字段,如：
        # ordering = ['-object_id']







