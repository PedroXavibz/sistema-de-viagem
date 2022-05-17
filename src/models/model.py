"""
Implementação da leitura e escrita de dados em arquivos JSON
"""

import uuid
import typing

from ..utils import handle_json

tmp_data: dict[str, list[dict[str, any]]] = {'data': []}


def _get_tmp_data_(filename: str) -> list[dict[str, any]]:
    """
    Pega os dados armazenados na variável temporaria tmp_data

    Args:
        filename: str

    Returns:
        list[dict[str, any]]:
    """
    data: list[dict[str, any]] = tmp_data['data']

    if _is_tmp_data_empty_():
        data = handle_json.read_json(filename=filename)
        tmp_data.update({'data': data})

    return data


def _is_tmp_data_empty_() -> bool:
    """
    Verifica se o array de dados da variáveis tmp_data está vazio

    Returns:
        bool:
    """
    data_arr: list[dict[str, any]] = tmp_data['data']
    is_empty: bool = len(data_arr) == 0

    return is_empty


def _set_tmp_data_(data: any) -> None:
    """
    Insere dados armazenados na variável temporaria tmp_data

    Args:
        data:

    Returns:
        None:
    """
    tmp_data.update({'data': data})


def clear_tmp_data() -> None:
    """
    Limpando os dados armazenados da variável tmp_data

    Returns:
        None:
    """
    if not _is_tmp_data_empty_():
        tmp_data.update({'data': []})


def search_between_modules(search_function: any, param: typing.Optional[any] = None) -> any:
    """
    Faz um pesquisa de dados entre modulos

    Args:
        search_function:
        param:

    Returns:
        Any:
    """
    if param:
        clear_tmp_data()
        result: any = search_function(param)
        clear_tmp_data()
        return result

    clear_tmp_data()
    result: any = search_function()
    clear_tmp_data()

    return result


def _find_eq_(query: dict[str, any]) -> list[dict[str, any]]:
    """
    Filtra todos os itens que são iguais oa valor de busca

    Args:
        query:

    Returns:
        list[dict[str, any]]:
    """
    field: str = query['field']
    value: any = query['eq']
    data: list[dict[str, any]] = query['data']
    result: list[dict[str, any]] = []

    for item in data:
        if item.get(field) == value:
            result.append(item)

    return result


def _find_ne_(query: dict[str, any]) -> list[dict[str, any]]:
    """
    Filtra todos os itens que não são iguais oa valor de busca

    Args:
        query:

    Returns:
        list[dict[str, any]:
    """
    field: str = query['field']
    value: any = query['ne']
    data: list[dict[str, any]] = query['data']
    result: list[dict[str, any]] = []

    for item in data:
        if item.get(field) != value:
            result.append(item)

    return result


def find(filename: str, query: typing.Optional[dict[str, any]] = None) -> list[dict[str, any]]:
    """
    Filtra a informações a serem resgatadas

    Args:
        filename:
        query:

    Returns:
        list[dict[str, any]]:
    """
    data: list[dict[str, any]] = _get_tmp_data_(filename=filename)

    if not query:
        return data

    operator: any = query.keys()

    operations = {
        'eq': _find_eq_,
        'ne': _find_ne_
    }

    query.update({'data': data})

    for k in operator:
        if k in 'field data':
            continue
        data = operations[k](query)

    return data


def insert(filename: str, data: dict[str, any]):
    """
    Inserindo dados no arquivo JSON e na variável temporaria tmp_data

    Args:
        filename:
        data (object):
    """
    data.update({'id': str(uuid.uuid4())})
    all_data: list[dict[str, any]] = _get_tmp_data_(filename=filename)
    all_data.append(data)

    _set_tmp_data_(data=all_data)

    handle_json.write_json(filename=filename, data=tmp_data)


def update(filename: str, data: dict[str, any]):
    """
    Alterando dados no arquivo JSON e na variável temporaria tmp_data
    """
    result = find(filename=filename)
    updated_data: list[dict[str, any] | any] = []

    for item in result:
        if item['id'] == data['id']:
            for key_result in item.keys():
                for data_key in data.keys():
                    if key_result == data_key:
                        item.update({key_result: data[data_key]})
        updated_data.append(item)

    _set_tmp_data_(data=updated_data)

    handle_json.write_json(filename=filename, data=tmp_data)


def delete(filename: str, query: dict[str, any]) -> None:
    """
    Removendo dados no arquivo JSON e na variável temporaria tmp_data

    Args:
        filename:
        query:

    Returns:
        None:
    """
    result: list[dict[str, any]] = find(filename=filename, query=query)
    _set_tmp_data_(data=result)

    handle_json.write_json(filename=filename, data=tmp_data)
