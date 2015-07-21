import django

if django.get_version().startswith("1.8"):
    from django_makemessages_xgettext import django18_makemessagesxgettext
    Command = django18_makemessagesxgettext.Command

else:
    from django_makemessages_xgettext import django17_makemessagesxgettext
    Command = django17_makemessagesxgettext.Command
