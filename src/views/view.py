"""
Implementação de UI
"""

from datetime import datetime
import os
import sys
import time

import colorama

COLOR_PRIMARY = colorama.Fore.BLUE
COLOR_SECONDARY = colorama.Fore.LIGHTYELLOW_EX
COLOR_WARNING = colorama.Fore.YELLOW
COLOR_SUCCESS = colorama.Fore.GREEN
COLOR_RED = colorama.Fore.LIGHTRED_EX

BOLD = colorama.Style.BRIGHT
RESET_COLOR = colorama.Style.RESET_ALL


def _load_clean_animation_() -> None:
    """
    Renderiza uma animação de lazzy load no terminal

    Returns:
        None:
    """
    animation: list[str] = [
        '[■□□□□□□□□□]', '[■■□□□□□□□□]',
        '[■■■□□□□□□□]', '[■■■■□□□□□□]',
        '[■■■■■□□□□□]', '[■■■■■■□□□□]',
        '[■■■■■■■□□□]', '[■■■■■■■■□□]',
        '[■■■■■■■■■□]', '[■■■■■■■■■■]'
    ]

    for i in range(10):
        time.sleep(0.1)

        sys.stdout.write(
            f' \r{COLOR_SUCCESS}Loading {COLOR_RED}{animation[i % len(animation)]}{RESET_COLOR}')

        sys.stdout.flush()


def clear_terminal(animation: bool = True) -> None:
    """
    Limpa a última saída do terminal

    Args:
        animation:

    Returns:
        None:
    """
    if animation:
        _load_clean_animation_()

    os.system('cls' if os.name == 'nt' else 'clear')


def beautiful_input_msg(icon: str, msg: str) -> str:
    """
    Exibi mensagens coloridas na entrada de dados

    Args:
        icon:
        msg:

    Returns:
        str:
    """
    msg = f' {COLOR_SECONDARY}{icon} {RESET_COLOR}{COLOR_PRIMARY} {msg}{RESET_COLOR}'
    return msg


def sucess_msg(msg: str) -> None:
    """
    Exibi mensagens coloridas quando algo ocorreu de forma esperada

    Args:
        msg:

    Returns:
        None:
    """
    now: datetime = datetime.now()
    current_time: str = now.strftime('%H:%M:%S')
    print(
        f' {COLOR_PRIMARY}[{current_time}] {COLOR_SUCCESS}{msg}  {RESET_COLOR}')


def warning_msg(msg: str) -> None:
    """
    Exibi mensagens coloridas de aviso ao usuário

    Args:
        msg:

    Returns:
        None:
    """
    print(f' {COLOR_WARNING}{msg}  {RESET_COLOR}')


def exit_msg(msg: str, wait: float = 1) -> None:
    """
    Exibi mensagens toda vez que o usuário decide sair do menu atual,
    indicando para onde ele será redirecionado

    Args:
        wait:
        msg:
        wait:

    Returns:
        None:
    """
    print(f' {COLOR_PRIMARY}{msg} שּ {RESET_COLOR}')
    time.sleep(wait)


def render_menu(title: str, menu_opts: list[dict[str, any]]) -> None:
    """
    Exibi um menu de aplicação CLI

    Args:
        title: str
        menu_opts: dict[str, any]

    Returns:
        None:
    """
    clear_terminal()

    print(f' {BOLD}{COLOR_PRIMARY}{title.upper().center(50)}{RESET_COLOR}')

    print(f' {COLOR_SECONDARY}'.ljust(50, '═'))

    for value in menu_opts:
        index: str = value['index']
        opt_menu_title: str = value['title']
        icon: str = value['icon']

        print(
            f' {COLOR_SECONDARY} {RESET_COLOR}{COLOR_PRIMARY}[{index}]  {opt_menu_title} '
            f' {icon} {RESET_COLOR}')

    print(f' {COLOR_SECONDARY}'.ljust(25, ''))
    print()


def _render_boders_(align: int, columns: str, rows: str) -> str:
    """
    Cria bordas

    Args:
        align:
        columns:
        rows:

    Returns:
        str:
    """
    borders: str = f'{columns}' + f'{rows}' * align + f'{columns} '
    return borders


def _render_text_(align: int, text: str, columns: str, upper: bool = False) -> str:
    """
    cria textos com bordas

    Args:
        align:
        text:
        columns:
        upper:

    Returns:
        str:
    """
    if upper:
        new_text: str = f'{columns}' + f'{text}'.upper().center(align) + \
            f'{columns} '
    else:
        new_text: str = f'{columns}' + f'{text}'.center(align) + \
            f'{columns} '
    return new_text


def render_search_results(search_result: list[dict[str, any]]) -> None:
    """
    Exibi um menu de fácil leitura de dados que foram resgatados
    de funções de pesquisa e filtragem

    Args:
        search_result:

    Returns:
        None:
    """
    clear_terminal(animation=False)

    amount_of_results: int = len(search_result)

    if amount_of_results == 0:
        warning_msg(msg='Nenhum resultado encontrado')
        return

    header_titles = search_result[0].keys()
    body_items = []

    for i in range(amount_of_results):
        cur_loop_items = []
        for key in header_titles:
            is_id_key = key == 'id'
            if not is_id_key:
                cur_loop_obj = search_result[i]
                cur_loop_items.append(cur_loop_obj[key])
        body_items.append(cur_loop_items)

    # header
    title = ''
    borders = ''
    align = 25

    for text in header_titles:
        if text != 'id':
            title += _render_text_(align=align, text=text,
                                   columns='|', upper=True)
            borders += _render_boders_(align=align,
                                       columns='|', rows='═')

    print(f' {COLOR_SECONDARY}'.ljust(25, ''))

    print(f'{COLOR_PRIMARY}{borders}')
    print(f'{COLOR_SECONDARY}{title}')
    print(f'{COLOR_PRIMARY}{borders}')

    # body
    body = ''
    borders = ''

    for items in body_items:
        for text in items:
            body += _render_text_(align=align, text=text, columns='|')
            borders += _render_boders_(align=align, columns='|', rows='-')
        print(body)
        print(borders)

        body = ''
        borders = ''

    sucess_msg(msg='Foram encontrados os seguintes dados')


def render_menu_edit_remove() -> None:
    """
    Menu com opções de edição e remoção

    Returns:
        None:
    """
    print(f'\n {COLOR_SECONDARY}'.ljust(50, '═'))

    print(
        f' {COLOR_SECONDARY} {RESET_COLOR}{COLOR_PRIMARY}[1]  Editar ')
    print(
        f' {COLOR_SECONDARY} {RESET_COLOR}{COLOR_PRIMARY}[2]  Remover ﯊')
    print(
        f' {COLOR_SECONDARY} {RESET_COLOR}{COLOR_PRIMARY}[3]  Sair ')

    print(f' {COLOR_SECONDARY}'.ljust(25, ''))
