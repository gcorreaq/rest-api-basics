from datetime import datetime

from models.events import Event


def create_event(data_store: list[Event], name: str, start_datetime: datetime, end_datetime: datetime, location: str, description: str) -> Event:
    """Crea un nuevo evento y lo agrega a `data_store`

    :param data_store:
    :param name:
    :param start_datetime:
    :param end_datetime:
    :param location:
    :param description:
    :return:
    """
    pass


def get_event():
    pass


def update_event():
    pass


def delete_event():
    pass
