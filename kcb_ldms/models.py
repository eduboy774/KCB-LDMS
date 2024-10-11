from django.db import models
import uuid


class KcbLdms(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    ldms_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.ldms_name)

    class Meta:
        db_table = "kcb_ldms"
        ordering = ["-id"]
        verbose_name_plural = "01. Ldms"






































    
# Many to many relationships
# class Teacher(models.Model):
#     primary_key = models.AutoField(primary_key=True)
#     uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
#     name = models.CharField(max_length=9000, null=True, blank=True)
#     position = models.CharField(max_length=9000, null=True, blank=True)

#     def __str__(self):
#         return "{}-{}".format(self.name, self.position)

#     class Meta:
#         db_table = "kcb_backend_teachers"
#         ordering = ["-primary_key"]
#         verbose_name_plural = "01. TEACHER"

# class Subject(models.Model):
#     primary_key = models.AutoField(primary_key=True)
#     uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
#     name = models.CharField(max_length=9000, null=True, blank=True)
#     code = models.CharField(max_length=9000, null=True, blank=True)

#     def __str__(self):
#         return "{}-{}".format(self.name, self.code)

#     class Meta:
#         db_table = "kcb_backend_subjects"
#         ordering = ["-primary_key"]
#         verbose_name_plural = "01. SUBJECTS"


# class TeacherSubject(models.Model):
#     primary_key = models.AutoField(primary_key=True)
#     uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
#     teacher = models.ForeignKey(Teacher, blank=True, null=True, related_name='teacher')
#     subject = models.ForeignKey(Subject, blank=True, null=True, related_name='subject')
