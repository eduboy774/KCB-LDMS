from django.db import models
import uuid

ZONE_CODE = (
    ('ZONE_01', 'ZONE_01'),
    ('ZONE_02', 'ZONE_02'),
    ('ZONE_03', 'ZONE_03'),
    ('ZONE_04', 'ZONE_04'),
)

DEPARTMENT_CODE = (
    ('RB', 'RB'),   #Retail Banking
    ('CB', 'CB'),   #Corporate Banking
    ('IB', 'IB'),   #Investment Banking
    ('CAB', 'CAB'), #Commercial Banking
    ('PB', 'PB'),   #Private Banking 
    ('TC', 'TC'),   #Treasury and Cash Management
    ('RM','RM'),    #Risk Management
    ('CL','CL'),    #Compliance and Legal
    ('HR','HR'),    #Human Resources
    ('ICT','ICT'),  #Information Technology
    ('CS', 'CS'),   #Customer Service
    ('MS','MS'),    #Marketing and Sales
    ('FA','FA'),    #Finance and Accounting
    ('OP','OP'),    #Operations
    ('AI','AI'),    #Audit and Internal Control
)

class KcbCategory(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    category_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.category_name,self.id,self.uuid)

    class Meta:
        db_table = "kcb_categories"
        ordering = ["-id"]
        verbose_name_plural = "01. Category"


class KcbRegionalZonal(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    zone_name = models.CharField(max_length=255, unique=True)
    zone_code = models.CharField(default='', choices=ZONE_CODE, max_length=9000,unique=True)
    zone_description = models.CharField(default='', max_length=9000,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.zone_name,self.id,self.uuid)

    class Meta:
        db_table = "kcb_regional_zonal"
        ordering = ["-id"]
        verbose_name_plural = "02. Regional Zone"

class KcbDepartments(models.Model):
    id =models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    department_name = models.CharField(max_length=255, unique=True)
    department_code = models.CharField(default='', choices=DEPARTMENT_CODE, max_length=9000,unique=True)
    department_description = models.CharField(default='', max_length=9000,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.department_name,self.id,self.uuid)

    class Meta:
        db_table = "kcb_departments"
        ordering = ["-id"]
        verbose_name_plural = "03. Departments"






































    
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
