import os

from django.core.management import call_command
from django.test import TestCase
import shutil

BASE_DIR = os.path.dirname(__file__)
LOCALE = 'en'
PO_FILE = 'locale/%s/LC_MESSAGES/django.po' % LOCALE

class MakeMessagesXGetTextTestCase(TestCase):

    def setUp(self):
        self.test_project_dir = os.path.abspath(os.path.join(BASE_DIR, '../'))
        self.locale_dir = os.path.abspath(os.path.join(BASE_DIR, '../locale'))

    def test_makemessages_xgettext(self):
        # Change Working Directory before calling the command
        os.chdir(self.test_project_dir)

        # Silently generate en locale files
        call_command('makemessagesxgettext', locale=[LOCALE], verbosity=0,)

        # Validate that it's created
        self.assertTrue(os.path.exists(PO_FILE))

        # Remove locale tree folder
        shutil.rmtree(self.locale_dir)

    def test_makemessages_xgettext_add_location_file(self):
        # Change Working Directory before calling the command
        os.chdir(self.test_project_dir)

        # Silently generate en locale files
        call_command('makemessagesxgettext', locale=[LOCALE], verbosity=0,
                     xgettext=['--add-location=file'])

        # Validate that it's created
        self.assertTrue(os.path.exists(PO_FILE))

        with open(PO_FILE, 'r', encoding='utf-8') as po_file:
            for line in (
                    line for line in po_file.readlines()
                    if line.startswith('#:')):
                # Check to see if the : separator (file:loc) is not there
                self.assertNotIn(':', line[2:])

        # Remove locale tree folder
        shutil.rmtree(self.locale_dir)




