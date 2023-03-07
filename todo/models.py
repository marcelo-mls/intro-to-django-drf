from django.db import models


# 1 - Primeira Etapa (proximo passo em admin.py)
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - [{self.created_at}]'


class Task(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255, default='Description here')
    is_finished = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} SINCE {self.created_at} DONE? {self.is_finished}'
