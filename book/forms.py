from django import forms

from .models import Book, BookCopy, Borrowing, Librarian, Member, Payment


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(attrs={'rows': 1}),
        }


class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(attrs={'rows': 1}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'publication_year': forms.DateInput(attrs={'type': 'date'}),
        }


class BookCopyForm(forms.ModelForm):
    class Meta:
        model = BookCopy
        fields = "__all__"


class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = "__all__"
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }
