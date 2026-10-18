from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    titulo = models.CharField("título", max_length=200)
    conteudo = models.TextField("conteúdo")
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="postagens", verbose_name="autor",
    )
    publicado = models.BooleanField("publicado", default=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "postagem"
        verbose_name_plural = "postagens"
        ordering = ["-criado_em", "-pk"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("blog:detalhe", kwargs={"pk": self.pk})
