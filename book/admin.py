from django.contrib import admin
from .models import Book, BookCopy, Borrowing, Payment, Member, Librarian

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title', 'author', 'publisher', 'publication_year', 'category')

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('copy_id', 'book_id', 'edition', 'status')

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_id', 'copy_id', 'librarian_id', 'borrow_date', 'return_date')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'borrowing_id', 'member_id', 'copy_id', 'librarian_id', 'payment_date', 'payment_method')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'age', 'contact', 'gender')

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'contact', 'gender')

admin.site.register(Book, BookAdmin)
admin.site.register(BookCopy, BookCopyAdmin)   
admin.site.register(Borrowing, BorrowingAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Librarian, LibrarianAdmin)
