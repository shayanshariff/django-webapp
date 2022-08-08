from django.shortcuts import render

posts = [
    {
        'author': 'ShayanS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 5, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 8, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
