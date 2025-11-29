from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView,
    CategoryDetailAPIView, SubCategoryListAPIView, SubCategoryDetailAPIView,
    CourseListAPIView, CourseDetailAPIView,
    CertificateViewSet,
    ReviewCreateAPIView,ReviewEditAPIView, LessonViewSet, AssignmentViewSet,
    SubscribeApiView ,CourseCreateViewSet,ExamListAPIView,ExamDetailAPIView,OptionViewSet,QuestionViewSet,
    QuestionCreateViewSet,OptionCreateViewSet,RegisterView,LogoutView,CustomLoginView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = SimpleRouter()

router.register(r'certificates', CertificateViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'course_create', CourseCreateViewSet)
router.register(r'question_create', QuestionCreateViewSet)
router.register(r'option_create', OptionCreateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user_profiles/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user_profiles/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('subcategories/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('subscribe/', SubscribeApiView.as_view(), name='subscribe'),
    path('exams/', ExamListAPIView.as_view(), name='exam_list'),
    path('exams/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('exams/<int:pk>/', QuestionViewSet.as_view(), name='exam_question'),
    path('exams/<int:pk>/', OptionViewSet.as_view(), name='exam_option'),
]
