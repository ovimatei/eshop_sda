# Generated by Django 3.1 on 2020-08-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productimage_selected_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='selected_image',
            field=models.CharField(choices=[(1, 'https://cdn.mos.cms.futurecdn.net/ahevYTh9pWRzkNPF85MQhb.jpg')], default=None, max_length=255),
        ),
    ]
