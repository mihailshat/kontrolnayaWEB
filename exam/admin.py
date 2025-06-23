from django.contrib import admin
from .models import msexam

class MsExamAdmin(admin.ModelAdmin):
    # Поля, которые отображаются в списке объектов
    list_display = ('name', 'exam_date', 'created_date', 'is_public')
    # 1) Поиск по названию экзамена и email пользователя
    search_fields = ('name', 'students__email')
    # 2) Поиск по конкретной дате проведения экзамена (под строкой поиска)
    date_hierarchy = 'exam_date'
    # 3) Настройка удобного редактирования поля M2M
    filter_horizontal = ('students',)  # Горизонтальное отображение: слева - все, справа - выбранные
    # 4) Фильтр по полю is_public
    # 5) Фильтр по полю даты добавления записи
    list_filter = ('is_public', 'created_date')

admin.site.register(msexam, MsExamAdmin)
