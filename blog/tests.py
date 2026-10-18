from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostagensTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = get_user_model().objects.create_superuser(
            username="administrador_teste", password="senha-apenas-para-testes-53"
        )

    def test_pagina_inicial_sem_postagens(self):
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "Ainda não há postagens publicadas.")
        self.assertTemplateUsed(response, "blog/base.html")

    def test_postagens_aparecem_no_painel_administrativo(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("admin:index"))
        self.assertContains(response, reverse("admin:blog_post_changelist"))
        self.assertContains(response, "Postagens")

    def test_cadastrar_editar_e_excluir_pelo_admin(self):
        self.client.force_login(self.admin)
        response = self.client.post(reverse("admin:blog_post_add"), {
            "titulo": "Minha primeira postagem", "conteudo": "Conteúdo criado no painel.",
            "publicado": "on", "_save": "Salvar",
        })
        self.assertEqual(response.status_code, 302)
        postagem = Post.objects.get()
        self.assertEqual(postagem.autor, self.admin)
        self.assertContains(self.client.get(reverse("blog:index")), postagem.titulo)
        self.assertContains(self.client.get(postagem.get_absolute_url()), postagem.conteudo)
        self.client.post(reverse("admin:blog_post_change", args=[postagem.pk]), {
            "titulo": "Título atualizado", "conteudo": "Conteúdo editado.",
            "publicado": "on", "_save": "Salvar",
        })
        postagem.refresh_from_db()
        self.assertEqual(postagem.titulo, "Título atualizado")
        self.assertContains(self.client.get(reverse("blog:index")), "Título atualizado")
        self.client.post(reverse("admin:blog_post_delete", args=[postagem.pk]), {"post": "yes"})
        self.assertFalse(Post.objects.exists())

    def test_rascunho_nao_aparece_no_site_nem_por_url(self):
        postagem = Post.objects.create(titulo="Rascunho privado", conteudo="Não publicar", autor=self.admin, publicado=False)
        self.assertNotContains(self.client.get(reverse("blog:index")), postagem.titulo)
        self.assertEqual(self.client.get(postagem.get_absolute_url()).status_code, 404)

    def test_titulo_e_conteudo_sao_escapados(self):
        postagem = Post.objects.create(titulo="<script>alert('titulo')</script>", conteudo="<script>alert('conteudo')</script>", autor=self.admin)
        response = self.client.get(postagem.get_absolute_url())
        self.assertNotContains(response, "<script>")
        self.assertContains(response, "&lt;script&gt;")

    def test_visitante_nao_pode_cadastrar_postagem(self):
        response = self.client.get(reverse("admin:blog_post_add"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("admin:login"), response.url)
        self.assertFalse(Post.objects.exists())

    def test_mais_novas_aparecem_primeiro(self):
        primeira = Post.objects.create(titulo="Primeira", conteudo="A", autor=self.admin)
        segunda = Post.objects.create(titulo="Segunda", conteudo="B", autor=self.admin)
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(list(response.context["postagens"]), [segunda, primeira])
