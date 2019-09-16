#生成管理账户
#python manage.py createsuperuser,然后输入用户名和密码
from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#添加班级的时候附带增加两名学员
class StudentsInfo(admin.TabularInline):
    model=Students
    extra = 2
#设置学生显示页面
class GradesAdmin(admin.ModelAdmin):
    #调用增加班级同时增加两名学生的类
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gname','gnum','createtime','isdelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page =5
    # #添加修改页属性
    # 规定显示顺序fields和fieldsets不能同时使用
    #fields = ['gnum','gname','createtime','isdelete']
    # 分组显示
    fieldsets = [
        ('数据项',{'fields':['gname','gnum']}),
        ('时间项',{'fields':['isdelete']})
    ]
#注册班级
admin.site.register(Grades,GradesAdmin)


#设置学生显示页面
#使用装饰器完成注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    #封装bool值返回有效和删除
    def isdel(self):
        if self.isdelete:
            return '删除'
        else:
            return  '有效'
    #设置列名显示
    isdel.short_description = '是否删除'

    #列表页属性
    list_display = ['pk','sname','sage','scard','createtime','lasttime','gradeid',isdel]

    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page =5
    # #添加修改页属性
    # 规定显示顺序fields和fieldsets不能同时使用
    #fields = ['gnum','gname','createtime','isdelete']
    # 分组显示
    fieldsets = [
        ('数据项',{'fields':['sname','sage','scard']}),
        ('时间项',{'fields':['gradeid','isdelete']})
    ]
#注册学生页面
#admin.site.register(Students,StudentsAdmin)使用类装饰器替换注册@admin.register(Students)
