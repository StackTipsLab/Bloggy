# Generated by Django 4.2.6 on 2023-10-21 21:44

import colorfield.fields
import django.contrib.auth.validators
import bloggy.models.article
import bloggy.models.categories
import bloggy.models.course
import bloggy.models.mixin.ResizeImageMixin
import bloggy.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_photo', models.ImageField(blank=True, null=True, storage=bloggy.models.user.select_storage,
                                                    upload_to=bloggy.models.user.upload_profile_image)),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('github', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['username'],
            },
            bases=(bloggy.models.mixin.ResizeImageMixin.ResizeImageMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('display_order', models.IntegerField(default=0, help_text='Display order', null=True)),
                ('title', models.CharField(help_text='Enter title', max_length=300)),
                ('keywords', models.CharField(blank=True, help_text='Enter title', max_length=300, null=True)),
                ('publish_status',
                 models.CharField(blank=True, choices=[('DRAFT', 'DRAFT'), ('LIVE', 'LIVE'), ('DELETED', 'DELETED')],
                                  default='DRAFT', help_text='Select publish status', max_length=20, null=True,
                                  verbose_name='Publish status')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(help_text='Enter slug', max_length=150, unique=True)),
                ('excerpt', models.CharField(blank=True, help_text='Enter excerpt', max_length=500, null=True)),
                ('video_id', models.CharField(blank=True, help_text='YouTube Video ID', max_length=100, null=True)),
                ('difficulty', models.CharField(blank=True,
                                                choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'),
                                                         ('advance', 'Advance')], default='beginner',
                                                help_text='Select difficulty', max_length=20, null=True,
                                                verbose_name='Difficulty level')),
                ('post_type',
                 models.CharField(blank=True, choices=[('article', 'Article'), ('quiz', 'Quiz'), ('lesson', 'Lesson')],
                                  default='article', help_text='Post type', max_length=20, null=True,
                                  verbose_name='Post type')),
                ('template_type', models.CharField(blank=True, choices=[('standard', 'Standard'), ('cover', 'Cover'),
                                                                        ('naked', 'Naked'), ('full', 'Full')],
                                                   default='standard', help_text='Template type', max_length=20,
                                                   null=True, verbose_name='Template type')),
                ('duration', models.IntegerField(default='1',
                                                 help_text='Duration in minutes. For articles, it will be calculated automatically.')),
                ('is_featured', models.BooleanField(default=False, help_text='Should this story be featured on site?')),
                ('content', models.TextField(help_text='Post content', null=True)),
                ('thumbnail',
                 models.ImageField(blank=True, null=True, upload_to=bloggy.models.article.upload_thumbnail_image)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles',
                                             to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(help_text='Enter title', max_length=150)),
                ('article_count', models.IntegerField(default=0)),
                ('slug', models.SlugField(help_text='Enter slug', max_length=150, unique=True)),
                (
                'description', models.TextField(blank=True, help_text='Enter description', max_length=1000, null=True)),
                ('logo', models.ImageField(null=True, upload_to=bloggy.models.categories.upload_logo_image)),
                ('color',
                 colorfield.fields.ColorField(default='#1976D2', image_field=None, max_length=25, samples=None)),
                ('publish_status',
                 models.CharField(blank=True, choices=[('DRAFT', 'DRAFT'), ('LIVE', 'LIVE')], default='DRAFT',
                                  help_text='Select publish status', max_length=20, null=True,
                                  verbose_name='Publish status')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Defaults to filename, if left blank', max_length=255,
                                          null=True)),
                ('file', models.FileField(upload_to='uploads/summernote')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.TextField(blank=True, help_text='Enter post ID', max_length=300, null=True)),
                ('post_type', models.CharField(blank=True, choices=[('article', 'article'), ('question', 'question'),
                                                                    ('category', 'category')], default='article',
                                               help_text='Select post type', max_length=20, null=True,
                                               verbose_name='Post type')),
                ('media_type',
                 models.CharField(blank=True, help_text='Media type like attachment, thumbnail', max_length=255,
                                  null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.SlugField(help_text='Enter key', max_length=150, unique=True)),
                ('value', models.TextField(help_text='Enter value', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('post_id', models.IntegerField(help_text='Post id')),
                ('post_type', models.CharField(choices=[('question', 'question'), ('article', 'article')],
                                               help_text='Select content type', max_length=20,
                                               verbose_name='Content type')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationToken',
            fields=[
                ('uuid',
                 models.UUIDField(db_index=True, default=uuid.uuid4, help_text='A unique identifier for the instance.',
                                  primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('token_type',
                 models.CharField(choices=[('signup', 'signup'), ('login', 'login')], help_text='Token type',
                                  max_length=20, verbose_name='Token type')),
                ('time_created',
                 models.DateTimeField(auto_now_add=True, help_text='The time that the token was created.',
                                      verbose_name='creation time')),
                ('token',
                 models.CharField(help_text='The random token identifying the verification request.', max_length=48,
                                  unique=True, verbose_name='token')),
                ('user', models.ForeignKey(help_text='The user who owns the email address.',
                                           on_delete=django.db.models.deletion.CASCADE, related_name='email_addresses',
                                           related_query_name='email_address', to=settings.AUTH_USER_MODEL,
                                           verbose_name='user')),
            ],
            options={
                'verbose_name': 'verification token',
                'verbose_name_plural': 'verifications tokens',
                'db_table': 'bloggy_verification_token',
                'ordering': ('time_created',),
            },
        ),
        migrations.CreateModel(
            name='UserQuizScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('score', models.FloatField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggy.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('confirmed', models.BooleanField(default=False, null=True)),
                ('confirmation_code', models.CharField(blank=True, default=None,
                                                       help_text='The random token identifying the verification request.',
                                                       max_length=48, null=True, verbose_name='token')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                           related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, help_text='Enter description', null=True)),
                ('explanation', models.TextField(blank=True, help_text='Enter explanation', null=True)),
                ('type', models.CharField(blank=True, choices=[('binary', 'binary'), ('multiple', 'multiple')],
                                          default='binary', help_text='Select type of question', max_length=20,
                                          null=True, verbose_name='Question type')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to='bloggy.article')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggy.quizquestion')),
            ],
        ),
        migrations.CreateModel(
            name='PostMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meta_key', models.SlugField(help_text='Enter key', max_length=150)),
                ('meta_value', models.TextField(help_text='Enter value', null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggy.article')),
            ],
            options={
                'verbose_name': 'Post metadata',
                'verbose_name_plural': 'Post metadata',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('display_order', models.IntegerField(default=0, help_text='Display order', null=True)),
                ('title', models.CharField(help_text='Enter title', max_length=300)),
                ('keywords', models.CharField(blank=True, help_text='Enter title', max_length=300, null=True)),
                ('publish_status',
                 models.CharField(blank=True, choices=[('DRAFT', 'DRAFT'), ('LIVE', 'LIVE'), ('DELETED', 'DELETED')],
                                  default='DRAFT', help_text='Select publish status', max_length=20, null=True,
                                  verbose_name='Publish status')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(help_text='Enter slug', max_length=150, unique=True)),
                ('excerpt', models.CharField(blank=True, help_text='Enter excerpt', max_length=500, null=True)),
                ('difficulty', models.CharField(blank=True,
                                                choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'),
                                                         ('advance', 'advance')], default='easy',
                                                help_text='Select difficulty', max_length=20, null=True,
                                                verbose_name='Difficulty level')),
                ('is_featured', models.BooleanField(default=False, help_text='Is featured')),
                ('description', models.TextField(help_text='Enter answer', null=True)),
                ('thumbnail',
                 models.ImageField(blank=True, null=True, upload_to=bloggy.models.course.upload_thumbnail_image)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses',
                                             to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, to='bloggy.category')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ['-display_order'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_author_name', models.TextField(blank=True, null=True)),
                ('comment_author_email', models.TextField(blank=True, null=True)),
                ('comment_author_url', models.TextField(blank=True, null=True)),
                ('comment_author_ip', models.GenericIPAddressField(blank=True, default='0.0.0.0', null=True)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('parent',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reply_set',
                                   to='bloggy.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                           to='bloggy.article')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['comment_date'],
            },
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('post_id', models.IntegerField(help_text='Post id')),
                ('post_type', models.CharField(choices=[('question', 'question'), ('article', 'article')],
                                               help_text='Select content type', max_length=20,
                                               verbose_name='Content type')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='bloggy.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='bloggy.course'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['slug', 'publish_status', 'published_date'], name='bloggy_cour_slug_7b04ce_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['slug', 'publish_status', 'post_type', 'published_date'],
                               name='bloggy_arti_slug_0a0597_idx'),
        ),
    ]
