# Generated by Django 4.2.7 on 2023-11-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2023-11-13')),
                ('due_date', models.DateField(default='2023-11-13')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='tasklist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
