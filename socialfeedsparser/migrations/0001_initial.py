# Generated by Django 2.0.4 on 2018-08-21 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name="Channel's name")),
                ('source', models.CharField(choices=[('facebook', 'Facebook')], default=('facebook', 'Facebook'), max_length=50, verbose_name='Social media')),
                ('limit', models.IntegerField(blank=True, null=True, verbose_name='Limit')),
                ('query', models.CharField(help_text='Enter a search query or user/page id.', max_length=255, verbose_name='Query')),
                ('query_type', models.CharField(choices=[('feed', 'feed'), ('search', 'search')], default='feed', help_text='Note: search is not applicable for Facebook.', max_length=5, verbose_name='Search for:')),
                ('periodicity', models.IntegerField(default=60, help_text='Collecting messages periodicy. (In minutes)', verbose_name='Periodicy')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Last Updated')),
                ('user_secret', models.TextField(blank=True, null=True, verbose_name='User Secret')),
                ('user_token', models.TextField(blank=True, null=True, verbose_name='User Token')),
            ],
            options={
                'verbose_name': 'Social feed channel',
                'verbose_name_plural': 'Social feed channels',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_uid', models.CharField(editable=False, max_length=255, verbose_name='ID in the social media source')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link')),
                ('author', models.CharField(max_length=50, verbose_name='Author name')),
                ('author_uid', models.CharField(max_length=50, verbose_name='Author id')),
                ('content', models.TextField(verbose_name='Post content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='socialfeedsparser', verbose_name='Image')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('like_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Like count')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialfeedsparser.Channel')),
            ],
            options={
                'verbose_name': 'Social feed post',
                'verbose_name_plural': 'Social feed posts',
                'ordering': ('order',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('source_uid', 'channel')},
        ),
    ]
