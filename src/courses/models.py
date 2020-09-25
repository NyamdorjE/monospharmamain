from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class CourseCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    class Meta:
        verbose_name = _("Course category")
        verbose_name_plural = _("Course category")
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="Course_category", null=True)
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(
        max_length=200, null=True, verbose_name=_('Description'))
    image = models.ImageField(
        upload_to='cat_images', default='cat_images/default.png', verbose_name=_('Picture'))
    students = models.ManyToManyField(
        User, swappable=True, verbose_name=_('Students'))
    price = models.CharField(
        max_length=150, verbose_name=_('Price'),  default="₮")

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Course")
        ordering = ['title']

    def __str__(self):
        return '{}'.format(self.title)


class Subject(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Created by '))
    title = models.CharField(max_length=30, verbose_name=_('Title'))
    slug = models.SlugField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    description = models.TextField(
        max_length=400, verbose_name=_('Description'))
    created_on = models.DateTimeField(
        auto_now=True, verbose_name=_('Created_on'))

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subject")
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    title = models.CharField(
        max_length=30, verbose_name=_(' Lesson title'))
    slug = models.SlugField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name=_('Subject'))
    video_id = models.FileField(
        upload_to="course_video", blank=True, null=True, verbose_name=_('Upload video'))
    content = RichTextField(verbose_name=_('Content'))
    position = models.IntegerField(verbose_name=_('Lesson position'))
    pdf_file = models.FileField(upload_to="pdf_file", null=True, blank=True)
    photo = models.FileField(upload_to="course_image", null=True, blank=True)
    is_active = models.BooleanField(_("Register activated"))
    start_at = models.DateTimeField(
        _('Start_at'), help_text='0000-00-00 00:00:00 форматтай байна', null=True)
    state_choices = (
        ('started', 'Lesson started'),
        ('done', 'Lesson over')
    )
    state = models.CharField(max_length=100, blank=False,
                             choices=state_choices, default="started", verbose_name=_('State'))
    youtube_code = models.CharField(verbose_name=_(
        'Youtubecode'), max_length=250, blank=True, null=True)
    embedurl = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.subject.slug, 'lesson_slug': self.slug})

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lesson")
        ordering = ['title']


class Post(models.Model):
    post = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Review(models.Model):
    text = models.CharField(verbose_name=_('Question text'), max_length=250)
    student = models.ForeignKey(User, verbose_name=_(
        'Student'), null=False, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=_(
        'Lesson'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        verbose_name=_('Created at '), auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ['-created_at']

    def __unicode__(self):
        return u'{0}'.format(self.question)
