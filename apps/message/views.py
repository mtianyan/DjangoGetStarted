# coding:utf-8
from django.shortcuts import render
# import MySQLdb
from .models import UserMessage
# Create your views here.


def getform(request):
    """
    :param request:
    :return: render后的HttpResponse
    """
    # 查询部分

    # UserMessage默认的数据管理器objects
    # 方法1 :all()是将所有数据返回成一个queryset类型(django的内置类型)
    # all_message = UserMessage.objects.all()

    # 方法2 :filter取出指定条件值，逗号代表and 必须同时满足两个条件才返回。
    all_message = UserMessage.objects.filter(name='mtianyan', address='西安')

    # 删除操作

    # all_message.delete()


    # 我们可以对于all_message进行遍历操作
    for message in all_message:
        message.delete()
        # 每个message实际就是一个UserMessage对象（这时我们就可以使用对象的相关方法）。
        print message.name

    # 存储部分

    # 首先实例化一个对象
    # user_message = UserMessage()

    # 为对象增加属性

    # user_message.name = "mtianyan2"
    # user_message.message = "blog.mtianyan.cn"
    # user_message.address = "西安"
    # user_message.email = "1147727180@qq.com"
    # user_message.object_id = "efgh"

    # 调用save方法进行保存
    # user_message.save()

    # html表单部分

    # 此处对应html中的method="post"，表示我们只处理post请求
    if request.method == "POST":
        # 就是取字典里key对应value值而已。取name，取不到默认空
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        # 实例化对象
        user_message = UserMessage()

        # 将html的值传入我们实例化的对象.
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "ijkl"

        # 调用save方法进行保存
        user_message.save()

    return render(request, 'message_form.html')


# # 使用原生sql获取书的列表
# def book_list(request):
#     # 创建到数据库的连接: 指明用户名，数据库，密码
#     db = MySQLdb.connect(user = 'me', db='mydb', passwd='secret', host='localhost')
#     # 创建一个游标对象执行器
#     cursor = db.cursor()
#     # 书写我们需要的sql语句
#     cursor.execute('SELECT name FROM books ORDER BY name')
#     # 对于fetchall()的结果做遍历，将遍历回来的结果当做数组，取第0个值name。
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()

