from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.urls import reverse_lazy
from .forms import FeedbackForm, AddInkForm, EditInkForm
from .models import Post, Category

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "feedback_form": FeedbackForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        feedback_form = FeedbackForm(data=request.POST)

        if feedback_form.is_valid():
            feedback_form.instance.email = request.user.email
            feedback_form.instance.name = request.user.username
            comment = feedback_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            feedback_form = FeedbackForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "feedback_form": FeedbackForm(),
            },
        )


class InkLike(View):
    """
    Allows user to like and unlike posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CategoryListView(generic.ListView):
    """
    Create a category object for users to 
    categorize their posts
    """
    template_name = 'category.html'
    context_object_name = 'categorylist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']),
        }
        return content


def category_list(request):
    """
    Creates a list of all available
    categories to allow user to 
    browse through them
    """
    category_list = Category.objects.exclude(name='uncategorized')
    context = {
        "category_list": category_list,
    }
    return context


class AddInkPost(CreateView):
    """
    A class for authorised users to create and
    post an Ink post
    """
    model = Post
    template_name = 'add_post.html'
    form_class = AddInkForm
    success_url = reverse_lazy('home')


class UpdateInkView(UpdateView):
    """
    Allows users to update their posts
    """
    model = Post
    template_name = 'update_post.html'
    form_class = EditInkForm
    success_url = reverse_lazy('home')
