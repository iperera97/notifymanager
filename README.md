# notifymanager

notifymanager is a simple package that can be used to manage notifications in python application.
it's mainly used observer design pattern.

```
from notifymanager import BaseSubject, BaseSubscriber, publish_msg

# create subject
flash_sales_subject = BaseSubject(name="flash_sales")

# create subclass using the base Subscriber
class FlashSaleSubscriber(BaseSubscriber):

    def notify_on_email(self, msg, data_msg):
        pass


# create first subsriber
subsriber_1 = FlashSaleSubscriber()

# subsribe to the subject
subsribe_by = ["notify_on_email"] # default "all"
flash_sales_subject.subsribe(subsriber_1, subsribe_by)

# publish message to the subject
publish_msg(flash_sales_subject, "50% discount for X product")



```