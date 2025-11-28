from .models import (Country , City , Category ,SubCategory , Course,
                     Exam , Question, Option ,Review, Lesson , Assignment)
from modeltranslation.translator import TranslationOptions,register

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name','description',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title','description',)

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_name',)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name',)

