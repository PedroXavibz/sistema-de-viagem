"""
Manipula a entrada dos usuários e exibi novos menus
com base nessas entradas
"""

import sys
from typing import Callable

from ..config import main_menu_opts
from ..models import model
from ..views import menu_principal_view, view
from ..controllers import motorista_controller, veiculo_controller, viagem_controller
from ..utils import handle_input


MENU_MAX_OPTS: int = main_menu_opts['MAX_OPTIONS']
MENU_MOTORISTA: int = main_menu_opts['MOTORISTA']
MENU_VEICULO: int = main_menu_opts['VEICULO']
MENU_VIAGEM: int = main_menu_opts['VIAGEM']
EXIT_PROGRAM: int = main_menu_opts['SAIR']

menu_opts: dict[int, Callable[[], None] | Callable[[], None] | Callable[[], None]] = {
    MENU_MOTORISTA: motorista_controller.load_menu,
    MENU_VEICULO: veiculo_controller.load_menu,
    MENU_VIAGEM: viagem_controller.load_menu
}


def load_menu() -> None:
    """
    Exibi o menu principal e pede ao usuário escolher uma das opções
    do menu

    Returns:
        None:
    """
    menu_principal_view.show()

    user_opt = handle_input.menu(menu_max_opts=MENU_MAX_OPTS)

    model.clear_tmp_data()

    if user_opt == EXIT_PROGRAM:
        view.exit_msg(msg='Fim da aplicação, tenha um bom dia', wait=0.5)
        view.clear_terminal()
        sys.exit()

    menu_opts[user_opt]()
