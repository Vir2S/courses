from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class CourseParticipant(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_index=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_index=False)
    complete = models.BooleanField(default=False)
    count = 0

    class Meta:
        unique_together = (
            'course',
            'student',
        )

    def __str__(self):
        return '%s %s' % (self.course, self.student)
