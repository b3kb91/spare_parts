from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html

User = get_user_model()


class Review(models.Model):
    part = models.ForeignKey(
        "part.Part",
        related_name="reviews",
        on_delete=models.CASCADE,
        verbose_name="Запчасть",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Пользователь",
        default=1,
    )
    text = models.TextField(max_length=400, verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]

    def to_display(self):
        return [
            self.user,
            self.part,
            self.text[:20]
        ]

    def get_column_headers(self):
        return [
            'Пользователь',
            'Товар',
            'Отзыв',
        ]

    class Meta:
        db_table = "reviews"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
