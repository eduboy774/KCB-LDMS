# Generated by Django 4.2.1 on 2024-10-11 16:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KcbLdms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('ldms_name', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '01. Ldms',
                'db_table': 'kcb_ldms',
                'ordering': ['-id'],
            },
        ),
    ]
