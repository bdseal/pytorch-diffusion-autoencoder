import importlib
from inspect import isfunction


def get_class_from_str(string, reload=False):
    if string == "None":

        def noop(*args, **kwargs):
            pass

        return noop

    module, cls = string.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)


def exists(x):
    return x is not None


def default(val, d):
    if exists(val):
        return val
    return d() if isfunction(d) else d
