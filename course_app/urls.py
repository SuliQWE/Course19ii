from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView,
    CategoryDetailAPIView, SubCategoryListAPIView, SubCategoryDetailAPIView,
    CourseListAPIView, CourseDetailAPIView,
    ExamViewSet, QuestionViewSet, OptionViewSet, CertificateViewSet,
    ReviewViewSet, LessonViewSet, AssignmentViewSet
)

router = SimpleRouter()
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_profiles/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user_profiles/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('subcategories/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail')

]
