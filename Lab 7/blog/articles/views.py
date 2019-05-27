#coding:utf-8
from models import Article
from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse

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

	
