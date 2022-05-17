"""
Menu de motorista
"""
from src.views.view import render_menu
from .. import config

MENU_MOTORISTA = {
    'title': 'Menu motorista ',
    'interface': {
        'cadastrar_motorista': {
            'index': config.menu_motorista_opts.get('CADASTRAR_MOTORISTA'),
            'title': 'Cadastrar motorista',
            'icon': ''
        },
        'buscar_motorista_por_cpf': {
            'index': config.menu_motorista_opts.get('BUSCAR_MOTORISTA_POR_CPF'),
            'title': 'Buscar motorista por CPF',
            'icon': ''
        },
        'listar_por_carteira': {
            'index': config.menu_motorista_opts.get('LISTAR_POR_CARTEIRA'),
            'title': 'Listar todos os motorista por tipo da carteira',
            'icon': ''
        },
        'listar_todos': {
            'index': config.menu_motorista_opts.get('LISTAR_TODOS'),
            'title': 'Listar todos os motorista',
            'icon': ''
        },
        'sair': {
            'index': config.menu_motorista_opts.get('SAIR'),
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

    title = MENU_MOTORISTA['title']

    menu_opts = MENU_MOTORISTA['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)


MENU_CADASTRAR_MOTORISTA = {
    'title': 'Cadastrar motorista  ',
    'interface': {
        'campo_nome': {
            'index': 1,
            'title': 'Nome',
            'icon': ''
        },
        'campo_cpf': {
            'index': 2,
            'title': 'CPF',
            'icon': ''
        },
        'campo_carteira': {
            'index': 3,
            'title': 'Carteira [A, B, AB]',
            'icon': ''
        }
    }
}


def show_cadastro_de_motorista() -> None:
    """
    Exibi o menu de cadastro de motorista

    Returns:
        None:
    """
    title = MENU_CADASTRAR_MOTORISTA['title']
    menu_opts = MENU_CADASTRAR_MOTORISTA['interface'].values()

    render_menu(title=title, menu_opts=menu_opts)
