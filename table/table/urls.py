
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.forms import MyCustomUserForm
from users.views import MyLoginView, RegistrationView
from table.views import MainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('goods/', include('goods.urls')),
    path(
        'accounts/register/',
        RegistrationView.as_view(
            form_class=MyCustomUserForm,
        ),
        name='django_registration_register'),
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path(
        'accounts/',
        include(
             'django_registration.backends.activation.urls',
            )
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MainView.as_view(), name='main')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "table.views.not_found"
