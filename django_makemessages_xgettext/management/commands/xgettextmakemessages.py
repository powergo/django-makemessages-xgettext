import django

if django.get_version().startswith("1.8"):
    from django_makemessages_xgettext import django18_xgettextmakemessages
    Command = django18_xgettextmakemessages.Command

else:
    from django_makemessages_xgettext import django17_xgettextmakemessages
    Command = django17_xgettextmakemessages.Command
