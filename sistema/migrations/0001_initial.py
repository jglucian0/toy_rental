# Generated by Django 5.2.4 on 2025-07-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brinquedo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('toboga', 'Tobogã Inflável'), ('cama_elastica', 'Cama Elástica'), ('piscina_bolas', 'Piscina de Bolas')], max_length=20)),
                ('valor_locacao', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ultima_limpeza', models.DateField()),
                ('disponivel', models.BooleanField(default=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
