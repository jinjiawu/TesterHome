# -*- coding:utf-8 -*-
from django.http import JsonResponse
from vacate.models import Event
from django.core.exceptions import ValidationError


def add_event(request):
    eid = request.POST.get('eid','') # 请假 id
    name = request.POST.get('name','') # 请假类型
    realname = request.POST.get('realname','') # 谁请的假
    reason = request.POST.get('status','') # 请假原因
    days = request.POST.get('address','') # 请假天数
    start_time = request.POST.get('start_time','') # 请假开始时间
    end_time = request.POST.get('start_time','') # 请假结束时间

    if eid == '' or name == '' or realname == '' or reason == '' or days == '' or start_time == '' or end_time == '':
        return JsonResponse({'status':10021,'message':'parameter error'})

    result = Event.objects.filter(id = eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})

    result = Event.objects.filter(name = name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists'})

    try:
        Event.objects.create(id=eid,name=name,realname=realname,
                             reason=reason,days=days,start_time=start_time,
                             end_time=end_time)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})
    return JsonResponse({'status':200,'message':'add event success'})