from django.db import models
 
 
class Post(models.Model): # импортируется класс models, а затем модель Post наследует класс models.Model.
    title = models.CharField(max_length=200) # Для заголовка title ставим ограничение на 200 символов
    author = models.ForeignKey( # Для поля автора author используем ForeignKey, Это значит, что любой пользователь может быть автором множества записей
        'auth.User',
        on_delete=models.CASCADE, # требуется уточнить опцию on_delete чтобы знать как себя вести при удалении записи из одной таблицы которая связана с данными из других таблиц
    )
    body = models.TextField() # для содержимого статьи body используем тип TextField, что автоматические расширяется, подстраиваясь под длину текста пользователя
 
    def __str__(self):
        return self.title

