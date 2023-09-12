from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='标题',max_length=32)

    def __str__(self):
        return self.title
class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name='姓名',max_length=32)
    pwd = models.CharField(verbose_name='密码',max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    # creat_data = models.DateTimeField(verbose_name='入职时间',auto_now=True)
    creat_data = models.DateField(verbose_name='入职时间',auto_now=True)

    # depart = models.ForeignKey(to = 'Department',to_field='id',on_delete=models.CASCADE)
    #第一个to 与表关联  第二个to 与表中的列关联  ForeignKey列名后自动加关联的_名字
    # on_delete = models.CASCADE 若部门被删除 级联删除

    depart = models.ForeignKey(verbose_name='部门',to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    # 若部门被删除 置空删除（不删，职位变为空）  null=True, blank=True, on_delete=models.SET_NULL
    gender_choices = (
        (1,'男'),
        (2,'女')
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

class PrettyNum(models.Model):
    '''靓号管理'''
    mobile = models.CharField(verbose_name='手机号',max_length=11)
    price = models.IntegerField(verbose_name='价格',)
    level_choices =(
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
        (5,'5级')
    )
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choices,default=1)
    statues_choices=(
        (1,'已占用'),
        (2,'未占用')
    )
    statues = models.SmallIntegerField(verbose_name='状态',default=2,choices=statues_choices)

class Admin(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)