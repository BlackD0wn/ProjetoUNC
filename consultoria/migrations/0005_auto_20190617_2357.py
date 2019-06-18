# Generated by Django 2.0.13 on 2019-06-18 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultoria', '0004_post_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('NOVO', 'Novo'), ('CONTATO', 'Realizado contato'), ('ACEITO', 'Aceito'), ('RECUSADO', 'Recusado')], default='NOVO', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AddField(
            model_name='contact',
            name='service',
            field=models.ForeignKey(on_delete='CASCADE', to='consultoria.Service'),
        ),
    ]