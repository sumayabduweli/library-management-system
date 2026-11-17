
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MemberForm, LibrarianForm, BookForm, BookCopyForm, BorrowingForm, PaymentForm
from .models import Member, Librarian, Book, BookCopy, Borrowing, Payment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.views.decorators.http import require_POST

# Create your views here.

def login_view(request):
    return render(request,'login.html')

@login_required
def index_view(request):
    recent_books = Book.objects.annotate(
        copy_count=Count('bookcopy'),
        available_copy_count=Count('bookcopy', filter=Q(bookcopy__status=True)),
    ).order_by('-id')[:5]
    context = {
        'total_members': Member.objects.count(),
        'total_librarians': Librarian.objects.count(),
        'total_books': Book.objects.count(),
        'total_copies': BookCopy.objects.count(),
        'available_copies': BookCopy.objects.filter(status=True).count(),
        'total_borrowings': Borrowing.objects.count(),
        'total_payments': Payment.objects.count(),
        'recent_books': recent_books,
    }
    return render(request, 'index.html', context)

@login_required
def librarian_view(request):
    librarians = Librarian.objects.all().order_by('id')
    return render(request, 'librarian.html', {'librarians': librarians})

@login_required
def member_view(request):
    members = Member.objects.all().order_by('id')
    return render(request, 'member.html', {'members': members})

@login_required
def book_view(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'book.html', {'books': books})

@login_required
def book_copy_view(request):
    book_copies = BookCopy.objects.select_related('book_id').all().order_by('copy_id')
    return render(request, 'book_copy.html', {'book_copies': book_copies})

@login_required
def borrowing_view(request):
    borrowings = Borrowing.objects.select_related(
        'member_id', 'copy_id', 'librarian_id'
    ).all().order_by('id')
    return render(request, 'borrowing.html', {'borrowings': borrowings})

@login_required
def payment_view(request):
    payments = Payment.objects.select_related(
        'borrowing_id', 'member_id', 'copy_id', 'librarian_id'
    ).all().order_by('id')
    return render(request, 'payment.html', {'payments': payments})

@login_required
def add_member_view(request):
    message = ''
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            member_form.save()
            message = 'Member added successfully!'

    else:
        member_form = MemberForm()

    members = Member.objects.all()

    context = {
        'member_form': member_form,
        'message': message,
        'members': members
    }
    return render(request, 'add_member.html', context)

@login_required
def add_librarian_view(request):
    message = ''
    if request.method == 'POST':
        librarian_form = LibrarianForm(request.POST)
        if librarian_form.is_valid():
            librarian_form.save()
            message = 'Librarian added successfully!'
    else:
        librarian_form = LibrarianForm()

    librarians = Librarian.objects.all()

    context = {
        'librarian_form': librarian_form,
        'message': message,
        'librarians': librarians
    }
    return render(request, 'add_librarian.html', context)

@login_required
def add_book_view(request):
    message = ''
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            message = 'Book added successfully!'
    else:
        book_form = BookForm()

    books = Book.objects.all()

    context = {
        'book_form': book_form,
        'message': message,
        'books': books
    }
    return render(request, 'add_book.html', context)

@login_required
def add_book_copy_view(request):
    message = ''
    if request.method == 'POST':
        book_copy_form = BookCopyForm(request.POST)
        if book_copy_form.is_valid():
            book_copy_form.save()
            message = 'Book copy added successfully!'
    else:
        book_copy_form = BookCopyForm()

    book_copies = BookCopy.objects.all()

    context = {
        'book_copy_form': book_copy_form,
        'message': message,
        'book_copies': book_copies
    }
    return render(request, 'add_book_copy.html', context)

@login_required
def add_borrowing_view(request):
    message = ''
    if request.method == 'POST':
        borrowing_form = BorrowingForm(request.POST)
        if borrowing_form.is_valid():
            borrowing_form.save()
            message = 'Borrowing added successfully!'
    else:
        borrowing_form = BorrowingForm()

    borrowings = Borrowing.objects.all()

    context = {
        'borrowing_form': borrowing_form,
        'message': message,
        'borrowings': borrowings
    }
    return render(request, 'add_borrowing.html', context)

@login_required
def add_payment_view(request):
    message = ''
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            message = 'Payment added successfully!'
    else:
        payment_form = PaymentForm()

    payments = Payment.objects.all()

    context = {
        'payment_form': payment_form,
        'message': message,
        'payments': payments
    }
    return render(request, 'add_payment.html', context)


@login_required
def edit_member_view(request, member_id):
    message = ''
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        member_form = MemberForm(request.POST, instance=member)

        if member_form.is_valid():
            member_form.save()
            return redirect('add_member_page')
        else:
            message = 'form has invalid data.'
    else:
        member_form = MemberForm( instance=member)

    context = {
        'member_form': member_form,
        'member': member,
        'message': message
    }
    return render(request, 'edit_member.html', context)


@login_required
def edit_librarian_view(request, librarian_id):
    message = ''
    librarian = get_object_or_404(Librarian, id=librarian_id)
    if request.method == 'POST':
        librarian_form = LibrarianForm(request.POST, instance=librarian)

        if librarian_form.is_valid():
            librarian_form.save()
            return redirect('add_librarian_page')
        else:
            message = 'form has invalid data.'
    else:
        librarian_form = LibrarianForm( instance=librarian)

    context = {
        'librarian_form': librarian_form,
        'librarian': librarian,
        'message': message
    }
    return render(request, 'edit_librarian.html', context)


@login_required
def edit_book_view(request, book_id):
    message = ''
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book_form = BookForm(request.POST, instance=book)

        if book_form.is_valid():
            book_form.save()
            return redirect('add_book_page')
        else:
            message = 'form has invalid data.'
    else:
        book_form = BookForm( instance=book)

    context = {
        'book_form': book_form,
        'book': book,
        'message': message
    }
    return render(request, 'edit_book.html', context)

@login_required
def edit_book_copy_view(request, book_copy_id):
    message = ''
    book_copy = get_object_or_404(BookCopy, copy_id=book_copy_id)
    if request.method == 'POST':
        book_copy_form = BookCopyForm(request.POST, instance=book_copy)

        if book_copy_form.is_valid():
            book_copy_form.save()
            return redirect('add_book_copy_page')
        else:   
            message = 'form has invalid data.'

    else:
        book_copy_form = BookCopyForm( instance=book_copy)

    context = {
        'book_copy_form': book_copy_form,
        'book_copy': book_copy,
        'message': message
    }
    return render(request, 'edit_book_copy.html', context)

@login_required
def edit_borrowing_view(request, borrowing_id):
    message = ''
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    if request.method == 'POST':
        borrowing_form = BorrowingForm(request.POST, instance=borrowing)

        if borrowing_form.is_valid():
            borrowing_form.save()
            return redirect('add_borrowing_page')
        else:
            message = 'form has invalid data.'
    else:
        borrowing_form = BorrowingForm(instance=borrowing)

    context = {
        'borrowing_form': borrowing_form,
        'borrowing': borrowing,
        'message': message
    }
    return render(request, 'edit_borrowing.html', context)

@login_required
def edit_payment_view(request, payment_id):
    message = ''
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST, instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            return redirect('add_payment_page')
        else:
            message = 'form has invalid data.'
    else:
        payment_form = PaymentForm(instance=payment)

    context = {
        'payment_form': payment_form,
        'payment': payment,
        'message': message
    }
    return render(request, 'edit_payment.html', context)

#delete views
@login_required
@require_POST
def delete_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    return redirect('add_member_page')

@login_required
@require_POST
def delete_librarian_view(request, librarian_id):
    librarian = get_object_or_404(Librarian, id=librarian_id)
    librarian.delete()
    return redirect('add_librarian_page')

@login_required
@require_POST
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('add_book_page')

@login_required
@require_POST
def delete_book_copy_view(request, book_copy_id):
    book_copy = get_object_or_404(BookCopy, copy_id=book_copy_id)
    book_copy.delete()
    return redirect('add_book_copy_page')

@login_required
@require_POST
def delete_borrowing_view(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    borrowing.delete()
    return redirect('add_borrowing_page')

@login_required
@require_POST
def delete_payment_view(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    return redirect('add_payment_page')  


def sign_up_view(request):
    message = ''
    if request.method == 'POST':
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'Account created successfully!'
        else:
            message = 'form has invalid data.'
    else:
        sign_up_form = UserCreationForm()

    context = {
        'sign_up_form': sign_up_form,
        'message': message
    }
    return render(request, 'registrations/sign_up.html', context)


