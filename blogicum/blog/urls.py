from django.urls import include, path

from blog import views

app_name = 'blog'


posts_urls = [
    path(
        '<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'create/',
        views.PostCreateView.as_view(),
        name='create_post'
    ),
    path(
        '<int:post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(
        '<int:post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),
    path(
        '<int:post_id>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        '<int:post_id>/edit_comment/<int:comment_id>/',
        views.CommentUpdateView.as_view(),
        name='edit_comment'
    ),
    path(
        '<int:post_id>/delete_comment/<int:comment_id>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment',
    ),
]

profile_urls = [
    path(
        'edit/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    path(
        '<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
]

urlpatterns = [
    path(
        '',
        views.IndexHome.as_view(),
        name='index'
    ),
    path('posts/', include(posts_urls)),
    path('profile/', include(profile_urls)),
    path(
        'category/<slug:category_slug>/',
        views.CategoryListView.as_view(),
        name='category_posts'
    )
]