from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)


class SchoolClass(models.Model):
    teacher = models.OneToOneField(Teacher, models.CASCADE, default=1)
    number = models.IntegerField()
    letter = models.CharField(max_length=1, default='a')


class Subject(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.OneToOneField(Teacher, models.CASCADE, default=1)


class Pupil(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    school_class = models.ForeignKey(SchoolClass, models.CASCADE, default=1)


class Achievement(models.Model):
    BAD = '2'
    UNSATISFACTORY = '3'
    GOOD = '4'
    EXCELLENT = '5'

    subject = models.ForeignKey(Subject, models.CASCADE, default=1)
    pupil = models.ForeignKey(Pupil, models.CASCADE, default=1)
    MARK = (
        (BAD, '2'),
        (UNSATISFACTORY, '3'),
        (GOOD, '4'),
        (EXCELLENT, '5'))
    mark = models.CharField(max_length=15,
                            choices=MARK,
                            default=BAD)
