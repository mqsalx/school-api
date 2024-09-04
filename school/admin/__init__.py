import glob
import importlib
import os

admin_dir = os.path.dirname(__file__)

admin_files = glob.glob(os.path.join(admin_dir, "**", "*.py"), recursive=True)

for admin_file in admin_files:
    module_name = os.path.relpath(admin_file, admin_dir)[:-3].replace(
        os.sep, "."
    )
    if module_name != "__init__":
        try:
            importlib.import_module(f"school.admin.{module_name}")
        except ModuleNotFoundError as e:
            print(f"ADMIN - Erro ao importar o módulo {module_name}: {e}")
