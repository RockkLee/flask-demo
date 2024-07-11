import os
import importlib.util

from flask_demo.orm.database import Base, engine
from flask_demo.orm.models import get_models_dir


def _import_all_modules_from_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module_path = os.path.join(directory, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            globals()[module_name] = module


def create_tables():
    # import all models
    current_directory = get_models_dir()
    _import_all_modules_from_dir(current_directory)

    Base.metadata.create_all(bind=engine)
    print(Base.metadata.tables.keys())
    print(current_directory)


if __name__ == "__main__":
    create_tables()
