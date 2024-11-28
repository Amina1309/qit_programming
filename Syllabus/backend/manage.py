#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matrix_project.settings')
    
    try:
        # Import execute_from_command_line from Django management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Provide a helpful error message if Django isn't installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute Django management commands
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()