from django.views.generic import (TemplateView,ListView,DetailView,CreateView,
                                  UpdateView, DeleteView)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from book_app.models import Blog,Comment
from .forms import PostForm, CommentForm

# Create your views here.
class IndexView(TemplateView):
  template_name = 'book_app/index.html'

class BlogListView(ListView):
  model = Blog
  ordering = ['-posted']

class BlogDetailView(DetailView):
  model = Blog

class CreatePostView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
  login_url = '/login/'
  redirected_field_name='book_app/blog_detail.html'
  form_class = PostForm
  model = Blog
  permission_required = 'book_app.add_blog'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'book_app/blog_detail.html'
  form_class = PostForm
  model = Blog

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model = Blog
  login_url = '/login/'
  success_url = reverse_lazy('book_app:blog_list')

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user


@staff_member_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog_pk = comment.blog.pk
    comment.delete()
    return redirect('book_app:blog_detail', pk=blog_pk)

@login_required
def add_comment_to_post(request, pk):
  blog = get_object_or_404(Blog, pk=pk)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.author = request.user
        comment.save()
        return redirect('book_app:blog_detail', pk=blog.pk)
  else:
    form = CommentForm()
  return render(request, 'book_app/add_comment_to_post.html', {'form': form})
