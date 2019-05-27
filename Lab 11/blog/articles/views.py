#coding:utf-8
from models import Article
from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User,check_password

def archive(request):
	return render (request,'archive.html',{"posts":Article.objects.all()})

def get_article(request,article_id):
	try:
		post=Article.objects.get(id=article_id)
		return render(request,'article.html',{"post":post})
	except Article.DoesNotExist:
		raise Http404

def create_post(request):
	if not request.user.is_anonymous():
		if request.method == "POST":
			# обработать данные формы, если метод POST
			form = {
				'text': request.POST["text"],
				'title': request.POST["title"]
			}
			# в словаре form будет храниться информация, введенная пользователем
			if form["text"] and form["title"]:
				# если поля заполнены без ошибок
				try:					
					# если введено уже имеющееся в БД название статьи
					art_title=Article.objects.get(title=form["title"])
					form['errors'] = u"Статья с таким названием уже существует".encode('1251')
					return render(request, 'create_post.html', {'form': form})

				except Article.DoesNotExist:					
					# создать пост и перейти на его страницу
					art=Article.objects.create(text=form["text"], 
											   title=form["title"], 
											   author=request.user)
					return redirect('get_article',article_id=art.id)  

			else:
				# если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены".encode('1251')
				return render(request, 'create_post.html', {'form': form})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'create_post.html', {})
	else:
		raise Http404

def reg (request):
	if not request.user.is_anonymous():
		if request.method == "POST":
			# создать пользователя, если метод POST
			new_user = {
				'login': request.POST["login"],
				'email': request.POST["email"],
				'password':request.POST["password"]
			}
			# в словаре new_user будет храниться информация, введенная пользователем
			if new_user["login"] and new_user["password"]:
				# если поля заполнены без ошибок
				try:					
					# если введённый логин уже существует, то пользователя перенаправят на страницу авторизации
					er_user=User.objects.get(username=new_user["login"])
					new_user['errors'] = u"Пользователь с таким логином уже существует".encode('1251')
					return redirect('auth')

				except User.DoesNotExist:					
					# создаёт нового пользователя и перенаправляет его на общую страницу статей
					user=User.objects.create_user(new_user["login"], new_user["email"], new_user["password"])
					return redirect('archive')  

			else:
				# если введенные данные некорректны
				new_user['errors'] = u"Не все обязатаельные поля заполнены".encode('1251')
				return render(request, 'reg_new.html', {'form': new_user})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'reg_new.html', {})
	else:
		raise Http404

def auth (request):
	if not request.user.is_anonymous():
		if request.method == "POST":
			# авторизация пользователя, если метод POST
			auth_user = {
				'login': request.POST["login"],
				'password':request.POST["password"]
			}
			# в словаре auth_user будет храниться информация, введенная пользователем
			if auth_user["login"] and auth_user["password"]:
				try:
					Log=User.objects.get(username=auth_user["login"])
					if check_password(auth_user["password"],Log.password):
						# если поля заполнены без ошибок то пользователь будет авторизован и перенаправлен на общую страницу статей
						user = authenticate(username=auth_user["login"], password=auth_user["password"])
						login(request, user)
						return redirect('archive')
					else:
						auth_user['errors'] = u"Вы ввели неверный пароль".encode('1251')
						return render(request,'auth.html',{'form':auth_user})
						
				except User.DoesNotExist:
					auth_user['errors'] = u"Вы ввели неверный логин".encode('1251')
					return render(request,'auth.html',{'form':auth_user})
			else:
				# если введенные данные некорректны
				auth_user['errors'] = u"Не все обязатаельные поля заполнены".encode('1251')
				return render(request, 'auth.html', {'form': auth})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'auth.html', {})
	else:
		raise Http404