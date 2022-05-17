"""
Responsável por minupular os arquivos JSON
"""

import os
import json


def _get_json_file_location_(filename: str) -> str:
    """
    Retorna a localização de um arquivo JSON armazenado na pasta data

    Args:
        filename:

    Returns:
        str:
    """
    file: str = f'{filename}.json'
    cur_dir: str = os.getcwd()
    file_location: str = os.path.join(cur_dir, 'data', file)

    return file_location


def read_json(filename: str) -> list[[dict[str, any]]]:
    """
    Faz a leitura de arquivos JSON e retorna seus valores armazenados

    Args:
        filename:

    Returns:
        list[[dict[str, any]]]:
    """
    file_location: str = _get_json_file_location_(filename=filename)

    with open(file=file_location, mode='r+', encoding='utf-8') as json_file:
        data: dict[str, any] = json.loads(json_file.read())

    return data['data']


def write_json(filename: str, data: object) -> None:
    """
    Escreve novos dados em arquivos JSON

    Returns:
        None:
    """
    file_location = _get_json_file_location_(filename=filename)

    json_object = json.dumps(obj=data, indent=4)

    with open(file=file_location, mode='w', encoding='utf-8') as json_file:
        json_file.write(json_object)
