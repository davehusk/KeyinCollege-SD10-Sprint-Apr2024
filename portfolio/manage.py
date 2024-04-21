#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """
    Run administrative tasks.

    This function sets the Django settings module and executes the command line arguments.

    Raises:
        ImportError: If Django is not installed or the settings are incorrect.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. pip install django or check your settings."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
