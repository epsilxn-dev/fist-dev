from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from filebrowser import sites

schema_view = get_schema_view(
    openapi.Info(
        title="FIST API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="arklightx@yandex.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^admin/filebrowser/', sites.site.urls),
    path(r'grappelli/', include("grappelli.urls")),
    re_path(r'^tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include("src.modules.tags.urls")),
    path('api/v1/', include("src.modules.user.user.urls")),
    path('api/v1/', include("src.modules.faculty.structure.urls")),
    path('api/v1/', include("src.modules.faculty.laboratories.urls")),
    path('api/v1/', include("src.modules.projects.ideas.urls")),
    path('api/v1/', include("src.modules.work.urls")),
    path('api/v1/', include("src.modules.questions.urls")),
    path('api/v1/', include("src.modules.courses.north_valley.urls")),
    path('api/v1/', include("src.modules.news.fac_news.urls")),
    path('api/v1/', include("src.modules.courses.fist_school.urls")),
    path('api/auth/', include('src.modules.user.identification.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
