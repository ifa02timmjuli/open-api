import connexion
import six

from swagger_server.models.entry import Entry  # noqa: E501
from swagger_server.models.entry_entry_id_body import EntryEntryIdBody  # noqa: E501
from swagger_server.models.list_id_entry_body import ListIdEntryBody  # noqa: E501
from swagger_server.models.todolist_body import TodolistBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_body import UserBody  # noqa: E501
from swagger_server import util


def todo_list_list_id_delete(list_id):  # noqa: E501
    """todo_list_list_id_delete

    Löscht eine komplette Todo-Liste mit allen Einträgen. # noqa: E501

    :param list_id: List ID
    :type list_id: str

    :rtype: None
    """
    return 'do some magic!'


def todo_list_list_id_entry_entry_id_delete(list_id, entry_id):  # noqa: E501
    """todo_list_list_id_entry_entry_id_delete

    Löscht einen einzelnen Eintrag einer Todo-Liste. # noqa: E501

    :param list_id: List ID
    :type list_id: str
    :param entry_id: List ID
    :type entry_id: str

    :rtype: None
    """
    return 'do some magic!'


def todo_list_list_id_entry_entry_id_put(body, list_id, entry_id):  # noqa: E501
    """todo_list_list_id_entry_entry_id_put

    Aktualisiert einen bestehenden Eintrag. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param list_id: List ID
    :type list_id: str
    :param entry_id: List ID
    :type entry_id: str

    :rtype: List[Entry]
    """
    if connexion.request.is_json:
        body = EntryEntryIdBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def todo_list_list_id_entry_post(body, list_id):  # noqa: E501
    """todo_list_list_id_entry_post

    Fügt einen Eintrag zu einer bestehenden Todo-Liste hinzu. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param list_id: List ID
    :type list_id: str

    :rtype: List[Entry]
    """
    if connexion.request.is_json:
        body = ListIdEntryBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def todo_list_list_id_get(list_id):  # noqa: E501
    """todo_list_list_id_get

    Liefert alle Einträge einer Todo-Liste zurück. # noqa: E501

    :param list_id: List ID
    :type list_id: str

    :rtype: List[List]
    """
    return 'do some magic!'


def todo_list_post(body):  # noqa: E501
    """todo_list_post

    Fügt eine neue Todo-Liste hinzu. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: List[List]
    """
    if connexion.request.is_json:
        body = TodolistBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_get():  # noqa: E501
    """user_get

    Liefert eine Liste aller Benutzer zurück. # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'


def user_post(body):  # noqa: E501
    """user_post

    Fügt einen neuen Benutzer hinzu. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: List[User]
    """
    if connexion.request.is_json:
        body = UserBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_user_id_delete(user_id):  # noqa: E501
    """user_user_id_delete

    Löscht einen Benutzer. # noqa: E501

    :param user_id: User ID
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'
