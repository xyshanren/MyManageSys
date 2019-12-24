from django.db import models

# Create your models here.


class Students(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='入学时间')
    remarks = models.TextField(verbose_name='备注', blank=True)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.name
