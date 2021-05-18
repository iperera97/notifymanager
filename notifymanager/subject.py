from .import utils
from .import constants


class BaseSubject:
    """Base Subject Blueprint for create a subject"""
    subject_name = None

    def __init__(self, name):
        self.subject_name = name
        self._subscribers = {}

    def __str__(self):
        return f"{self.subject_name}"

    def subscribe(self, subscriber, notify_attrs=None):
        """Subsribe to the subject

        Args:
            subscriber (object): subscriber
            notify_attrs (list, None):. notify methods on subscriber.
            Defaults to None.

        Raises:
            NotifyMeException: if notify mehthods empty

        Returns:
            bool: True if subscribed otherwise False
        """
        notify_methods = []
        if not notify_attrs:
            notify_attrs = [constants.NOTIFY_ALL_METHODS]

        if constants.NOTIFY_ALL_METHODS in notify_attrs:
            notify_attrs = utils.get_notify_attrs(subscriber)

        notify_methods = utils.get_callable_notify_methods(
            subscriber, notify_attrs
        )

        if not notify_methods:
            raise utils.NotifyMeException("notify methods not found")

        self._subscribers[subscriber] = notify_methods
        return True

    def unsubscribe(self, subscriber):
        """Unsubsribe from the subject

        Args:
            subsriber (object): subscriber

        Returns:
            bool: True if successfully unsubscribed otherwise False
        """
        if subscriber in self._subscribers:
            self._subscribers.pop(subscriber)
            return True

    def unsubscribe_all(self):
        self._subscribers.clear()

    def get_all_subscribers(self):
        return self._subscribers

    def notify(self, msg, data_msg=None):
        """Notify a message to all subscribers

        Args:
            msg (str): published message
            data_msg (dict): published data message

        Returns:
            dict: notify response for each subscriber
        """
        notify_response = {}
        if not data_msg:
            data_msg = {}

        data_msg["subject_name"] = self.subject_name

        for sub, notify_methods in self._subscribers.items():
            sub_name = sub.get_unique_name()
            notify_response[sub_name] = [
                utils.add_logger(each_method)(msg, data_msg)
                for each_method in notify_methods
            ]

        return notify_response
