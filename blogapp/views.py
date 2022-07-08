from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from blogapp.forms import CommentForm
from blogapp.models import Post, Comments


class PostList(ListView):
    model = Post
    template_name = 'blogapp/index.html'


class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'blogapp/single.html'
    form_class = CommentForm

    def get_object(self, queryset=None):
        return Post.objects.get(id=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        context['post_list_detail'] = Post.objects.all().order_by("?")[:4]
        context['com'] = Comments.objects.filter(post=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        p = self.get_object()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = p
            obj.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetail, self).form_valid(form)
