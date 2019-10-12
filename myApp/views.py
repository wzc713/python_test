from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return  HttpResponse("wzc is a good man")
#num接受请求url地址的值
def detail(request,num):
    return  HttpResponse('detail-%s' % num)
from myApp.models import Grades,Students
def grade(request):
    gra=Grades.objects.all()
    context={
        'grades':gra
    }
    return  render(request,'myApp/grades.html',context)
def student(request):
    stu=Students.stuobj2.all()
    context={
        'students':stu
    }
    return render(request, 'myApp/students.html', context)
#点击班级显示学生  num接受班级id
def gradesstudents(request, num):
    ''' 函数功能 '''
    gra=Grades.objects.get(pk=num)
    stulist=gra.students_set.all()
    context={
        'students':stulist
    }
    return render(request,'myApp/students.html',context)
def addstudent(request):
    gra=Grades.objects.get(pk=1)
    #调用类里面重写的类方法生成学生对象
    stu=Students.createstudent('迪丽热巴',18,410225,gra)
    #调用自定义管理器中添加的一个方法生成学生对象
    stu1=Students.stuobj2.createstudent('迪丽热巴1',18,410225,gra)
    print('stu:%s----stu1:%s' % (stu,stu1))
    #stu.save()
    return  HttpResponse("ADD OK")

#分页显示学生http://127.0.0.1:8000/stu/3/
def stupage(reuqest, page):
    ''' 注释 '''
    #0-5  5-10  10-15
    #1      2     3
    #每页显示两条记录
    page1=int(page)
    stulist=Students.stuobj2.all()[(page1-1)*2:page1*2]
    context = {
        'students': stulist
    }
    return render(reuqest, 'myApp/students.html',context)
#获取GET传递的参数http://127.0.0.1:8000/getdata/?a=1&b=2
def getdata(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    return  HttpResponse('a=%s     b=%s'  % (a,b))
#获取GET传递的参数http://127.0.0.1:8000/getdata/?a=1&a=2
def getdatas(request):
    a=request.GET.getlist('a')
    a1=a[0]
    a2=a[1]
    return  HttpResponse(a1+"    "+a2)
def postdata(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    password = request.POST.get('password')
    context = {
    'dict':{
        'name':name,
        'gender':gender,
        'hobby':hobby,
        'password':password
    }

    }
    return render(request, 'myApp/showdata.html', context)
def regist(request):
    return render(request, 'myApp/regist.html')
def requestdata(request):

    path=request.path
    method=request.method
    encoding=request.encoding
    get=request.GET
    post=request.POST
    files=request.FILES
    cook=request.COOKIES
    host=request.get_host
    session=request.session
    print(path,method,encoding, get, post, files)
    return HttpResponse(path)


def showresponse(request):

    res = HttpResponse()
    res.content = 'wzc good'
    context = {
        'dict':{
            'content':res.content,
            'charset':res.charset,
            'status_code':res.status_code,

        }
    }
    return render(request, 'myApp/showdata.html', context)
def cookiestest(request):
    res = HttpResponse()
    cook = res.set_cookie('name','tongliya')
    res.write('cookies:    '+request.COOKIES['name'])
    return res
from django.http import JsonResponse
def jsontest(request):
    if request.is_ajax():
        res=JsonResponse({'name':'tongliya' })
        return res
    else:
        res = JsonResponse({'name': 'tongliya'})
        return res
def main(request):
    ''' 登录主页，判断是否登录 '''
    name = request.session.get('name', default='游客')
    context = {
        'name':name
    }
    return render(request, 'myApp/main.html', context)
def login(request):
    return render(request, 'myApp/login.html')
from django.shortcuts import redirect
def showmain(request):
    name = request.POST.get('username')
    request.session['name'] = name
    request.session.set_expiry(50)#s设置50秒过期
    return  redirect('/main/')

from django.contrib.auth import logout

def quit(request):
    #request.session.clear()
    #request.session.flush()
    logout(request)
    return redirect('/main/')
