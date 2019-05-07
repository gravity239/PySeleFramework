from importlib import import_module
import sys


class Page:

    @staticmethod
    def get_page(parent_class, *args, **kwargs):
        try:
            if '--run-mode=mobile' in sys.argv:
                module_name = parent_class.__module__ + "_mobile"
                class_name = parent_class.__name__ + "Mobile"
            else:
                module_name = parent_class.__module__ + "_desktop"
                class_name = parent_class.__name__ + "Desktop"
            interface_module = import_module(module_name)
            interface_class = getattr(interface_module, class_name)
            instance = interface_class(*args, **kwargs)
        except (AttributeError, ModuleNotFoundError):
            raise ImportError("{} is not part of our interface collection!".format(module_name))

        return instance
