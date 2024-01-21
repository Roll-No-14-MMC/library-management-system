from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    image = models.FileField(upload_to='students/')
    student_id =models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    author_name = models.CharField(max_length = 100)
    number_of_copies = models.IntegerField()
    category_id = models.ForeignKey("Category",on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.name

class BookBorrow(models.Model):
    student_id = models.ForeignKey("Student", on_delete = models.CASCADE)
    book_id = models.ForeignKey("Books", on_delete = models.CASCADE)
    borrowed_at = models.DateField()
    returned_at = models.DateField()
    is_returned = models.BooleanField(default = False)

    def __str__(self) -> str:
        return (f'{self.student_id} has borrowed {self.book_id}!')
