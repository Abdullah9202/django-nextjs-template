import os
import shutil


def clean_project(apps_to_clean, base_dir):
    """
    Iterate over specified apps in the project and perform cleanup:
    - Delete `__pycache__` folders.
    - Delete all files in `migrations/` except `__init__.py`.

    :param apps_to_clean: List of app names to clean (e.g., ['proposals', 'projects'])
    :param base_dir: The base directory of your Django project
    """
    for app in apps_to_clean:
        app_path = os.path.join(base_dir, app)

        if not os.path.exists(app_path):
            print(f"App '{app}' not found in: {base_dir}")
            continue

        # Delete __pycache__ folders in the app
        for root, dirs, files in os.walk(app_path):
            if "__pycache__" in dirs:
                pycache_path = os.path.join(root, "__pycache__")
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")

        # Handle migrations folder files
        migrations_path = os.path.join(app_path, "migrations")
        if os.path.exists(migrations_path):
            for filename in os.listdir(migrations_path):
                file_path = os.path.join(migrations_path, filename)
                if filename != "__init__.py" and os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")


if __name__ == "__main__":
    # List of apps to clean
    apps_to_clean = []

    # Base directory path
    base_dir = os.path.dirname(__file__)

    clean_project(apps_to_clean, base_dir)
    print("Cleanup complete!")