from django.db import models
from django.contrib.auth.models import User
import datetime


class System(models.Model):
    class Meta:
        verbose_name_plural = 'システム'

    name = models.CharField(max_length=50, verbose_name='システム名')
    start_date = models.DateField(default=datetime.date.today, verbose_name='開始日')
    end_date = models.DateField(blank=True, null=True, verbose_name='終了日')
    users = models.ManyToManyField(User, verbose_name='システムユーザ', related_name='attendances')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="マネジャー",
                                related_name='manager')

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name_plural = 'タグ'

    name = models.CharField(max_length=50, verbose_name='タグ名')

    def __str__(self):
        return self.name


class Qa(models.Model):
    class Meta:
        verbose_name_plural = 'QA'
        ordering = ['-update_datetime']

    system = models.ForeignKey(System, on_delete=models.CASCADE, verbose_name='システム')
    function = models.CharField(max_length=100, null=False, blank=False,
                                verbose_name='機能')
    priority = models.CharField(choices=(('3', '高'), ('2', '中'), ('1', '低')), max_length=1, verbose_name='優先度')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='質問者', related_name='sender')
    send_datetime = models.DateTimeField(auto_now=True, verbose_name='質問日時')
    expect_answer_date = models.DateField(verbose_name='回答希望日')
    expect_answer_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='回答希望者',
                                           related_name='expect_answer_user')
    title = models.CharField(max_length=50, verbose_name='質問概要', db_index=True)
    detail = models.TextField(verbose_name='質問詳細')
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='回答者', null=True,
                                   related_name='respondent')
    answer = models.TextField(verbose_name='回答詳細', null=True)
    answer_datetime = models.DateTimeField(null=True, verbose_name='回答日時')
    status = models.CharField(choices=(('1', '起票'), ('2', '回答完了'), ('3', '確認完了'), ('4', '保留'), ('5', '廃棄')),
                              default='1', max_length=1,
                              verbose_name='ステータス', db_index=True)
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新日時', db_index=True)
    tags = models.ManyToManyField(Tag, 'タッグ')

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'コメント'

    qa = models.ForeignKey(Qa, on_delete=models.CASCADE, verbose_name='QA')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='送信者')
    content = models.TextField(verbose_name='内容')
    insert_datetime = models.DateTimeField(auto_now=True, verbose_name='送信日時')

    def __str__(self):
        if len(self.content) > 10:
            return self.content[:10] + '...'
        else:
            return self.content
