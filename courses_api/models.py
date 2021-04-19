from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    students = models.ManyToManyField('Student', related_name='courses', blank=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return '%s %s' % (self.name, self.student_count())

    def student_count(self):
        return Course.objects.filter(pk=self.id).aggregate(models.Count('students'))


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class CourseParticipant(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_index=False, related_name='course')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_index=False, related_name='student')
    complete = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            'course',
            'student',
        )

    def __str__(self):
        return '%s %s %s' % (self.course, self.student, self.complete)
