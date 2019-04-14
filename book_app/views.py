from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from book_app.models import Blog,Comment
from .forms import PostForm, CommentForm

# Create your views here.
class IndexView(TemplateView):
  template_name = 'book_app/index.html'

class BlogListView(ListView):
  model = Blog

class BlogDetailView(DetailView):
  model = Blog

class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirected_field_name='book_app/blog_detail.html'
  form_class = PostForm
  model = Blog

class PostUpdateView(LoginRequiredMixin,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'book_app/blog_detail.html'
  form_class = PostForm
  model = Blog

class PostDeleteView(LoginRequiredMixin,DeleteView):
  model = Blog
  success_url = reverse_lazy('book_app:blog_list')

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog_pk = comment.blog.pk
    comment.delete()
    return redirect('book_app:blog_detail', pk=blog_pk)

def add_comment_to_post(request, pk):
  blog = get_object_or_404(Blog, pk=pk)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        return redirect('book_app:blog_detail', pk=blog.pk)
  else:
    form = CommentForm()
  return render(request, 'book_app/add_comment_to_post.html', {'form': form})
