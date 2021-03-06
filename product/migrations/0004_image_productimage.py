# Generated by Django 3.1 on 2020-08-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200830_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='https://thumbs.dreamstime.com/b/no-thumbnail-image-placeholder-forums-blogs-websites-148010362.jpg', max_length=255)),
                ('upload_to', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_product', models.CharField(choices=[(1, 'Laptop'), (2, 'Monitor'), (3, 'Mouse'), (4, 'tastatura')], max_length=255)),
            ],
        ),
    ]
