from django.db import models


class TagGroup(models.Model):
    name = models.TextField()


class Tag(models.Model):
    name = models.TextField()
    group = models.ForeignKey(TagGroup, on_delete=models.CASCADE)
    locmap = models.TextField()


class Note(models.Model):
    tags = models.ManyToManyField(Tag)


class NoteText(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.TextField()