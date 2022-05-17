"""
Menu de veículo
"""

from .view import render_menu
from ..config import menu_veiculo_opts

MENU_VEICULO = {
    'title': 'Menu de veículo ﲦ',
    'interface': {
        'cadastrar_veiculo': {
            'index': menu_veiculo_opts.get('CADASTRAR_VEICULO'),
            'title': 'Cadastrar veículo',
            'icon': ''
        },
        'buscar_placa': {
            'index': menu_veiculo_opts.get('BUSCAR_PLACA'),
            'title': 'Buscar veículo por placa',
            'icon': ''
        },
        'listar_veiculos_com_motoristas': {
            'index': menu_veiculo_opts.get('LISTAR_VEICULOS_COM_MOTORISTAS'),
            'title': 'Listar veículos com motoristas',
            'icon': '  '
        },
        'listar_veiculos_sem_motoristas': {
            'index': menu_veiculo_opts.get('LISTAR_VEICULOS_SEM_MOTORISTAS'),
            'title': 'Listar veículos sem motoristas',
            'icon': ' '
        },
        'sair': {
            'index': menu_veiculo_opts.get('SAIR'),
            'title': 'Voltar ao menu principal',
            'icon': ''
        }
    }
}


def show() -> None:
    """
    Exibi o menu principal de motorista

    Returns:
        None:
    """
    title = MENU_VEICULO['title']

    menu_opts = MENU_VEICULO['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)


MENU_CADASTRAR_VEICULO = {
    'title': 'Cadastrar veiculo ',
    'interface': {
        'campo_veiculo': {
            'index': 1,
            'title': 'Placa do veículo',
            'icon': ''
        },
        'campo_tipo': {
            'index': 2,
            'title': 'Tipo [CARRO, MOTO]',
            'icon': ''
        },
    }
}


def show_menu_add_vehicle() -> None:
    """
    Exibi o menu para cadastro de veiculo

    Returns:
        None:
    """
    title = MENU_CADASTRAR_VEICULO['title']
    menu_opts = MENU_CADASTRAR_VEICULO['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)
