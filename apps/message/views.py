# coding:utf-8
from django.shortcuts import render
# import MySQLdb

# Create your views here.


def getform(request):
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

