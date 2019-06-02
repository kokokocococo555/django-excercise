from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    # books
    path('book/', views.book_list, name='book_list'),  # 一覧
    path('book/add/', views.book_edit, name='book_add'),  # 登録
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),  # 削除
    # impressions
    path('impression/<int:book_id>/', views.ImpressionList.as_view(), name='impression_list'),
    path('impression/add/<int:book_id>/', views.impression_edit, name='impression_add'),
    path('impression/mod/<int:book_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),
    path('impression/del/<int:book_id>/<int:impression_id>/', views.impression_del, name='impression_del'),
]