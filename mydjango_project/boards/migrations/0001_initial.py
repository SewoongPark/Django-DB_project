# Generated by Django 4.1 on 2023-06-17 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('champion', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('line', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('CC', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Champion_rate',
            fields=[
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='boards.champions')),
                ('line', models.CharField(max_length=100)),
                ('win_rate', models.CharField(max_length=100)),
                ('pick_rate', models.CharField(max_length=100)),
                ('ban_rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='champion_skill_img_text',
            fields=[
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='boards.champions')),
                ('cham_img', models.CharField(max_length=512)),
                ('passive_img', models.CharField(max_length=512)),
                ('q_img', models.CharField(max_length=512)),
                ('w_img', models.CharField(max_length=512)),
                ('e_img', models.CharField(max_length=512)),
                ('r_img', models.CharField(max_length=512)),
                ('passive', models.CharField(max_length=512)),
                ('Q', models.CharField(max_length=512)),
                ('W', models.CharField(max_length=512)),
                ('E', models.CharField(max_length=512)),
                ('R', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='champion_skill_name',
            fields=[
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='boards.champions')),
                ('passive_name', models.CharField(max_length=512)),
                ('Q_name', models.CharField(max_length=512)),
                ('W_name', models.CharField(max_length=512)),
                ('E_name', models.CharField(max_length=512)),
                ('R_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Champion_story',
            fields=[
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='boards.champions')),
                ('url', models.CharField(max_length=512)),
                ('text', models.TextField()),
                ('story', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='champion_tip',
            fields=[
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='boards.champions')),
                ('image_url', models.CharField(max_length=512)),
                ('enemy_tips', models.TextField()),
                ('ally_tips', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.FloatField()),
                ('likes', models.FloatField()),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.champions')),
            ],
        ),
        migrations.CreateModel(
            name='Champion_counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_name', models.CharField(max_length=512)),
                ('win', models.CharField(max_length=512)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.champions')),
            ],
        ),
    ]
