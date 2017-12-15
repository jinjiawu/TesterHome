from django.db import models

# Create your models here.

#事件表
class Event(models.Model):
    name = models.CharField(max_length=100) # 事件的标题
    realname = models.CharField(max_length=64) # 姓名
    reason = models.CharField(max_length=128) #请假原因
    days = models.CharField(max_length=128) #请假天数
    start_time = models.DateTimeField('start time') #请假开始时间
    end_time = models.DateTimeField('end time') #请假结束时间
    def __str__(self):
        return self.realname

#人员表
# class Guest(models.Model):
#     event = models.ForeignKey(Event)# 关联事件 id
#     realname = models.CharField(max_length=64) # 姓名
#     reason = models.CharField(max_length=128) #请假原因
#     days = models.CharField(max_length=128) #请假天数
#     start_time = models.DateTimeField('start time') #请假开始时间
#     end_time = models.DateTimeField('end time') #请假结束时间
#     class Meta:
#         unique_together = ("event", "realname")
#
#     def __str__(self):
#         return self.realname