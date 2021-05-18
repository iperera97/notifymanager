import inspect

from .import utils
from .import constants


class SubscriberMetaClass(type):

    notify_on_args = constants.NOTIFY_METHOD_ARGS

    def __new__(cls, *args, **kwargs):
        """Override to validate notify arguments"""
        new_class = super().__new__(cls, *args, **kwargs)
        cls.validate_notify_args(new_class)
        return new_class

    @classmethod
    def validate_notify_args(cls, sub_class):
        """Validate the notify args in notify methods

        Args:
            sub_class (class)

        Raises:
            NotifyMeException: if not valid arguments for notify methods
        """
        notify_methods = utils.get_callable_notify_methods(sub_class)

        for method in notify_methods:
            required_args = inspect.getfullargspec(method).args
            required_args.remove("self")

            if cls.notify_on_args != required_args:
                err_msg = f"{method.__name__} required following args {cls.notify_on_args}"  # noqa
                raise utils.NotifyMeException(err_msg)


class BaseSubscriber(metaclass=SubscriberMetaClass):

    subsriber_name = None

    def __init__(self, name, *args, **kwargs):
        self.subsriber_name = name

    def __str__(self):
        return f"{self.subsriber_name}"

    def get_unique_name(self):
        return f"{self.subsriber_name}_{id(self)}"

    def notify_on_http(self, msg, data_msg):
        print("notify_on_http")