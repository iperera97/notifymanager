import pytest

from notifyme.subject import BaseSubject
from notifyme.subscriber import BaseSubscriber
from notifyme import utils as notify_utils


@pytest.fixture
def new_subject():
    subject_name = "flash_sales"
    flash_sales = BaseSubject(name=subject_name)
    all_subsribers = flash_sales.get_all_subscribers()
    
    assert len(all_subsribers) == 0
    assert flash_sales.subject_name == subject_name
    return flash_sales

@pytest.fixture
def new_subsriber():
    sub_name = "admin"
    subscriber = BaseSubscriber(name=sub_name)
    
    assert subscriber.subsriber_name == sub_name
    return subscriber


def test_create_subscription(new_subject, new_subsriber):
    first_time_sub = new_subject.subscribe(new_subsriber)
    second_time_sub = new_subject.subscribe(new_subsriber)
    all_subsribers = new_subject.get_all_subscribers()

    assert first_time_sub == True
    assert not second_time_sub
    assert len(all_subsribers) == 1

    first_time_unsub = new_subject.unsubscribe(new_subsriber)
    second_time_unsub = new_subject.unsubscribe(new_subsriber)

    assert first_time_unsub == True
    assert not second_time_unsub
    assert len(all_subsribers) == 0

    new_subject.subscribe(new_subsriber)
    new_subject.unsubscribe_all()

    assert len(all_subsribers) == 0


def test_publish_msg(new_subject, new_subsriber):
    new_subject.subscribe(new_subsriber)
    msg = "new data source come"
    data_msg = {"user_id": 100}
    
    notify_response = notify_utils.publish_msg(new_subject, msg, data_msg)
    print(notify_response)
