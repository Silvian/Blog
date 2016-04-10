from django.views import generic
from models import Blog, Comment
from django.utils import timezone
from .forms import CommentForm
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')[:5]


class ListView(generic.ListView):
    template_name = 'blog/list.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')


class ContentView(generic.DetailView):
    model = Blog
    template_name = 'blog/content.html'
    context_object_name = 'blog'

    def get_queryset(self):
        """
        Excludes any blogs that aren't published yet.
        """

        return Blog.objects.filter(published_date__lte=timezone.now())


class CommentFormView(generic.FormView, generic.DetailView, generic.base.ContextMixin):
    model = Blog
    template_name = 'blog/comment_post.html'
    form_class = CommentForm
    success_url = 'blog/'
    context_object_name = 'blog'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('blog/content')

    def get_queryset(self):
        """
        Excludes any blogs that aren't published yet.
        """
        return Blog.objects.filter(published_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        """
        Call the base implementation first to get a context
        """
        context = super(CommentFormView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(blog_id=self.kwargs['pk']).order_by('-published_date')
        return context

