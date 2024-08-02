from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, LikeDislike
from .forms import CommentForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    likes = post.likes_dislikes.filter(is_like=True).count()
    dislikes = post.likes_dislikes.filter(is_like=False).count()

    if request.method == 'POST':
        if 'comment_form' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        elif 'like' in request.POST or 'dislike' in request.POST:
            is_like = 'like' in request.POST
            LikeDislike.objects.update_or_create(
                post=post,
                user=request.user,
                defaults={'is_like': is_like},
            )
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'likes': likes,
        'dislikes': dislikes,
    })
