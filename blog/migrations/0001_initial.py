from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200, verbose_name="título")),
                ("conteudo", models.TextField(verbose_name="conteúdo")),
                ("publicado", models.BooleanField(default=True, verbose_name="publicado")),
                ("criado_em", models.DateTimeField(auto_now_add=True, verbose_name="criado em")),
                ("atualizado_em", models.DateTimeField(auto_now=True, verbose_name="atualizado em")),
                ("autor", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="postagens", to=settings.AUTH_USER_MODEL, verbose_name="autor")),
            ],
            options={
                "verbose_name": "postagem", "verbose_name_plural": "postagens",
                "ordering": ["-criado_em", "-pk"],
            },
        ),
    ]
