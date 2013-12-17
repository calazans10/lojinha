#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    DJANGO_SETTINGS = os.environ.get('DJANGO_SETTINGS')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
