from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CblUserManager(BaseUserManager):
    def create_user(self, email,  first, last, phone, gender, password):
        if not email:
            raise ValueError("E-mail cannot be empty")

        if not first:
            raise ValueError("Name cannot be empty")

        if not last:
            raise ValueError("last cannot be empty")

        if not password:
            raise ValueError('Password cannot be empty')

        if not phone:
            raise ValueError('Phone cannot be empty')

        email = self.normalize_email(email)

        user = self.model(first=first, last=last, email=email,
                          phone=phone, gender=gender)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first, last, phone, gender, password):
        if not email:
            raise ValueError("E-mail cannot be empty")

        if not first:
            raise ValueError("Name cannot be empty")

        if not last:
            raise ValueError("last cannot be empty")

        if not password:
            raise ValueError('Password cannot be empty')

        if not phone:
            raise ValueError('Phone cannot be empty')

        email = self.normalize_email(email)

        user = self.model(first=first, last=last, email=email,
                          phone=phone, gender=gender)

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CblUser(AbstractBaseUser, PermissionsMixin):
    gender = (('male', 'Male'), ('female', 'Female'))
    country = (('egypt', 'EGYPT'), ('usa', 'USA'), ('germany', 'Germany'))

    def get_countries():
        with open('countries') as target:
            pass
    email = models.EmailField(unique=True,
                              max_length=250,
                              verbose_name='user email',
                              help_text='enter a valid user mail',
                              error_messages={
                                  "invalid": 'Cannot email be empty'
                              }
                              )
    first = models.CharField(max_length=250, verbose_name='first name',
                             help_text='enter a valid first name',
                             )
    last = models.CharField(max_length=250, verbose_name='last name',
                            help_text='enter a valid last name',
                            )
    phone = models.CharField(max_length=20, unique=True,
                             help_text='enter a valid phone number',
                             )
    gender = models.CharField(max_length=6, choices=gender, default='male',
                              help_text='select a gender',
                              )
    country = models.CharField(max_length=100, choices=country ,
                              help_text='select a country', 
                               )
    address = models.CharField(max_length=200,  blank=True, 
                              help_text='enter a valid address', 
                               )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    objects = CblUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first', 'last', 'gender', 'phone']

    def user_name(self) -> str:
        return self.first + ' '+self.last

    def __str__(self) -> str:
        return self.user_name()
