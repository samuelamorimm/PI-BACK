from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from blog.forms import PostForm
from .models import Post

def home(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    
    return render(request, 'base/base.html', {'posts': posts})

# Função para verificar se o usuário é administrador
def is_admin(user):
    return user.is_superuser

#Listar post 
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    
    return render(request, 'blog/post_list.html', {'posts': posts})

#Exibir um post 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#Criar um post
@login_required
@user_passes_test(is_admin)  # Garante que só administradores possam criar posts
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})

#Editar um post 
@login_required
@user_passes_test(is_admin)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk) 
    else:
        form = PostForm(instance=post) 
    return render(request, 'blog/post_form.html', {'form': form})

#Excluir um post
@login_required
@user_passes_test(is_admin)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Verifica se o usuário tem permissão para excluir
    if not request.user.is_superuser:
        return HttpResponseForbidden("Você não tem permissão para excluir este post.")

    if request.method == 'POST':
        # Deleta o post
        post.delete()
        return redirect('post_list')  # Redireciona para a lista de posts após a exclusão

    return redirect('post_list')