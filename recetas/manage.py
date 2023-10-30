import os
import sys

sys.setrecursionlimit(300)  

def main():
    package_name = os.path.basename(os.path.abspath(__file__)).split('.')[0]


    settings_module = f"{package_name}.settings"

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
