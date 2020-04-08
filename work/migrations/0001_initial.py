# Generated by Django 3.0.3 on 2020-04-05 19:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField()),
                ('bookname', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=20)),
                ('requester', models.CharField(max_length=20)),
                ('makeanoffer', models.CharField(default='please provide me this book', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OwnedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('askedBookname', models.CharField(max_length=100)),
                ('requestername', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('usermail', models.EmailField(max_length=254, unique=True)),
                ('userfirstname', models.CharField(max_length=10)),
                ('userlastname', models.CharField(max_length=10)),
                ('userpassword', models.CharField(max_length=30)),
                ('userlocation', models.CharField(max_length=30)),
                ('usercontact', models.IntegerField(unique=True)),
                ('userDoB', models.CharField(max_length=10)),
                ('usergender', models.CharField(max_length=6)),
                ('userKey', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('bookimage', models.ImageField(blank=True, upload_to='bookImg/')),
                ('bookimage0', models.ImageField(blank=True, upload_to='bookImg/')),
                ('bookimage1', models.ImageField(blank=True, upload_to='bookImg/')),
                ('bookimage2', models.ImageField(blank=True, upload_to='bookImg/')),
                ('bookname', models.CharField(max_length=100)),
                ('bookdescription', models.CharField(max_length=300)),
                ('bookauthor', models.CharField(blank=True, max_length=30)),
                ('active_status', models.BooleanField(default=True)),
                ('timeadded', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.UserDetails')),
            ],
        ),
    ]
