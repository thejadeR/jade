from .models import *
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .gen_code import generate_code
import random
import os
from jadejade.settings import BASE_DIR
import time
import hashlib

from .logic import *
# Create your views here.
def index(request):
    # 获取用户信息
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
        # data['uemail'] = u.uemail
        # data['uFirstTime'] = u.uFirstTime

    return render(request,'index.html', context=data)

# def index(request):
#
#     return render(request,'index.html')


def generate_token():
    token = str(time.time()) + str(random.random())
    mymd5 = hashlib.md5()
    mymd5.update(token.encode('utf-8'))
    return mymd5.hexdigest()


def generate_psword(password):
    mymd5 = hashlib.md5()
    mymd5.update(password.encode('utf-8'))
    return mymd5.hexdigest()

# 注册
def sign_up(request):
    if request.method == 'GET':
        return render(request,'sign_up.html')

    elif request.method == 'POST':

        uemail = request.POST.get('uemail')
        uname = request.POST.get('uname')
        upassword = request.POST.get('upassword')

        u = User()

        u.uemail = uemail
        u.uname = uname
        u.upassword = generate_psword(upassword)
        u.utoken = generate_token()

        u.save()
        request.session['utoken'] = u.utoken

        # request.session.set_expiry(3600)
        # response.set_cookie('uname', u.db_uname)
        response = redirect('mtwSite:userdetail')

        return response

def check_email(request):
    # 邮箱
    email = request.GET.get('email')

    users = User.objects.filter(uemail=email)
    if users.exists():
        return JsonResponse({'msg': '邮箱已被占用!', 'returnCode': 0})
    else:
        return JsonResponse({'msg': '邮箱可以使用!', 'returnCode': 1})

def check_name(request):
    # 邮箱
    name = request.GET.get('name')

    users = User.objects.filter(uname=name)
    if users.exists():
        return JsonResponse({'msg': '用户名已被占用!', 'returnCode': 0})
    else:
        return JsonResponse({'msg': '用户名可以使用!', 'returnCode': 1})


imgcode = ''
imgname = ''
def get_code(request):
    global imgcode, imgname

    if imgname == '':
        pass
    else:
        path3 = os.path.join(BASE_DIR,'static/img/'+imgname+'.png')
        if os.path.exists(path3):
            os.remove(path3)

    res = generate_code('code'+ str(random.randint(1000,9999)))
    imgcode = res[0]
    imgname = res[1]

    print(imgcode)
    return JsonResponse({'imgcode': imgcode, 'returnCode': 1,'imgname': imgname})


def check_code(request):
    # 邮箱
    imgcode2 = request.GET.get('imgcode')

    # print(imgcode)
    # print(imgcode2)
    if imgcode.lower() == imgcode2.lower():
        return JsonResponse({'msg': '', 'returnCode': 1})
    else:
        return JsonResponse({'msg': '验证码不正确', 'returnCode': 0})





def sign_in(request):

    if request.method == 'GET':
        return render(request, 'sign_in.html')

    elif request.method == 'POST':
        uname = request.POST.get('uname')
        upassword = request.POST.get('upassword')
        # print(generate_psword(upassword))
        # print(uname)
        try:
            # 不存在，会抛出异常
            # 多个时，会抛出异常　【uname是唯一约束】

            user = User.objects.get(uname=uname)
            if user.upassword == generate_psword(upassword):
                print('111')
                user.utoken = generate_token()
                user.save()
                print('222')
                request.session['utoken'] = user.utoken
                return redirect('mtwSite:userdetail')
            else:
                return render(request, 'sign_in.html', context={'err': '密码错误'})
        except:
            return render(request, 'sign_in.html', context={'err': '账号不存在'})




def userAgreement(request):
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
    return render(request,'userAgreement.html',context=data)


def siteNotice(request):
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
    return render(request,'siteNotice.html',context=data)


def aboutJadeJade(request):
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
    return render(request,'aboutJadeJade.html',context=data)


def helpCenter(request):
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
    return render(request,'helpCenter.html',context=data)


def userdetail(request):
    # 获取用户信息
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        data['uname'] = u.uname
        data['uemail'] = u.uemail
        data['uFirstTime'] = u.uFirstTime

    return render(request,'userdetail.html', context=data)


def logout(request):
    request.session.flush()
    return redirect('index.html')


def findpassword(request):
    return redirect('userdetail.html')


def modifypassword(request):
    return redirect('userdetail.html')


def modifyemail(request):
    # 邮箱
    uemail = request.POST.get('uemail')
    upassword = request.POST.get('upassword')

    # 获取用户信息
    utoken = request.session.get('utoken')
    data = {}
    if utoken:
        u = User.objects.get(utoken=utoken)
        upasswordReal = u.upassword
        upassword = generate_psword(upassword)
        if upasswordReal == upassword:
            u.uemail = uemail
            u.save()

            data['uname'] = u.uname
            data['uemail'] = u.uemail
            data['uFirstTime'] = u.uFirstTime
            return render(request, 'userdetail.html', context=data)
        else:
            return render(request,'userdetail.html')

    return render(request,'userdetail.html', context=data)


