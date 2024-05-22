from django.contrib import admin

from .models import Author, Category, Comment, Post, Subscriber


# создаём новый класс для представления публикаций в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с публикациями
    # list_display = [field.name for field in Post._meta.get_fields()]    # генерируем список имён всех полей для более красивого отображения
    list_display = ('title', 'author', 'rating', 'dateCreation')
    list_filter = ('author', 'dateCreation', 'rating')    # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'dateCreation')    # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)
# admin.site.unregister(Post)    # разрегистрируем наши публикации
