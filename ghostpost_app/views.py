
from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.forms import AddPost
from ghostpost_app.models import Post

# Create your views here.
def index_view(request):
    all_posts = Post.objects.filter().order_by('-id')
    return render(request, 'index.html', {'ghostpost_welcome': 'Welcome to my version of the Kenzie Academy Ghostpost assessment', 'all_posts': all_posts})


def boast_view(request):
    boast_posts = Post.objects.filter(post_type=True).order_by('-id')
    return render(request, 'boasts.html', {'boast_posts': boast_posts, 'boasts_title': 'Boasts!'})


def roast_view(request):
    roast_posts = Post.objects.filter(post_type=False).order_by('-id')
    return render(request, 'roasts.html', {'roast_posts': roast_posts, 'roasts_title': 'Roasts!'})


def votes_view(request):
    votes = sorted(Post.objects.all(), key=lambda votes: votes.count_votes)[::-1]
    return render(request, 'votes.html', {'votes': votes, 'votes_title': 'Sorted by your votes!'})


def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
              content=data.get('content'),
              post_type=data.get('post_type')
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddPost()
    return render(request, 'form.html', {'form': form, 'add_title': 'Add a post now!'})


def up_vote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def down_vote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))