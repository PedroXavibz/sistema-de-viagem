"""
Menu principal da aplicação
"""

from src.views.view import render_menu
from .. import config

_MENU_UI_ = {
    'title': 'Menu ',
    'interface': {
        'motorista': {
            'index': config.main_menu_opts.get('MOTORISTA'),
            'title': 'Menu motorista',
            'icon': ''
        },
        'veiculo': {
            'index': config.main_menu_opts.get('VEICULO'),
            'title': 'Menu veiculo',
            'icon': 'ﲦ'
        },
        'viagem': {
            'index': config.main_menu_opts.get('VIAGEM'),
            'title': 'Menu viagem',
            'icon': ''
        },
        'sair': {
            'index': config.main_menu_opts.get('SAIR'),
            'title': 'Sair',
            'icon': ''
        }
    }
}


def show() -> None:
    """
    Exibi o menu principal

    Returns:
        None:
    """

    title: str = _MENU_UI_.get('title')

    menu_opts = _MENU_UI_.get('interface').values()

    render_menu(title=title, menu_opts=menu_opts)
