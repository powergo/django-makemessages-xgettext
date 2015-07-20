import io
import os
import shutil

from django.core.management import call_command
from django.test import TestCase

BASE_DIR = os.path.dirname(__file__)
LOCALE = 'en'
PO_FILE = 'locale/%s/LC_MESSAGES/django.po' % LOCALE


class MakeMessagesXGetTextTestCase(TestCase):

    def setUp(self):
        self.test_project_dir = os.path.abspath(os.path.join(BASE_DIR, '../'))
        self.locale_dir = os.path.abspath(os.path.join(BASE_DIR, '../locale'))

    def test_makemessages_xgettext(self):
        # Silently generate en locale files
        call_command('makemessagesxgettext', locale=[LOCALE],)

        # Validate that it's created
        self.assertTrue(os.path.exists(PO_FILE))

        # Remove locale tree folder
        shutil.rmtree(self.locale_dir)

    def test_makemessages_xgettext_add_location_file(self):
        # Silently generate en locale files
        call_command('makemessagesxgettext', locale=[LOCALE], xgettext=['--no-location'])

        # Validate that it's created
        self.assertTrue(os.path.exists(PO_FILE))

        with io.open(PO_FILE, 'r', encoding='utf-8') as po_file:
            for line in (
                    line for line in po_file.readlines()
                    if line.startswith('#:')):
                # Check to see if the : separator (file:loc) is not there
                self.assertNotIn(':', line[2:])

        # Remove locale tree folder
        shutil.rmtree(self.locale_dir)
