from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField('タイトル',max_length=255)         #最大255文字の文字列フィールド
    content = models.TextField('内容')                          #最大255文字の文字列フィールド
    updated_at = models.DateTimeField('更新日',auto_now=True)   #記事の最終更新日時を自動的に記録するフィールド 現在の日時が自動的に設定
    created_at = models.DateTimeField('作成日',auto_now_add=True)   #記事の作成日時を自動的に記録するフィールド デルが作成されるタイミングでのみ初期値として現在の日時が設定
    
    class Meta: #デルのメタデータを定義するためのクラス
        verbose_name = 'ブログ'     #モデルの単数形と複数形の表示名を指定
        verbose_name_plural = 'ブログ'
    
    def __str__(self):      #モデルの文字列表現を返すための特殊メソッド
        return self.title   #titleフィールドの値を返し