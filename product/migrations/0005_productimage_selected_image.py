# Generated by Django 3.1 on 2020-08-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_image_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='selected_image',
            field=models.CharField(choices=[(1, 'https://cdn.mos.cms.futurecdn.net/ahevYTh9pWRzkNPF85MQhb.jpg')], default=1, max_length=255),
        ),
    ]
