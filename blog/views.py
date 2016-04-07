from django.views import generic
from models import Blog
from django.utils import timezone


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
        ).order_by('-published_date')[:5]


class ContentView(generic.DetailView):
    model = Blog
    template_name = 'blog/content.html'
    context_object_name = 'blog'

    def get_queryset(self):
        """
        Excludes any blogs that aren't published yet.
        """
        return Blog.objects.filter(published_date__lte=timezone.now())
