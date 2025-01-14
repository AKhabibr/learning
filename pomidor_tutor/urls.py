"""
URL configuration for pomidor_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orders.views import orders_page

from rest_framework.routers import SimpleRouter


from orders.views import orders_page, OrderView

# Что делает SimpleRouter?
# Он автоматически создает маршруты для стандартных действий API (таких как list, create, retrieve, update, destroy) на основе представлений, определённых в классе ViewSet (в твоём случае это OrderView).
# Он избавляет от необходимости вручную прописывать маршруты для каждого HTTP-метода (например, для GET, POST, PUT, DELETE), что упрощает настройку API.

router = SimpleRouter()

# router.register() — это метод, который позволяет зарегистрировать класс представления (в твоём случае OrderView) и указать URL-путь, по которому это представление будет доступно
router.register('api/orders', OrderView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', orders_page),
]

urlpatterns += router.urls

 
