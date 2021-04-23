from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    lectures = models.IntegerField(default=0)

    students = models.ManyToManyField('Student', related_name='courses', blank=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
