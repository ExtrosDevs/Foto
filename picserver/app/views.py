
from django.http.response import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from datetime import datetime
from picserver.settings import EMAIL_HOST_USER
from .models import Image, User, Chat, ChatImage,Tag
from django.core.mail import send_mail;
import random
from cryptography.fernet import Fernet
from django.db.models import Q

from .form import userForm, userLoginForm

import numpy as np
# Create your ssviews here.


def sendEmail(request):
    send_mail('aaa','hi',EMAIL_HOST_USER, ['wisamabady7@gmail.com'])
    

    return HttpResponseRedirect('app/')
def appi(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            if datetime.now().minute < User.objects.get(userName = request.session['user']).createdDate.minute + 3:
                # return render(request , "index.html", {'time':User.objects.get(userName = 'ahmad').createdDate.minute + 3, 'datetime': datetime.now().minute})
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        form = userForm()
        return render(request , "index.html", {'data' : 'not created' , 'form':form,'time':User.objects.get(userName = request.session['user']).createdDate.minute + 3, 'datetime': datetime.now().minute})




def api(request):
    ob = User.objects.get(userName='ahmad')
    data = {
        'username':'omar'
    }
    
    return JsonResponse(data)



def Home(request):
    data = None
    user = None
    if request.session.get('userName', None):
        user = User.objects.get(userName = request.session['userName'])
        tags = user.tagsLike.all()
        ls = None
        if tags.exists():
            imagesByTag = Image.objects.filter(tags__in= tags)

            ls = np.array(imagesByTag.values_list('id'))
            np.random.shuffle(ls)
            ls = ls[:4]
        else :
            ls = np.array([[1]])
            images = Image.objects.all().values_list('id')
            arr = np.array(images)
            np.random.shuffle(arr)
            ls = arr[:5]
     
        imagesByLikes = Image.objects.all().order_by('-likes')
        lst = np.array(imagesByLikes.values_list('id'))
        np.random.shuffle(lst)
        ls = np.concatenate([ls, lst[:5]], axis=0)

        imagesByDate = Image.objects.order_by('-imageDate')
        lst = np.array(imagesByDate.values_list('id'))[:7]
        np.random.shuffle(lst)
        ls = np.concatenate([ls, lst[:5]], axis=0)


        imagesByFollowing = Image.objects.filter(user__id__in=user.following.values_list('id')).order_by('-imageDate')

        lst = np.array(imagesByFollowing.values_list('id'))[:7]
        np.random.shuffle(lst)
        ls = np.concatenate([ls, lst[:5]], axis=0)

        ls= np.unique(ls)
        data = Image.objects.filter(id__in=ls)
   
    else:
        images = Image.objects.all().values_list('id')
        arr = np.array(images)
        np.random.shuffle(arr)
        imgs = Image.objects.filter(id__in=arr[:15])
        data = imgs
    if request.method=='GET':
        if request.GET.get('search'):  
            ser = request.GET['search'].strip()
            imgs = Image.objects.all()
            tags = Tag.objects.filter(tagName__contains=ser)
            imgs = imgs.filter(tags__in=tags)
            return render(request, 'index.html', {'data':imgs, 'user':user})
    ourpicks = Image.objects.filter(inOurPicks=True)
    return render(request, 'index.html', {'data':data,  'ourpicks':ourpicks, 'user':user})

def userProfile(request, username):
    print('ss')
    user = User.objects.filter(userName = username)
    if user.exists():
        return render(request, 'profile.html', {'user':user[0]})
    else :
        HttpResponseRedirect('/')


def imageView(request, id):
    image = Image.objects.get(id=id)
    if request.session.get('userName'):
        user = User.objects.get(userName=request.session['userName'])
        user.tagsLike.add(*image.tags.all())
        user.save()

    return render(request, 'photo.html', {'img':image})


def register(request):
   
    if request.method == 'POST':
        form = request.POST
        if form.get('register'):
            isUserExists = User.objects.filter(userName = form.cleaned_data['userName'].strip()).exists()
            isEmailExists = User.objects.filter(userEmail = form.cleaned_data['userEmail'].strip()).exists()
            if isUserExists or isEmailExists:
                err = ''
                if isUserExists:
                    err +='username, '

                if isEmailExists:
                    err += 'email'
                return render(request, 'login.html' ,{'form':form, 'error':'the'+err+'is already exists'})
            if form['password'] != form['passwordconf']:
                 return render(request, 'login.html' ,{'form':form, 'error':'password not match '})
            else:
                request.session['username'] = form['name']
                request.session['email'] = form['email']
                request.session['password'] = form['password']
                code = ''
                for i in range(6):
                    code += str(random.randrange(0,10))
                request.session['codeAct'] = code
                print(request.session['password'])
                # request.session.save()
                send_mail('CodeActivate of your account is',code ,EMAIL_HOST_USER, [form.cleaned_data['userEmail']])
                return HttpResponseRedirect('../activate/')

    else:     
        form =userForm()
    return render(request, 'register.html' ,{'form':form})
def login(request):
       
    if request.method == 'POST':
        form = request.POST
        if form.get('login'):
            user =  User.objects.filter(userEmail =  form['email'].strip())
            if user.exists():
                if  form['password'] == user[0].userPassword:
                    print('login ')
                    request.session['userEmail'] = user[0].userEmail
                    request.session['userName'] = user[0].userName
                    user[0].userstatus = True
                    user[0].save()
                    return HttpResponseRedirect('/')
        if form.get('forgetpass'):
            user =  User.objects.filter(userEmail =  form['email'].strip())
            if user.exists():
                send_mail('change password', 'not supported yet',EMAIL_HOST_USER, [user[0].userEmail])
                
    return render(request, 'login.html' )
def logout(request):
    user = User.objects.get(userName= request.session['userName'])
    request.session['userEmail'] = ''
    request.session['userName'] = ''
    user.userstatus = False
    return HttpResponseRedirect('/')
def activate(request):
    if request.session['codeAct'] == '':
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        if code.strip() == request.session['codeAct'].strip():
            obj = User()
            obj.userName = request.session['username']
            obj.userEmail = request.session['email']
            obj.userPassword = request.session['password']
            obj.emailActvate = True;
            obj.save()
            request.session['codeAct'] = ''
            print('created it sucssfuly ')
            send_mail('your account is created ','welcome' ,EMAIL_HOST_USER, [request.session['email']])
            return HttpResponseRedirect('/')
    return render (request, 'activateEmail.html')

def dashBoard(request):
    if request.session.get('userName', None):
        user = User.objects.get(userName=request.session['userName'])
        chats = user.chats.all()
        print(chats)
        return render(request,'dashBoard.html', {'user':user, 'chats':chats})
    return HttpResponseRedirect('/')
def pro(request):
    return render(request, 'Pro.html')
def addImage(request):
    if request.session.get('userName', None):
        user = User.objects.get(userName=request.session['userName'])
        if request.method == "POST":
            form = request.POST
            file = request.FILES
            if file['image'].size >3000000:
                return render(request, 'upload.html', {'err':"image size must be less than 3MB"})
            if form.get('imageForm') :
                imgs = Image.objects.filter(image='publicImages/'+file['image'].name)
                if not imgs.exists():
                    image = Image()
                    image.user =user
                    image.imageTitle = form['title']
                    image.image = file['image']
                    image.imageDesc = form['desc']
                    Tags = Tag.objects.filter(tagName__in=form['tags'].split('#'))

                    image.save()
                    image.tags.add(*Tags.all())
            
            return HttpResponseRedirect('/')
        return render(request, 'upload.html')

    else:
        return HttpResponseRedirect('/')

# chat code
def chatGen(request,username):
    if  request.session.get('userName', None) :
        users = User.objects.filter(userName__in=[request.session['userName'], username])

        chats = Chat.objects.filter(users=users.first()).filter(users=users.last())
        print(chats)

        if chats.exists():
            return HttpResponseRedirect('../chat/'+str(chats[0].id))
        else:
            chat = Chat()
            chat.users.add(*users)
            chat.save()
            user1 = User.objects.get(userName=username)
            user2 = User.objects.get(userName=request.session['userName'])
            user1.chats.add(chat)
            user2.chats.add(chat)
            user1.save()
            user2.save()
        return HttpResponseRedirect('../chat/'+str(chat.id))
    
    return HttpResponseRedirect('../login/')
def chatView(request, id):
    if request.session.get('userName', None):
        user = User.objects.get(userName=request.session['userName'])
        chats = user.chats.all()
        if chats.filter(id=id).exists() :
            return render(request, 'chat.html', {'ID':id})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

# apis
def requestDataJson(request,id):
    if request.session.get('userName', None):
        user = User.objects.get(userName=request.session['userName'])
        chats = user.chats.all()
        if  chats.filter(id=id).exists():
            chat = Chat.objects.get(id=id)
            return JsonResponse(chat.chat, safe=False)
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

def responseDataJson(request, id):
    if request.method == 'POST':
        if request.session.get('userName', None):
            chat = Chat.objects.get(id=id)
            print(chat)
            if request.FILES :
                file =request.FILES['file']
                if file.size < 4000000 and (file.name.endswith('.png') or file.name.endswith('.jpg')):
                    img = ChatImage()
                    img.image =request.FILES['file']
                    img.user = User.objects.get(userName = request.session['userName'])
                    img.save()
                    chat.chat.append({"massage":{"user":request.session['userName'], "contentImage":str(request.FILES['file'])}})
                    chat.save()
            if request.POST['text'] != '':
                
                chat.chat.append({"massage":{"user":request.session['userName'], "content":request.POST['text']}})
                chat.save()
            # print(request.FILES['file'])
            print(request.POST['text'])
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/')


def imageApi(request):
    images = []
    for i in Image.objects.all():
        images.append({'id':i.id,'img':i.image.url})
    return JsonResponse(images, safe=False)
def imageResponse(request, id):
    if request.is_ajax:
        if request.session['userName']:
            o = Image.objects.get(id=id)
            # user= User.objects.get(userName= request.session['userName'])
            
            if {'user':request.session['userName']} not in o.usernameLikes:
                o.likes+=1
                o.usernameLikes.append({'user':request.session['userName']})
            else:
                o.likes-=1
                o.usernameLikes.remove({'user':request.session['userName']})
            o.save()

    return HttpResponseRedirect('/')
def resLike(request, id):
    image = Image.objects.get(id=id)
    print('s')
    return JsonResponse({'likes':image.likes})
