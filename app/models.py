from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Subgroup(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Level(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class AnswerType(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Questions(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    subgroup = models.ForeignKey('Subgroup', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    question = models.TextField()
    answer_type = models.ForeignKey('AnswerType', on_delete=models.CASCADE)
    option_1 = models.TextField(blank=True, null=True)
    option_2 = models.TextField(blank=True, null=True)
    option_3 = models.TextField(blank=True, null=True)
    option_4 = models.TextField(blank=True, null=True)
    answer_text = models.CharField(max_length=300, blank=True, null=True)
    correct_answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.group.title} | {self.subgroup.title} | {self.question} | {self.answer_type}'
