"""
Escreve e acessa dados do arquivo veiculo.json
"""

from . import model

FILE_NAME: str = 'veiculo'


def get_by_license_plate(value: str):
    """
    Filtra os veiculos que possuem um tipo especifico de placa
    """
    query: any[str, any] = {
        'field': 'placa',
        'eq': value
    }

    result = model.find(filename=FILE_NAME, query=query)

    return result


def get_all_vehicles_with_drivers():
    """
    Filtra os veiculos que possuem motorista
    """
    query: dict[str, any] = {
        'field': 'motorista',
        'ne': None
    }

    result = model.find(filename=FILE_NAME, query=query)

    return result


def get_all_vehicles_without_drivers():
    """
    Filtra os veiculos que possuem motorista
    """
    query: dict[str, any] = {
        'field': 'motorista',
        'eq': None
    }

    result = model.find(filename=FILE_NAME, query=query)

    return result


def add_vehicle(data: dict[str, any]) -> bool:
    """
    Adicionar um novo veiculo

    Returns:
        object:
    """
    result = get_by_license_plate(value=data['placa'])

    vehicle_already_exist = len(result) != 0

    is_successfull: bool = True

    if vehicle_already_exist:
        is_successfull = False
        return is_successfull

    model.insert(filename=FILE_NAME, data=data)

    return is_successfull


def update_vehicle(data: dict[str, any]):
    """
    Alterar dados do veiculo
    """
    model.update(filename=FILE_NAME, data=data)


def remove_vehicle(user_id: str):
    """
    Remove um veiculo
    """
    query: dict[str, any] = {
        'field': 'id',
        'ne': user_id
    }

    model.delete(filename=FILE_NAME, query=query)
