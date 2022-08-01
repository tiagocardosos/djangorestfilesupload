from rest_framework import serializers
from simplefile.models import (SimpleFile, SimpleFileCustom,
                               SimpleUploadValidation, SimpleFileDetails, SimpleFileId)


class SimpleFileSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SimpleFile


class SimpleFileCustomSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SimpleFileCustom


class SimpleFileValidationSerializers(serializers.ModelSerializer):
    # path = serializers.CharField(read_only=True)

    class Meta:
        fields = ['id', 'title']
        model = SimpleUploadValidation
        read_only_fields = ['file.name', ]

    def create(self, validated_data):
        instance = SimpleUploadValidation(**validated_data)
        # instance.save()
        instance.save(path='novopath/')

        return instance


class SimpleFileDetailsSerializers(serializers.ModelSerializer):
    # path = serializers.CharField(read_only=True)
    # file = serializers.FileField()

    class Meta:
        model = SimpleFileDetails
        fields = ['id', 'title', 'file', 'name', 'hash_name', 'size', 'content_type', 'identifier', 'full_path']
        read_only_fields = ['name', 'hash_name', 'size', 'content_type', 'identifier', 'full_path']
        # write_only_fields = ['file']

    def create(self, validated_data):
        instance = SimpleFileDetails(**validated_data)
        # instance.save()
        instance.save(path='novopath/')

        return instance


class SimpleFileIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = SimpleFileId
        fields = ['id', 'title', 'file', 'name', 'hash_name', 'size', 'content_type', 'identifier', 'full_path']
        read_only_fields = ['name', 'hash_name', 'size', 'content_type', 'identifier', 'full_path']
        # write_only_fields = ['file']

    def create(self, validated_data):
        instance = SimpleFileId(**validated_data)
        # instance.save()
        instance.save(path='xxxy')

        return instance
