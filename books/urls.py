"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include
from book.views import index_view, librarian_view, member_view, book_view, book_copy_view, borrowing_view, payment_view, add_member_view, add_librarian_view, add_book_view, add_book_copy_view, add_borrowing_view, add_payment_view, edit_member_view, edit_librarian_view, edit_book_view, edit_book_copy_view, edit_borrowing_view, edit_payment_view, delete_member_view,delete_librarian_view, delete_book_view, delete_book_copy_view, delete_borrowing_view, delete_payment_view, sign_up_view

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registrations/login.html'), name='login_page'),
    path('', index_view, name='index_page'),
    path('librarian/', librarian_view, name='librarian_page'),
    path('member/', member_view, name='member_page'),
    path('book/', book_view, name='book_page'),
    path('book-copy/', book_copy_view, name='book_copy_page'),
    path('borrowing/', borrowing_view, name='borrowing_page'),
    path('payment/', payment_view, name='payment_page'),

    path('add-member/', add_member_view, name='add_member_page'),
    path('add-librarian/', add_librarian_view, name='add_librarian_page'),
    path('add-book/', add_book_view, name='add_book_page'),
    path('add-book-copy/', add_book_copy_view, name='add_book_copy_page'),
    path('add-borrowing/', add_borrowing_view, name='add_borrowing_page'),
    path('add-payment/', add_payment_view,  name='add_payment_page'),

    path('edit-member/<int:member_id>/', edit_member_view, name='edit_member_page'),
    path('edit-librarian/<int:librarian_id>/', edit_librarian_view, name='edit_librarian_page'),
    path('edit-book/<int:book_id>/', edit_book_view, name='edit_book_page'),
    path('edit-book-copy/<int:book_copy_id>/', edit_book_copy_view, name='edit_book_copy_page'),
    path('edit-borrowing/<int:borrowing_id>/', edit_borrowing_view, name='edit_borrowing_page'),
    path('edit-payment/<int:payment_id>/', edit_payment_view, name='edit_payment_page'),

    path('delete-member/<int:member_id>/', delete_member_view, name='delete_member_page'),
    path('delete-librarian/<int:librarian_id>/', delete_librarian_view, name='delete_librarian_page'),
    path('delete-book/<int:book_id>/', delete_book_view, name='delete_book_page'),
    path('delete-book-copy/<int:book_copy_id>/', delete_book_copy_view, name='delete_book_copy_page'),
    path('delete-borrowing/<int:borrowing_id>/', delete_borrowing_view, name='delete_borrowing_page'),
    path('delete-payment/<int:payment_id>/', delete_payment_view, name='delete_payment_page'),

    path('sign-up/', sign_up_view, name='sign_up_page'),

]

