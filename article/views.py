from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {"articles" : articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article Uploaded")
        return redirect("dashboard")
    return render(request, "addarticle.html", {"form":form})

def about(request):
    return render(request, "about.html")
#dinamik url
def detail(request, id):
    return HttpResponse("Detail:" + str(id))

def addcomment(request, id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        new_comment = Comment(comment_author = comment_author, comment_content = comment_content)
        new_comment.article = article
        new_comment.save()

    return redirect(reverse('article:article', kwargs={"id":id}))    

def article(request, id):
    #article = Article.objects.filter(id = id)
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()
    context = {"article" : article, "comments":comments
    }
    return render(request, "article.html", context)
@login_required(login_url="user:login")
def deletearticle(request, id):
    article = Article.objects.filter(id = id)
    article.delete()
    return redirect("dashboard")

@login_required(login_url="user:login")
def updatearticle(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article Updated Succesfully")
        return redirect("dashboard")
    return render(request, "update.html", {"form":form})

def article_show(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"article_show.html", {"articles": articles})
    articles = Article.objects.all()
    context = {"articles" : articles
    }
    return render(request, "article_show.html", context)