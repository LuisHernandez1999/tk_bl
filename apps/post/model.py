from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Publication(models.Model):
    imagem1 = models.URLField(blank=True, null=True)
    imagem2 = models.URLField(blank=True, null=True)
    imagem3 = models.URLField(blank=True, null=True)
    imagem4 = models.URLField(blank=True, null=True)

    # Data da publicação
    data = models.DateField(default=timezone.now)

    # Formulário / observação
    formulario = models.TextField(
        blank=True,
        null=True,
        max_length=175
    )

    # Dono da publicação
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="publications"
    )

    def clean(self):
        super().clean()

        imagens = [
            self.imagem1,
            self.imagem2,
            self.imagem3,
            self.imagem4,
            self.imagem5,
            self.imagem6,
            self.imagem7,
        ]

        if not any(imagens):
            raise ValidationError(
                "Adicione pelo menos uma imagem à publicação."
            )

    class Meta:
        db_table = "publication"
        managed = True
        indexes = [
            models.Index(fields=["data"]),
            models.Index(fields=["owner", "data"]),
        ]

    def __str__(self):
        return f"Publication {self.id} - {self.owner}"
