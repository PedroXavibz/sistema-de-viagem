"""
Escreve e acessa dados do arquivo viagem.json
"""

from datetime import datetime

from ..utils import date_convert
from . import model

FILE_NAME: str = 'viagem'


def get_all_travels() -> list[dict[str, any]]:
    """
    Busca por todas as viagens

    Returns:
        list[dict[str, any]]:
    """
    result: list[dict[str, any]] = model.find(filename=FILE_NAME)

    return result


def get_travels_by_period(from_period: datetime, to_period: datetime) -> list[dict[str, any]]:
    """
    Filtra viagens por periodo

    Args:
        from_period:
        to_period:

    Returns:
        list[dict[str, any]]:
    """
    travels: list[dict[str, any]] = get_all_travels()

    filtered_travels: list[dict[str, any]] = []
    if len(travels) == 0:
        return filtered_travels

    for travel in travels:
        travel_date: datetime = date_convert.convert_string_to_date(string=travel['data'])

        if from_period <= travel_date <= to_period:
            filtered_travels.append(travel)

    return filtered_travels


def get_current_travels() -> list[dict[str, any]]:
    """
    Filtra as viagens ativas

    Returns:
        list[dict[str, any]]:
    """
    query: dict[str, any] = {
        'field': 'status',
        'eq': True
    }

    result: list[dict[str, any]] = model.find(filename=FILE_NAME, query=query)

    return result


def get_vehicules_in_travel() -> list[str]:
    """
    Filtra os veiculos que estão em viagens

    Returns:
        list[str]:
    """
    result: list[dict[str, any]] = get_current_travels()

    vehicules: list[str] = []

    if len(result) > 0:
        for item in result:
            vehicules.append(item['veiculo'])

    return vehicules


def add_travel(data: dict[str, any]) -> bool:
    """
    Adicionar uma nova viagem

    Args:
        data:

    Returns:
        bool:
    """
    vehicules: list[str] = get_vehicules_in_travel()

    vehicule_avaliable: bool = True

    for vehicule in vehicules:
        if data['veiculo'] == vehicule:
            vehicule_avaliable = False
            return vehicule_avaliable

    model.insert(filename=FILE_NAME, data=data)

    return vehicule_avaliable


def update_travel(data: dict[str, any]) -> None:
    """
    Alterar dados da viagem

    Args:
        data:

    Returns:
        None:
    """
    model.update(filename=FILE_NAME, data=data)
