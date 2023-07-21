
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator

from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
    EmailValidator
)
from account.helper.enums import RegexPatternEnum
from  warehouse.mixins import TimestampMixin
import secrets
from account.repository.manager import UserManager
class User(AbstractUser, TimestampMixin):
    username = None
    username_validator = UnicodeUsernameValidator()
    secret = models.CharField(
        unique=True,
        max_length=43,
        default=secrets.token_urlsafe,
        editable=False,
        help_text= _(
                    "A user secret key use for encryption and token generation.")
        )
    username = models.CharField(
        _("Username"),
        max_length=25,
        unique=True,
        null= True,
        blank= True,
        validators=[
            username_validator,
            RegexValidator(RegexPatternEnum.USERNAME),
            MaxLengthValidator(25),
            MinLengthValidator(3)
        ],
        error_messages={
            "unique": _("A user with that username already exist."),
            "min_length": _("Username must be at least 3 characters"),
            "max_length": _("Username should have maxim 15 characters"),
            "invalid":_(
                "Username must start with characters, then it "
                "could have numbers and characters and `.`."
                ),
        },
        help_text=_("Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.")
        )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank = True,
        null = True,
        validators=[RegexValidator(RegexPatternEnum.NAME),
                    MaxLengthValidator(15),
                    MinLengthValidator(3)
                    ],
        error_messages={
            "unique": _("A user with that username already exist."),
            "min_length": _("first_name` must be at least 3 characters"),
            "max_length": _("first_name should not be more than 15 characters"),
            "invalid":_(
                "first_name` must start with characters, then it "
                "could have numbers and characters and `.`."
                ),
        },
        help_text=_("Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.")
    )

    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank = True,
        null = True,
        validators=[RegexValidator(RegexPatternEnum.NAME),
                    MaxLengthValidator(15),
                    MinLengthValidator(3)
                    ]
    )

    phone_number = models.CharField(
        _("Phone number"),
        max_length=15,
        validators = [
            RegexValidator(RegexPatternEnum.IRAN_PHONE_NUMBER),
            MaxLengthValidator (15),
            MinLengthValidator (10)
            ],
        unique=True,
        help_text=_("phone number for login")
        )
    email = models.EmailField(
        _("email address"),
        validators=[EmailValidator("Email is invalid")],
        blank = True,
        null = True
    )
    objects = UserManager()
    
    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def email_user(self, subject: str, message: str, from_email: str = None, **kwargs) -> None:
        """
        send an email to the instance user
        """
        return super().email_user(subject, message, from_email=from_email, **kwargs)
    def send_message(self, subject, message):
        """
        send an SMS to the instance user
        """
        raise NotImplementedError

    def send_otp(self):
        """
        send an SMS to the instance user
        """
        raise NotImplementedError
    # @property
    # def username(self):
    #     return self.phone_number
    
    def __str__(self):
        return f'{self.phone_number}'

    def __repr__(self):
        return f'{self.phone_number}'