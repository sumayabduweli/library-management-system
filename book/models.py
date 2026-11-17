from django.db import models

# Create your models here.

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Librarian(models.Model):
        GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female')
        ]

        firstname = models.CharField(max_length=100)
        lastname = models.CharField(max_length=100)
        contact = models.CharField(max_length=15, blank=True)
        address = models.TextField(blank=True, null=True)
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
        email = models.EmailField(unique=True, blank=True, null=True)

        def __str__(self):
            return f"{self.firstname} {self.lastname}"

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_year = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.book_title

class BookCopy(models.Model):
    StatusChoices = [
        (True, 'Available'),
        (False, 'Not Available')
    ]

    copy_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    edition = models.PositiveIntegerField()
    status = models.BooleanField(default=True, choices=StatusChoices)

    def __str__(self):
        return f"Copy {self.copy_id} - {self.book_id}"

class Borrowing(models.Model):
        member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
        copy_id = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
        librarian_id = models.ForeignKey(Librarian, on_delete=models.CASCADE)
        borrow_date = models.DateField()
        return_date = models.DateField()

        def __str__(self):
            return f"{self.member_id} - {self.copy_id}"

class Payment(models.Model):
    borrowing_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    copy_id = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    librarian_id = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.pk} - {self.member_id} ({self.payment_method})"
        

