from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "publicado", "criado_em")
    list_filter = ("publicado", "criado_em")
    search_fields = ("titulo", "conteudo", "autor__username")
    readonly_fields = ("autor", "criado_em", "atualizado_em")
    fields = ("titulo", "conteudo", "publicado", "autor", "criado_em", "atualizado_em")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        super().save_model(request, obj, form, change)
