from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.

class UserModel(models.Model):
    """
    Модель, которая содержит расширение для стандартной модели пользователя веб-платформы
    """

    user = models.ForeignKey(
        db_column='user_db_column',
        db_index=True,
        db_tablespace='user_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
        related_name='user',
    )
    password = models.CharField(
        db_column='password_db_column',
        db_index=True,
        db_tablespace='password_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Пароль',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    is_active_account = models.BooleanField(
        db_column='is_active_account_db_column',
        db_index=True,
        db_tablespace='is_active_account_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
        verbose_name='Активность аккаунта',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    email = models.EmailField(
        db_column='email_db_column',
        db_index=True,
        db_tablespace='email_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Почта',
        help_text='<small class="text-muted">EmailField [0, 300]</small><hr><br>',

        max_length=300,
    )
    secret_question = models.CharField(
        db_column='secret_question_db_column',
        db_index=True,
        db_tablespace='secret_question_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Секретный вопрос',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    secret_answer = models.CharField(
        db_column='secret_answer_db_column',
        db_index=True,
        db_tablespace='secret_answer_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Секретный ответ',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    is_temp_password = models.BooleanField(
        db_column='is_temp_password_db_column',
        db_index=True,
        db_tablespace='is_temp_password_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
        verbose_name='Пароль не изменён',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    last_name = models.CharField(
        db_column='last_name_db_column',
        db_index=True,
        db_tablespace='last_name_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Фамилия',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    first_name = models.CharField(
        db_column='first_char_db_column',
        db_index=True,
        db_tablespace='first_char_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Имя',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    patronymic = models.CharField(
        db_column='patronymic_db_column',
        db_index=True,
        db_tablespace='patronymic_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Отчество',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    personnel_number = models.SlugField(
        db_column='personnel_number_db_column',
        db_index=True,
        db_tablespace='personnel_number_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Табельный номер',
        help_text='<small class="text-muted">SlugField [0, 300]</small><hr><br>',

        max_length=300,
        allow_unicode=False,
    )
    subdivision = models.CharField(
        db_column='subdivision_db_column',
        db_index=True,
        db_tablespace='subdivision_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Подразделение',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    workshop_service = models.CharField(
        db_column='workshop_service_db_column',
        db_index=True,
        db_tablespace='workshop_service_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Цех/Служба',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    department_site = models.CharField(
        db_column='department_site_db_column',
        db_index=True,
        db_tablespace='department_site_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Отдел/Участок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    position = models.CharField(
        db_column='position_db_column',
        db_index=True,
        db_tablespace='position_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Должность',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    category = models.CharField(
        db_column='category_db_column',
        db_index=True,
        db_tablespace='category_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Категория',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    education = models.TextField(
        db_column='education_db_column',
        db_index=True,
        db_tablespace='education_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Образование',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    achievements = models.TextField(
        db_column='achievements_db_column',
        db_index=True,
        db_tablespace='achievements_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Достижения',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    biography = models.TextField(
        db_column='biography_db_column',
        db_index=True,
        db_tablespace='biography_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Биография',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    hobbies = models.TextField(
        db_column='hobbies_db_column',
        db_index=True,
        db_tablespace='hobbies_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Увлечения',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    image = models.ImageField(
        db_column='image_db_column',
        db_index=True,
        db_tablespace='image_db_tablespace',
        error_messages=False,
        validators=[FileExtensionValidator(['jpg', 'png'])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='default/account/default_avatar.jpg',
        verbose_name='Изображение',
        help_text='<small class="text-muted"ImageField [jpg, png]</small><hr><br>',

        upload_to='uploads/admin/account/avatar',
        max_length=200,
    )

    class Meta:
        app_label = 'backend'
        ordering = ('-id',)
        verbose_name = 'Пользователь расширение'
        verbose_name_plural = 'Admin 1, Пользователи расширение'
        db_table = 'user_extend_model_table'

    def __str__(self):
        if self.is_active_account:
            is_active_account = 'Активен'
        else:
            is_active_account = 'Неактивен'
        return f'{self.last_name} | {self.first_name} | {is_active_account} | {self.personnel_number} | ' \
               f'{self.position} | {self.id} | {self.user}'


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    if created:
        try:
            UserModel.objects.get_or_create(user=instance)
        except Exception as error:
            pass


class Category(models.Model):
    title = models.CharField(
        db_column='title_db_column',
        db_index=True,
        db_tablespace='title_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )


class Post(models.Model):
    """
    Модель Post
    """
    author = models.ForeignKey(
        db_column='author_db_column',
        db_index=True,
        db_tablespace='author_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=UserModel,
        on_delete=models.SET_NULL,
        related_name='idea_author',
    )
    title = models.CharField(
        db_column='title_db_column',
        db_index=True,
        db_tablespace='title_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    description = models.TextField(
        db_column='description_db_column',
        db_index=True,
        db_tablespace='description_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name='Описание',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    is_completed = models.BooleanField(
        db_column='is_completed_db_column',
        db_index=True,
        db_tablespace='is_completed_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Статус выполнения',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    image = models.ImageField(
        db_column='image_db_column',
        db_index=True,
        db_tablespace='image_db_tablespace',
        error_messages=False,
        validators=[FileExtensionValidator(['jpg', 'png'])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='uploads/rational/default_rational.jpg',
        verbose_name='Изображение',
        help_text='<small class="text-muted">ImageField [jpg, png]</small><hr><br>',

        upload_to='uploads/rational/avatar/',
        max_length=200,
    )
    additional_file = models.FileField(
        db_column='additional_file_db_column',
        db_index=True,
        db_tablespace='additional_file_db_tablespace',
        error_messages=False,
        validators=[FileExtensionValidator(['docx', 'doc'])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Прикрепляемый файл',
        help_text='<small class="text-muted">FileField</small><hr><br>',

        upload_to='uploads/rational/files/',
        max_length=200,
    )
    created = models.DateTimeField(
        db_column='created_db_column',
        db_index=True,
        db_tablespace='created_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )
    updated = models.DateTimeField(
        db_column='updated_db_column',
        db_index=True,
        db_tablespace='updated_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время обновления',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'app_django'
        ordering = ('-updated',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post_post_list_model_table'

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.title} | {self.description[0:30]}... | {completed} | {self.updated}"
