from django.db import models

# Create your models here.

#�¼���
class Event(models.Model):
    name = models.CharField(max_length=100) # �¼��ı���
    realname = models.CharField(max_length=64) # ����
    reason = models.CharField(max_length=128) #���ԭ��
    days = models.CharField(max_length=128) #�������
    start_time = models.DateTimeField('start time') #��ٿ�ʼʱ��
    end_time = models.DateTimeField('end time') #��ٽ���ʱ��
    def __str__(self):
        return self.realname

#��Ա��
# class Guest(models.Model):
#     event = models.ForeignKey(Event)# �����¼� id
#     realname = models.CharField(max_length=64) # ����
#     reason = models.CharField(max_length=128) #���ԭ��
#     days = models.CharField(max_length=128) #�������
#     start_time = models.DateTimeField('start time') #��ٿ�ʼʱ��
#     end_time = models.DateTimeField('end time') #��ٽ���ʱ��
#     class Meta:
#         unique_together = ("event", "realname")
#
#     def __str__(self):
#         return self.realname