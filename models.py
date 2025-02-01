from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)

    def save(self, *args, **kwargs):
        translator = Translator()
        languages = ['hi', 'bn']
        for lang in languages:
            for field_type in ['question', 'answer']:
                field = f'{field_type}_{lang}'
                if not getattr(self, field):
                    try:
                        translated = translator.translate(
                            getattr(self, f'{field_type}_en'), dest=lang
                        )
                        setattr(self, field, translated.text)
                    except:
                        setattr(self, field, getattr(self, f'{field_type}_en'))
        super().save(*args, **kwargs)