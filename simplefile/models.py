import os
import uuid

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from .validators import validate_file_extension, validate_pdf_file
from utils.utils import uuid_to_hex

fs = FileSystemStorage(location=settings.SENDFILE_ROOT)


class SimpleFile(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    file = models.FileField(verbose_name='File', upload_to='uploads/')

    class Meta:
        db_table = 'simple_file'

    def __str__(self):
        return self.title


class SimpleFileCustom(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    file = models.FileField(verbose_name='File', upload_to='uploads/', storage=fs)

    class Meta:
        db_table = 'simple_file_custom'

    def __str__(self):
        return self.title

    def __delete_file(self):
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)

    def save(self, path=None, *args, **kwargs):

        # path = kwargs.pop('path', None)
        # is_overwrite = kwargs.pop('overwrite', None)

        if self.file:
            name, ext = os.path.splitext(self.file.name)
            new_name = f"{str(uuid.uuid4()).replace('-', '')}{ext}"

            if path:
                new_path = settings.SENDFILE_ROOT + path
                if not os.path.exists(new_path):
                    os.makedirs(os.path.dirname(new_path))
                new_name = f"{new_path}{new_name}"

            self.file.name = new_name

            # # TODO Melhor fazer a exlusão lógica e manter sempre o arquivo
            # if is_overwrite and os.path.isfile(self.file.name):
            #     print('fazer a exclusão lógica')
            #     # self.__delete_file()

            super().save(*args, **kwargs)


class SimpleUploadValidation(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    file = models.FileField(verbose_name='File', upload_to='uploads/', storage=fs,
                            validators=[validate_file_extension])

    class Meta:
        db_table = 'simple_file_validation'

    def __str__(self):
        return self.title

    def save(self, path=None, *args, **kwargs):

        if self.file:
            name, ext = os.path.splitext(self.file.name)
            new_name = f"{str(uuid.uuid4()).replace('-', '')}{ext}"
            if path:
                new_path = settings.SENDFILE_ROOT + path
                if not os.path.exists(new_path):
                    os.makedirs(os.path.dirname(new_path))
                if os.path.isfile(new_path):
                    os.rename(new_path, new_name)
                new_name = f"{path}/{new_name}"
                # new_name = f"{new_path}{new_name}"
                # if os.path.isfile(initial_path):
                #     os.makedirs(initial_path, new_path)

                # new_name = f"{new_path}{new_name}"

            self.file.name = new_name

            # # TODO Melhor fazer a exlusão lógica e manter sempre o arquivo
            # if is_overwrite and os.path.isfile(self.file.name):
            #     print('fazer a exclusão lógica')
            #     # self.__delete_file()

            super().save(*args, **kwargs)


# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
# path = default_storage.save('path/to/file', ContentFile(b'new content'))


class SimpleFileDetails(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    identifier = models.UUIDField(verbose_name='Identifier', default=uuid.uuid4())
    file = models.FileField(verbose_name='File', upload_to='uploads/', storage=fs,
                            validators=[validate_file_extension])
    name = models.CharField(max_length=255, verbose_name='Name')
    hash_name = models.CharField(max_length=255, verbose_name='Hash name')
    extension = models.CharField(max_length=10, verbose_name='Extension')
    size = models.IntegerField(verbose_name='Size')
    content_type = models.CharField(max_length=100, verbose_name='Content Type')
    full_path = models.CharField(max_length=255, blank=True, verbose_name='Full Path')

    class Meta:
        db_table = 'simple_file_detail'

    def __str__(self):
        return f"{self.title} - {self.name}.{self.extension}"

    def make_private(self, path):
        try:
            self.full_path += path
            if not os.path.exists(self.full_path):
                os.makedirs(os.path.dirname(self.full_path))
            self.file.name = f"{path}/{self.hash_name}"
        except Exception as e:
            raise

    def save(self, path=None, *args, **kwargs):
        self.name = self.file.name
        name, ext = os.path.splitext(self.file.name)
        self.hash_name = f"{uuid_to_hex(uuid.uuid4().__str__())}{ext}"
        self.file.name = self.hash_name
        self.extension = ext[1:]
        self.size = self.file.size
        self.content_type = self.file.file.content_type
        self.full_path = f"{settings.SENDFILE_ROOT}{self.file.field.upload_to}"

        if path:
            self.make_private(path)

        super().save(*args, **kwargs)


class SimpleFileId(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    identifier = models.UUIDField(verbose_name='Identifier', default=uuid.uuid4())
    file = models.FileField(verbose_name='File', upload_to='uploads/', storage=fs,
                            validators=[validate_file_extension])
    name = models.CharField(max_length=255, verbose_name='Name')
    hash_name = models.CharField(max_length=255, verbose_name='Hash name')
    extension = models.CharField(max_length=10, verbose_name='Extension')
    size = models.IntegerField(verbose_name='Size')
    content_type = models.CharField(max_length=100, verbose_name='Content Type')
    full_path = models.CharField(max_length=255, blank=True, verbose_name='Full Path')

    class Meta:
        db_table = 'simple_file_id'

    def __str__(self):
        return f"{self.title} - {self.name}.{self.extension}"

    def make_private(self, path):
        try:
            self.full_path += f"{path}/{self.pk}/"
            if not os.path.exists(self.full_path):
                os.makedirs(os.path.dirname(self.full_path))

            new_name = f"{path}/{self.pk}/{self.hash_name}"
            if os.path.isfile(self.full_path):
                os.rename(self.full_path, new_name)

            self.file.name = new_name
        except Exception as e:
            raise

    def save(self, path=None, *args, **kwargs):
        self.name = self.file.name
        name, ext = os.path.splitext(self.file.name)
        self.hash_name = f"{uuid_to_hex(uuid.uuid4().__str__())}{ext}"
        self.extension = ext[1:]
        self.size = self.file.size
        self.content_type = self.file.file.content_type
        file = self.file
        self.file = None

        # TODO Melhorar a persistência usando PK
        super(SimpleFileId, self).save()
        self.file = file
        self.full_path = f"{settings.SENDFILE_ROOT}{self.file.field.upload_to}{self.pk}"
        self.file.name = f"{self.pk}/{self.hash_name}"
        if path:
            self.make_private(path)

        super().save(*args, **kwargs)
