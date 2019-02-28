from django.db import models

# Create your models here.
class User(models.Model):

    uname = models.CharField(max_length=50,unique=True)
    upassword = models.CharField(max_length=255)
    utoken = models.CharField(max_length=255)

    uemail = models.CharField(max_length=50,unique=True)

    uFirstTime = models.DateTimeField(auto_now=True)
    uLastTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '用户名:{}-用户邮箱:{}-创建时间:{}-最后修改时间:{}'.format(self.uname,self.uemail,self.uFirstTime,self.uLastTime)

    class Meta:
        db_table = 'user'