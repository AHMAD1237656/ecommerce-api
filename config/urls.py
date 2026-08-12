from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from categories.views import CategoryViewSet
from products.views import ProductViewSet
from customers.views import CustomerViewSet
from cart.views import CartViewSet
from orders.views import OrderViewSet
from wishlist.views import WishlistViewSet
from reviews.views import ReviewViewSet
from coupons.views import CouponViewSet
from inventory.views import InventoryViewSet


router = DefaultRouter()


router.register(
    "categories",
    CategoryViewSet,
    basename="category"
)

router.register(
    "products",
    ProductViewSet,
    basename="product"
)

router.register(
    "customers",
    CustomerViewSet,
    basename="customer"
)

router.register(
    "cart",
    CartViewSet,
    basename="cart"
)

router.register(
    "wishlist",
    WishlistViewSet,
    basename="wishlist"
)

router.register(
    "orders",
    OrderViewSet,
    basename="order"
)

router.register(
    "reviews",
    ReviewViewSet,
    basename="review"
)

router.register(
    "coupons",
    CouponViewSet,
    basename="coupon"
)

router.register(
    "inventory",
    InventoryViewSet,
    basename="inventory"
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/",
        include(router.urls)
    ),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    # OpenAPI Schema
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    # Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)