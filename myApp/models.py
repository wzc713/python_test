# 数据字段说明
# null=True如果为True，讲空值以NULL存储到数据库
# db_column='age'规定数据库字段名称
# blanke=True允许字段数据为空白
# db_index=True,为字段添加索引
# default=为字段设置默认值
# primary_key=True该字段会成为模型主键字段
# unique=True这个字段在表中必须有唯一值（唯一约束）
#
# 关系分类
# ForeignKey 一对多，将字段定义在多的端中
# ManyToManyField 多对多，将字段定义在两端中
# OnetoOneField 一对一，将字段定义在任意一端中
# 用一访问多
# 格式     对象.模型类小写_set    示例  grades.students_set
# 用一访问一
# 格式     对象.模型类小写        示例  grades.students
# 访问ID
# 格式     对象.属性_id            示例  student.gradeid_id
#
# 模型查询
# 1、调用过滤器方法获取查询集  .filter(name='')
# 2、查询集经过过滤器筛选后返回新的查询集.filter(name='').filter(pd=1)  支持链式调用
# 3、惰性执行   创建查询集不会带来任何数据库的访问，知道调用数据时，才会访问数据库
# 4、直接访问数据的情况    迭代    序列化    与if合用
# 5、返回查询集的方法称为过滤器  \
#     .all()
#     .filter(键=值，键=值)  效果等于  .filter(键=值).filter(键=值)
#     .exclude()   过滤掉符合掉件的数据
#     .order_by()  排序
#     .values()    一条数据就是一个对象（字典），返回一个列表[{'id'=1,'name'='佟丽娅''},{'id'=2,'name'='孟庭苇'}]
# 6、返回单个数据
#     .get()  返回一个满足条件的对象，如果没有找到符合条件的对象或者有多个对象模型类会引发错误
#     .count()返回查询集的对象个数
#     .first()返回查询集第一个对象
#     .last()返回查询集最后一个对象
#     .exists()判断查询集中是否有数据，有数据返回True没有返回False
# 7、返回指定条数查询集，分页
#     .all()[0:5]   使用下标的方式显示5条，下标不能是负数
#
# 字段查询
# 语法  属性名称_比较运算符=值   age__运算符=18  双下划綫
# 外键值   属性名称_id
# 转义     .filter(sname__contains='孙%') 相当于 where sname  like（'孙\%'）而不是where sname  like（'孙%'）
# 1、比较运算符
#     exact  判断，大小写敏感  .filter(isdelete=False)
#     contains  是否包含，大小写敏感   .filter(sname__contains='娅') 查找名字中有“娅”的
#     startswith  endswith  以value开头或结尾，大小写敏感 .filter(sname__startswith='孙')  查询名字以“孙”开头的
#     以上四个在前面加上i表示不区分大小写   iexact   icontains  istartswith  iendswith
#
#     isnull  isnotnull   判断是否为空  .filter(sname__isnull=False) 查找名字不为空的
#
#     in    判断是否在范围内   .filter(pk__in=[2,4,6]) 取出id是2,4,6的记录
#
#     gt  gte  大于  大于等于   .filter(sage__gt=30) 查找年龄大于30的
#     lt  lte  小于  小于等于
#
#     日期  year  month day  weekday   hour  minute second   .filter(createtime__year='2017')
#
#     跨关联查询,相当于sql的join  查询学生名字叫佟丽娅的学员的班级信息
#     Grades.objects.filter(students__sname__contains='佟丽娅')
#
#     查询快捷 pk代表主键，自动生成的主键默认为id
#
# 2、聚合函数
#     from django.db.models import Max,Count,Avg
#     使用aggregate函数返回聚合函数的值 .aggregate(Max(sage))获得年龄最大的值，而不是一条数据
#     Avg  平均值
#     Count
#     Max
#     Min
#     Sum
#
# 3、F对象
#     from django.db.models import F
#     可以使用模型的A属性与B属性进行比较
#     Grades.objects.filter(createtime__gte=F('lasttime')) 查找创建时间大于等于修改时间的班级
#     支持F对象的算术运算
#     Grades.objects.filter(createtime__gte=F('lasttime')+timedelta(days=3)) 查找创建时间大于修改时间加上3天的班级
#
#
# # 普通方式
# reporter = Reporters.objects.get(name='Tintin')
# reporter.stories_filed += 1 # 放到内存中,使用python计算,然后通过save方法保存
# reporter.save()
#
# # 使用F表达式 (简单使用)
# from django.db.models import F
# reporter = Reporters.objects.get(name='Tintin')
# reporter.stories_filed = F('stories_filed') + 1
# reporter.save()不用再调用
# 虽然看上去和上面的内存Python操作相似,但事实上这是一个描述数据库操作的sql概念
# 当django遇到F()实例,它覆盖了标准的Python运算符创建一个封装的SQL表达式。
# 在这个例子中，reporter.stories_filed就代表了一个指示数据库对该字段进行增量的命令。
# 无论reporter.stories_filed的值是或曾是什么，Python一无所知--
# 这完全是由数据库去处理的。所有的Python，通过Django的F() 类，只是去创建SQL语法参考字段和描述操作
#
# 4、Q对象
#     from django.db.models import Q
#     过滤器的方法中的关键字参数，条件为or模式
#     进行or查询  Students.objects.filter(Q(pk__lte=3) | Q（sage__gte=18))获取id小于等于3，年龄大于等于18的学员
#     Students.objects.filter(~Q(pk__lte=3) ）加~线相当于取反

from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gnum=models.IntegerField()
    createtime = models.DateTimeField(auto_now_add=True)
    isdelete=models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table='grades'#设置生成表的名称
        ordering = ['id']  # 对象的默认排序字段，获取对象的列表时可以使用，如果降序使用['-id']，排序会增加数据库耗时

#自定义Manage模型管理器类,Manage时Django的模型与数据库交互的借口，可以定义多个模型管理器
#作用1：向管理器类中额外添加方法2:修改管理器返回的原始查询集(重写get_queryset())
class studentManage(models.Manager):
    #过滤掉被删除的数据
    def get_queryset(self):
        return  super(studentManage,self).get_queryset().filter(isdelete=False)
    #和在类里面的生成函数(Students.createstudent())效果相同，这个的调用方式是student.stuobj2.createstudent(name,age,card,gradeid)
    def createstudent(self,name,age,card,grade):
        student=self.model()
        student.sname=name
        student.sage=age
        student.scard=card
        student.gradeid=grade
        return student

class Students(models.Model):
    sname=models.CharField(max_length=5)
    sage=models.IntegerField()
    scard=models.CharField(max_length=18)
    createtime=models.DateTimeField(auto_now_add=True)
    lasttime=models.DateTimeField(auto_now=True)
    isdelete=models.BooleanField(default=False)
    #关联主键
    # 整理一下on_delete参数的各个值的含义:
    #
    # on_delete = None,  # 删除关联表中的数据时,当前表与其关联的field的行为
    # on_delete = models.CASCADE,  # 删除关联数据,与之关联也删除
    # on_delete = models.DO_NOTHING,  # 删除关联数据,什么也不做
    # on_delete = models.PROTECT,  # 删除关联数据,引发错误ProtectedError
    # # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete = models.SET_NULL,  # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    # on_delete = models.SET_DEFAULT,  # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    # on_delete = models.SET,  # 删除关联数据,
    # a.与之关联的值设置为指定值, 设置：models.SET(值)
    # b.与之关联的值设置为可执行对象的返回值, 设置：models.SET(可执行对象)
    gradeid=models.ForeignKey('Grades',on_delete=models.SET('班级删除'))
    def __str__(self):
        return  self.sname
    #元选项Meta
    class Meta:
        db_table='students'#设置生成表的名称
        ordering=['id']#对象的默认排序字段，获取对象的列表时可以使用，如果降序使用['-id'],排序会增加数据库耗时
    #自定义模型管理器student.object被sudent.stuobj代替，student.object中的object模型管理器就不再生成
    stuobj=models.Manager()
    stuobj2=studentManage()

    # 因为类Students类的父类已经使用__init__,在自定义的类中无法再使用,所以用函数重写
    @classmethod  #用类修饰方法，表示是一个类方法 ,cls参数就表示Students类
    def createstudent(cls,name,age,card,grade):
        student=cls(sname=name,sage=age,scard=card,gradeid=grade)
        return  student

