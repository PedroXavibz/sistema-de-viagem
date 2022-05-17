"""
Manipula a entrada dos usuários e exibi novos
submenus com opção de cadastro, edição e busca
"""

from ..config import menu_motorista_opts
from ..utils import handle_input
from ..models import motorista_model
from ..views import motorista_view, view
from ..controllers import menu_principal_controller


MENU_MAX_OPTS: int = menu_motorista_opts['MAX_OPTIONS']
CADASTRAR_MOTORISTA: int = menu_motorista_opts['CADASTRAR_MOTORISTA']
BUSCAR_MOTORISTA_POR_CPF: int = menu_motorista_opts['BUSCAR_MOTORISTA_POR_CPF']
LISTAR_POR_CARTEIRA: int = menu_motorista_opts['LISTAR_POR_CARTEIRA']
LISTAR_TODOS: int = menu_motorista_opts['LISTAR_TODOS']
VOLTAR_AO_MENU_PRINCIPAL: int = menu_motorista_opts['SAIR']


def create_driver() -> None:
    """
    Exibi o menu de cadastro de motorista e pede ao usuário
    as informações para o cadastro do mesmo

    Returns:
        None:
    """
    while True:
        stop: bool = True
        motorista_view.show_cadastro_de_motorista()

        data: dict[str, str] = {
            'nome': handle_input.form(msg='Nome: '),
            'cpf': handle_input.form(msg='CPF: '),
            'carteira': handle_input.form(msg='Tipo de carteira: ', expected=['A', 'B', 'AB'])
        }

        is_success: bool = motorista_model.add_driver(data=data)

        if not is_success:
            msg: str = 'Motorista já cadastrado'
            view.warning_msg(msg=msg)
        else:
            nome: str = data['nome']
            msg = f'Novo motorista "{nome}" cadastrado com sucesso'
            view.sucess_msg(msg=msg)

        create_another: bool = handle_input.confirm(
            msg='Deseja criar outro motorista')

        if create_another:
            stop = False

        if stop:
            break


def handle_edit_remove_menu(result: list[dict[str, any]]):
    """
    Manipula as entradas de seleção de menu para criação ou remoção de motoristas

    Args:
        result:
    """
    def _update_driver_(data: dict[str, any]) -> None:
        """
        Alterar dados do motorista

        Args:
            data [str, any]:

        Returns:
            None:
        """
        usr_id: str = data['id']
        usr_name: str = data['nome']
        usr_license: str = data['carteira']

        edit_name: bool = handle_input.confirm('Deseja Editar o nome')
        if edit_name:
            usr_name = handle_input.form(msg='Nome: ')

        edit_license: bool = handle_input.confirm(
            'Deseja Editar o tipo de carteira')
        if edit_license:
            usr_license = handle_input.form(
                msg='Tipo de carteira: ', expected=['A', 'B', 'AB'])

        data: dict[str, str] = {
            'id': usr_id,
            'nome': usr_name,
            'carteira': usr_license
        }

        if edit_name or edit_license:
            motorista_model.update_driver(data=data)
            view.sucess_msg(msg='Motorista alterado com sucesso')

    def _remove_driver_(cur_user_id: str) -> None:
        """
        Remover motorista

        Args:
            cur_user_id (str):

        Returns:
            None:
        """
        remove_drive = handle_input.confirm(msg='Deseja remover motorista')

        if remove_drive:
            motorista_model.remove_driver(user_id=cur_user_id)
            view.sucess_msg(msg='Motorista removido com sucesso')

    view.render_menu_edit_remove()

    edit_menu: dict[str, int] = {
        'opt_edit': 1,
        'opt_remove': 2,
        'opt_exit': 3,
        'max_options': 3
    }

    user_opt: int = handle_input.menu(menu_max_opts=edit_menu['max_options'])

    if user_opt == edit_menu['opt_exit']:
        load_menu()
        return

    if user_opt == edit_menu['opt_remove']:
        user_id = result[0]['id']
        _remove_driver_(cur_user_id=user_id)

    if user_opt == edit_menu['opt_edit']:
        user_data = result[0]
        _update_driver_(data=user_data)


def search_driver_by_cpf() -> None:
    """
    Filtrando motorista por CPF

    Returns:
        None:
    """
    while True:
        stop: bool = True
        value = handle_input.form(msg='CPF: ')
        result = motorista_model.get_by_cpf(value=value)

        view.render_search_results(search_result=result)

        empty_results = len(result) == 0

        if empty_results:
            try_again: bool = handle_input.confirm(
                'Deseja fazer um outra consulta')
            if try_again:
                stop = False
        else:
            handle_edit_remove_menu(result)

        if stop:
            break


def search_by_license() -> None:
    """
    Filtrando motorista por tipo de carteira

    Returns:
        None:
    """
    while True:
        stop = True

        value = handle_input.form(
            msg='Tipo de carteira: ', expected=['A', 'B', 'AB'])
        result = motorista_model.get_by_license(value=value)
        view.render_search_results(search_result=result)

        search_again = handle_input.confirm(
            'Pesquisar por outro tipo de carteira')

        if search_again:
            stop = False

        if stop:
            break


def list_all_drivers() -> None:
    """
    Recuperando todos os dados dos motorista

    Returns:
        None:
    """
    result = motorista_model.get_all()
    view.render_search_results(search_result=result)


menu_opts = {
    CADASTRAR_MOTORISTA: create_driver,
    BUSCAR_MOTORISTA_POR_CPF: search_driver_by_cpf,
    LISTAR_POR_CARTEIRA: search_by_license,
    LISTAR_TODOS: list_all_drivers,
}


def load_menu() -> None:
    """
    Exibi o menu de motorista e pede ao usuário
    escolher uma das opções do menu

    Returns:
        None:
    """
    motorista_view.show()

    user_opt = handle_input.menu(menu_max_opts=MENU_MAX_OPTS)

    if user_opt == VOLTAR_AO_MENU_PRINCIPAL:
        view.exit_msg(msg='Voltando ao menu principal')
        menu_principal_controller.load_menu()
        return

    menu_opts[user_opt]()

    handle_input.enter_to_continue()
    load_menu()
