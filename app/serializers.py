from rest_framework import serializers
from .models import Blog

# シリアライザは、データモデル（データベースのレコードやDjangoのモデル）をシリアライズ（直列化）し、
# JSONやXMLなどの形式に変換するためのクラスです。
# また、逆にシリアライズされたデータをデシリアライズして元のデータモデルに戻すこともできます。

#ブログ
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog        #シリアライザに含めるフィールドを指定します
        fields = '__all__' #、Blogモデルの全てのフィールドがシリアライザに含まれるようになります