# Generated by Django 4.1.1 on 2022-10-09 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_pedido_active_account_pedido_cui_pedido_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='active_account',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cui',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fisrt_name',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='login_attempts',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='username',
        ),
    ]
