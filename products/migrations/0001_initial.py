# Generated by Django 2.1.6 on 2019-02-20 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='这是app标题', max_length=50)),
                ('intro', models.TextField(default='这是app介绍')),
                ('url', models.CharField(default='Http://', max_length=100)),
                ('icon', models.ImageField(default='1.png', upload_to='images/')),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('votes', models.IntegerField(default=1)),
                ('pub_date', models.DateTimeField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
