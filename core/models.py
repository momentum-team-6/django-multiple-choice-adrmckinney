from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='snippets')
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='snippets')
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title


class Category(models.Model):
    language = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.language


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        # ordering = 'category'
    
    # def get_absolute_url(self):
    #     return reverse('category_detail', args[str(self.id)])
    
