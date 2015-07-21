from optparse import make_option
from django.core.management.commands import makemessages


class Command(makemessages.Command):

    option_list = makemessages.Command.option_list + (
        make_option('--xgettext',
                    default=[], dest='xgettext', action='append',
                    help='Passes arguments to the xgettext command (e.g. '
                         '--add-location=file). Use multiple times to pass '
                         'additional arguments.'
                    ),
    )

    def handle_noargs(self, *args, **options):
        xgettext_cmd_options = options.pop('xgettext')

        for option in xgettext_cmd_options:
            self.xgettext_options = self.xgettext_options[:] + [option]

        super(Command, self).handle_noargs(*args, **options)
