import os
import importlib.util

Commands = {}

commands_dir = os.path.join(os.path.dirname(__file__), 'modules')

for fn in os.listdir(commands_dir):
    if fn.endswith('.py') and fn != '__init__.py':
        module_name = fn[:-3]
        spec = importlib.util.spec_from_file_location(module_name, os.path.join(commands_dir, fn))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        Commands[module.metadata['name']] = module