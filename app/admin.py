from django.contrib import admin
from .models import Blog

# Register your models here.

# Adminサイトを使用すると、データベースモデルを簡単に管理するためのインターフェースを提供することができます。
# admin.site.register()メソッドを使用して、管理サイトにモデルを登録すると、
# そのモデルのデータを管理者が追加、表示、編集、削除などの操作を行うことができます。
admin.site.register(Blog)
