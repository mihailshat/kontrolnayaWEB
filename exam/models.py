from django.db import models
from django.contrib.auth.models import User

class msexam(models.Model):
    # 1) поле, отвечающее за название экзамена
    name = models.CharField(max_length=200, verbose_name="Название экзамена")
    
    # 2) дата создания записи
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    # 3) дата проведения экзамена
    exam_date = models.DateTimeField(verbose_name="Дата проведения")
    
    # 4) поле для добавления изображения к записи (задание по экзамену в виде картинки)
    image = models.ImageField(upload_to='exam_images/', blank=True, null=True, verbose_name="Изображение задания")
    
    # 5) поле типа ManyToManyField - пользователи, которые должны писать экзамен
    students = models.ManyToManyField(User, related_name='exams', verbose_name="Студенты")
    
    # 6) поле is_public, отвечающее за публикацию записи
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")
    
    def __str__(self):
        return self.name
    
