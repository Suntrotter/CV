from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Image'

class About_me(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = 'About_me'
        verbose_name_plural = 'About_me'


class Skills(models.Model):
    skill = models.TextField()

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'

class Education(models.Model):
    place_of_study = models.TextField()

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

class Projects(models.Model):
    project = models.TextField()

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'
