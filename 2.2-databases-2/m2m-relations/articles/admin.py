from pprint import pprint

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        mains_num = 0
        pprint(self.forms)
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']:
                mains_num += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if mains_num == 0:
            raise ValidationError('Выберите главный тэг')
        elif mains_num > 1:
            raise ValidationError('Главный тэг может быть только один')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = Scope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
