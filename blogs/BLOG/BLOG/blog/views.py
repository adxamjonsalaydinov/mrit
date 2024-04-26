from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Comment, BlogCategory
from .forms import ContactForm
from django.shortcuts import HttpResponseRedirect, redirect



def home(request):
    blogs = Blog.manager.all()
    count_blog = blogs.count()
    if count_blog > 4:
        blogs = blogs[count_blog-4:]
    context = {
        "blog": blogs
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def blog(request):
    blogs = Blog.manager.all()
    return render(request, "blog.html", {"blogs":blogs})


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.save()
            return redirect('contact_page')
    return render(request, "contact.html", {'contact_form': contact_form})


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    blog_comments = blog.comments.filter(status=True)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.post = blog
            form.save()
            return HttpResponseRedirect("/" + str(blog.id))
    else:
        comment_form = CommentForm()
    return render(request, "single.html", {"blogd":blog, "blog_comment":blog_comments, "comment_form": comment_form})




def category_view(request, *args, **kwargs):
    category = kwargs['category']
    blogs = Blog.objects.filter(category__name=category)
    return render(request, 'category.html', {"blogs": blogs})


def categories(request):
    category_objs = BlogCategory.objects.exclude(name='default')
    context = {
        "category_objs": category_objs
    }
    return context