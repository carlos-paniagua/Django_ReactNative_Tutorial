from rest_framework.generics import ListAPIView, RetrieveAPIView
# Django REST Frameworkが提供するジェネリッククラスベースのビューで、複数のオブジェクトのリストを取得したり、
# 単一のオブジェクトを取得したりするAPIビューを簡単に作成できるようにしてくれます。

# ListAPIView: このクラスは、データベースモデルの一覧を表示するためのジェネリックビューです。
# クエリセットの取得やデータのシリアライズ、レスポンスのレンダリングなどの共通の操作を処理します。
# ビュー内でquerysetやserializer_classの属性を定義することで、動作をカスタマイズすることができます。

# RetrieveAPIView: このクラスは、データベースモデルの詳細な情報を表示するためのジェネリックビューです。
# 通常、ユニークな識別子（IDやスラグなど）に基づいて特定のオブジェクトを取得するために使用されます。
# ListAPIViewと同様に、querysetやserializer_classの属性を定義することで動作をカスタマイズできます。

from .serializers import BlogSerializer
from .models import Blog

# ブログ一覧
class BlogListView(ListAPIView):
    queryset = Blog.objects.order_by('-created_at') #作成日時の降順でソートされたBlogモデルのオブジェクトが取得されます。
    serializer_class = BlogSerializer
    
#ブログ詳細
class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()           #これにより、Blogモデルの全てのオブジェクトが取得されます。
    serializer_class = BlogSerializer
    
