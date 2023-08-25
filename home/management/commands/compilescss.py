from django.core.management.base import BaseCommand
import os
import sass

class Command(BaseCommand):
    help = 'Compile SCSS to CSS'

    def handle(self, *args, **options):
        scss_file = 'home/static/scss/styles.scss'  # Adjust the path as needed
        css_file = 'home/static/css/styles.css'  # Adjust the path as needed

        compiled_css = sass.compile(filename=scss_file)

        with open(css_file, 'w') as css_output:
            css_output.write(compiled_css)

        self.stdout.write(self.style.SUCCESS('Successfully compiled SCSS to CSS'))
