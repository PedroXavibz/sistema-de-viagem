"""
Escreve e acessa dados do arquivo motorista.json
"""

from . import model

FILE_NAME: str = 'motorista'


def get_all() -> list[dict[str, any]]:
    """
    Pega todas informações sobre os motoristas

    Returns:
        list[dict[str, any]]:
    """
    result: list[dict[str, any]] = model.find(filename=FILE_NAME)
    return result


def get_by_cpf(value: str) -> list[dict[str, any]]:
    """
    Acessa um motorista por meio do cpf

    Args:
        value:

    Returns:
        list[dict[str, any]]:
    """
    query: dict[str, any] = {
        'field': 'cpf',
        'eq': value
    }
    result: list[dict[str, any]] = model.find(filename=FILE_NAME, query=query)
    return result


def get_by_license(value: str) -> list[dict[str, any]]:
    """
    Filtra os motoristas que possuem um tipo especifico de carteira

    Args:
        value:

    Returns:
        list[dict[str, any]]:
    """
    query: dict[str, any] = {
        'field': 'carteira',
        'eq': value
    }
    result = model.find(filename=FILE_NAME, query=query)
    return result


def add_driver(data: dict[str, str]) -> bool:
    """
    Adicionar um novo motorista

    Args:
        data:

    Returns:
        bool:
    """
    result: list[dict[str, any]] = get_by_cpf(value=data['cpf'])
    driver_already_exist: bool = len(result) != 0

    is_successfull: bool = True

    if driver_already_exist:
        is_successfull = False
        return is_successfull

    model.insert(filename=FILE_NAME, data=data)
    return is_successfull


def update_driver(data: dict[str, str]) -> None:
    """
    Alterar dados do motorista

    Args:
        data:

    Returns:
        None:
    """
    model.update(filename=FILE_NAME, data=data)


def remove_driver(user_id: str) -> None:
    """
    Remove um motorista

    Args:
        user_id:

    Returns:
        None:
    """
    query: dict[str, any] = {
        'field': 'id',
        'ne': user_id
    }

    model.delete(filename=FILE_NAME, query=query)
