import glob
import importlib
import os

models_dir = os.path.dirname(__file__)

model_files = glob.glob(os.path.join(models_dir, "**", "*.py"), recursive=True)

for model_file in model_files:
    module_name = os.path.relpath(model_file, models_dir)[:-3].replace(
        os.sep, "."
    )
    if module_name != "__init__":
        importlib.import_module(f"school.models.{module_name}")
