"""
Manipulando entradas do usuário
"""

import re
import typing
from src.views.view import beautiful_input_msg, warning_msg


def _handle_empty_inputs_(input_msg: str) -> str:
    """
    Evita valores de entrada vazios

    Returns:
        str:
    """
    user_opt: str = input(input_msg)

    if not user_opt:
        while True:
            warning_msg(msg='Valor não pode ser vazio')
            user_opt = input(input_msg)
            if user_opt:
                break

    return user_opt


def enter_to_continue() -> None:
    """
    Espera a entra do usuário para excutar a próxima ação

    Returns:
        None:
    """
    input_msg: str = beautiful_input_msg(
        icon='', msg='Pressione enter para continuar...')
    print()
    input(input_msg)


def menu(menu_max_opts: int) -> int:
    """
    Essa função isola erros de entrada do usuário quando o valor de entrada for maior
    ou menor do que a quantidade de opções disponíveis de menu

    Args:
        menu_max_opts:

    Returns:
        int:
    """
    input_msg: str = beautiful_input_msg(
        icon='[ ﴕ ]', msg='Digite uma das opções acima: ')

    while True:
        try:
            user_opt: int = int(input(input_msg))
        except ValueError:
            warning_msg(msg='Digite um número')
            continue

        if user_opt > menu_max_opts or user_opt <= 0:
            warning: str = f'"{user_opt}" não é um valor válido'

            warning_msg(msg=warning)
        else:
            return user_opt


def confirm(msg: str) -> bool:
    """
    Confirmar mensagem com S ou N

    Args:
        msg: str

    Returns:
        bool:
    """
    msg: str = f'{msg}? [S/N] '
    input_msg: str = beautiful_input_msg(icon='', msg=msg)

    result: bool = True

    while True:
        stop: bool = False
        user_opt: str = input(input_msg)

        if user_opt in 'Ss':
            stop, result = True, True

        if user_opt in 'Nn':
            stop, result = True, False

        if stop:
            break

    return result


def form(msg: str, expected: object = None, regex: typing.Optional[str] = None,
         regex_model: typing.Optional[str] = None) -> str:
    """
    Manipula valores de entrada para formulários

    Args:
        msg: str
        expected:  object = None
        regex: regex: Optional[str] = None
        regex_model: Optional[str] = None) -> str

    Returns:
        str:
    """
    input_msg: str = beautiful_input_msg(icon='', msg=msg)
    user_opt: str = _handle_empty_inputs_(input_msg=input_msg)

    # Só retorna o valor de entrada se o mesmo for fornecido de forma esperada
    while True:
        stop = True
        if not expected or user_opt in expected:
            pass
        else:
            warn: str = f'"{user_opt}" não é um valor válido, são valores validos: {expected}'
            warning_msg(msg=warn)

            user_opt = _handle_empty_inputs_(input_msg=input_msg)

            stop = False

        if regex:
            is_match: typing.Match[str] | None = re.search(regex, user_opt)

            if not is_match:
                warn = f'"{user_opt}" não é um formato válido use {regex_model}'
                warning_msg(msg=warn)
                user_opt = _handle_empty_inputs_(input_msg=input_msg)
                stop = False

        if stop:
            break

    return user_opt
