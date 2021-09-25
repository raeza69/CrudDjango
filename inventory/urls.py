from django.urls import path
from . import views

app_name = 'inventory'


urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"), 
    
    path('manage/', views.ManageListView.as_view(),name='manage'),
    
    path('add_user/', views.CreateUser.as_view(),name='user'),
    path('', views.LocationListView.as_view(),name='index'),
    path('location/create/',views.LocationCreateView.as_view(),name='create'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('product/<slug:slug>/update/',views.ProductUpdateView.as_view(),name='product_update'),
    path('location/<slug:slug>/',views.LocationDetailView.as_view(),name='location'),
    path('move/<slug:slug>/<slug:location_slug>/',views.add_movement,name='movement'),
    path('move_out/<slug:slug>/<slug:location_slug>/',views.move_out,name='move_out'),
    path('delete/<int:id>/',views.delete_location,name='delete'),
    path('destroy/<int:id>',views.delete_view),
    path('useractive/<int:ky>', views.ActivateUser),
    path('userdeactive/<int:ky>', views.DeactivateUser)
]