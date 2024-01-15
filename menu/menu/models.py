from django.db import models


class Menu(models.Model):
    slug = models.SlugField(max_length=20, primary_key=True)
    title = models.CharField(verbose_name="Menu name", max_length=80)
    childs = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return f"/{self.slug}/"

    class Meta:
        verbose_name_plural = "Menues"
