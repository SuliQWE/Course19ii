from rest_framework import serializers
from .models import (UserProfile, Category ,SubCategory , Course,
                     Exam , Question, Option ,Certificate ,Review, Lesson , Assignment)


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'user_image']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = SubCategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'subcategories']


class CourseListSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryListSerializer()
    created_by = UserProfileNameSerializer()
    create_date = serializers.DateTimeField('%d-%m-%Y %H:%M')

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'sub_category', 'price',
                  'created_by', 'create_date']


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    courses = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['sub_category_name', 'courses']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video', 'content']


class CourseDetailSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryListSerializer()
    created_by = UserProfileNameSerializer()
    create_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    update_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'sub_category', 'level', 'price',
                  'created_by', 'description', 'create_date', 'update_date', 'lessons']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
