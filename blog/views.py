from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    postagens = Post.objects.filter(publicado=True).select_related("autor")
    return render(request, "blog/index.html", {"nome": "Bruno Macedo", "postagens": postagens})


def detalhe(request, pk):
    postagem = get_object_or_404(Post.objects.select_related("autor"), pk=pk, publicado=True)
    return render(request, "blog/detalhe.html", {"postagem": postagem})
