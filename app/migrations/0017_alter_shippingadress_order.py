# Generated by Django 4.2.2 on 2023-07-20 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_shippingadress_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingadress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.orderitem'),
        ),
    ]
