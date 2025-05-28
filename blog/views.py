from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def index(request):
    posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/author_detail.html', {
        'author': author,
        'posts': posts
    })

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/tag_post.html', {'tag': tag, 'posts': posts})
