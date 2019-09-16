from django.conf.urls import url
from . import views
app_name='myapp'
urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)/$',views.detail),
    url(r'^grades/$',views.grade),
    url(r'^students/$',views.student),
    url(r'^grades/(\d+)/$',views.gradesstudents),
    url(r'^addstudent/$',views.addstudent),
    url(r'^stu/(\d+)/$',views.stupage),
    url(r'^requestdata/$',views.requestdata),
    url(r'^getdata/$',views.getdata),
    url(r'^getdatas/$',views.getdatas),
    url(r'^postdata/$',views.postdata),
    url(r'^regist/$',views.regist),
    url(r'^showresponse/$',views.showresponse),
    url(r'^cookiestest/$',views.cookiestest),
    url(r'^jsontest/$',views.jsontest),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit)

]