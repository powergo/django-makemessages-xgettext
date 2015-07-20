from django.core.management.commands import makemessages


class Command(makemessages.Command):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--xgettext', '-X',
                            default=[], dest='xgettext', action='append',
                            help='Passes arguments to the xgettext command '
                                 '(e.g. --add-location=file). Use multiple '
                                 'times to pass additional arguments.')

    def handle(self, *args, **options):
        xgettext_cmd_options = options.pop('xgettext')
        
        for option in xgettext_cmd_options:
            self.xgettext_options = self.xgettext_options[:] + [option]

        super(Command, self).handle(*args, **options)