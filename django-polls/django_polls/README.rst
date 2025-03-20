=============
django-polls
=============

django-polls é um aplicativo Django para conduzir enquetes baseadas na web. Para cada
pergunta, os visitantes podem escolher entre um número fixo de respostas.

A documentação detalhada está no diretório "docs".

Quick start
-----------

1. Add "polls" em seu INSTALLED_APPS setting, desta forma::
    INSTALLED_APPS = [
        ...,
        "django_polls",
    ]

2. Inclua o polls URLconf no urls.py do seu projeto, desta forma::
    path("polls/", include("django_polls.urls")),

3. Run ``python manage.py migrate`` para criar os models.

4. Start o servidor de desenvolvimento e visite o admin para criar uma enquete

5. Visite o ``/polls/`` URL para participar da enquete