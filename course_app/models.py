from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import BooleanField
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)], null=True, blank=True)
    phone = PhoneNumberField()
    UserRole = (
        ('student','student'),
        ('teacher','teacher')
    )
    user_role = models.CharField(max_length=20, choices=UserRole)
    register_date = models.DateTimeField(auto_now_add=True)
    user_image = models.ImageField(upload_to='users_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.sub_category_name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='courses')
    LevelChoices = (
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard'),
    )
    level = models.CharField(max_length=10, choices=LevelChoices, default='easy')
    price = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    video = models.URLField()
    content = models.FileField(upload_to='lesson_video/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateField()
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_role': 'student'})

    def __str__(self):
        return self.title

class Exam(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()



class Question(models.Model):
    question_name = models.CharField(max_length=50)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=50)
    option_type = BooleanField()


class Certificate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_role': 'student'})
    issued_date = models.DateField()
    certificate_url = models.FileField(upload_to='certificate_url/', null=True, blank=True)


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_role': 'student'})
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField()

