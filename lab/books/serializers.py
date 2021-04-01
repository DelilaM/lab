from rest_framework import serializers
from books.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    authors = serializers.CharField(style={'base_template': 'textarea.html'})
    publisher = serializers.CharField(required=False)
    publication_date = serializers.DateTimeFieldField(choices=LANGUAGE_CHOICES, default='python')
    number_of_pages = serializers.IntegerField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.publicationdate = validated_data.get('publication date', instance.publicationdate)
        instance.numberofpages = validated_data.get('number of pages', instance.numberofpages)
        instance.save()
        return instance

    class BooksSerializer(serializers.ModelSerializer):
        class Meta:
            model = Books
            fields = ['id', 'title', 'authors', 'publisher', 'publication date', 'number of pages']