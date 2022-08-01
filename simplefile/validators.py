import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_file_extension(value):
    LIMIT = 5 * 1024 * 1024

    ext = str(os.path.splitext(value.name)[1]).lower()  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

    if value.size > LIMIT:
        raise ValidationError(_('Fle too large. Sze should not exceed 5 MB'))


def validate_pdf_file(value):
    LIMIT = 5 * 1024 * 1024
    validate_extensions = ['.pdf']
    ext = str(os.path.splitext(value.name)[1]).lower()
    if ext not in validate_extensions:
        raise ValidationError(_("File type supported! Only PDF files are accepted."))

    if value.size > LIMIT:
        raise ValidationError(_('Fle too large. Sze should not exceed 5 MB'))
