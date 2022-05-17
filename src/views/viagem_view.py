"""
Menu de viagem
"""

from .view import render_menu
from ..config import menu_viagem_opts


MENU_VIAGEM = {
    'title': 'Menu de viagem ',
    'interface': {
        'criar_viagem': {
            'index': menu_viagem_opts.get('CRIAR_VIAGEM'),
            'title': 'Criar viagem',
            'icon': '惘'
        },
        'finalizar_viagem_por_placa': {
            'index': menu_viagem_opts.get('FINALIZAR_VIAGEM_POR_PLACA'),
            'title': 'Finalizar viagem por placa',
            'icon': '賈'
        },
        'viagens_ativas': {
            'index': menu_viagem_opts.get('VIAGENS_ATIVAS'),
            'title': 'Viagens ativas',
            'icon': '車'
        },
        'veiculos_em_viagem': {
            'index': menu_viagem_opts.get('VEICULOS_EM_VIAGEM'),
            'title': 'Veículos que estão em viagem',
            'icon': '  '
        },
        'veiculos_disponiveis': {
            'index': menu_viagem_opts.get('VEICULOS_DISPONIVEIS'),
            'title': 'Veículos que estão disponíveis para viagem',
            'icon': ''
        },
        'listar_todas_as_viagens': {
            'index': menu_viagem_opts.get('LISTAR_TODAS_AS_VIAGENS'),
            'title': 'Listar todas as viagens',
            'icon': '陼 惘'
        },
        'listar_viagens_por_periodo': {
            'index': menu_viagem_opts.get('LISTAR_VIAGENS_POR_PERIODO'),
            'title': 'Listar todas as viagens por período',
            'icon': ''
        },
        'sair': {
            'index': menu_viagem_opts.get('SAIR'),
            'title': 'Voltar ao menu principal',
            'icon': ''
        }
    }
}


def show() -> None:
    """
    Exibi o menu principal de viagem

    Returns:
        None:
    """
    title = MENU_VIAGEM['title']

    menu_opts = MENU_VIAGEM['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)


MENU_CADASTRAR_VIAGEM = {
    'title': 'Criar viagem ',
    'interface': {
        'placa': {
            'index': 1,
            'title': 'Placa do veículo',
            'icon': ''
        },
        'rota': {
            'index': 2,
            'title': 'Rota',
            'icon': ''
        },
        'data': {
            'index': 3,
            'title': 'Data',
            'icon': ''
        },
    }
}


def show_menu_add_travel() -> None:
    """
    Exibi o menu para cadastro de viagem

    Returns:
        None:
    """
    title = MENU_CADASTRAR_VIAGEM['title']
    menu_opts = MENU_CADASTRAR_VIAGEM['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)
