from django.core.management.base import BaseCommand
from django.utils.timezone import now
from polls.models import Question


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("questions", type=int)

    def handle(
        self,
        *args,
        questions,
        **options,
    ):
        for _ in range(questions):
            q = Question.objects.create(question_text="42", pub_date=now())
            self.stdout.write(
                self.style.SUCCESS('Successfully created Question with ID "%s"' % q.id)
            )
