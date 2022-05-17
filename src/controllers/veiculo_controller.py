"""
Manipula a entrada dos usuários e exibi novos
submenus com opção de cadastro, edição e busca
"""

from typing import Callable

from .. import config
from src.utils import handle_input
from src.models import veiculo_model, motorista_model, model
from src.views import view, veiculo_view
from src.controllers import menu_principal_controller


MAX_OPTIONS: int = config.menu_veiculo_opts['MAX_OPTIONS']

CADASTRAR_VEICULO: int = config.menu_veiculo_opts['CADASTRAR_VEICULO']
BUSCAR_PLACA: int = config.menu_veiculo_opts['BUSCAR_PLACA']
LISTAR_VEICULOS_COM_MOTORISTAS: int = config.menu_veiculo_opts['LISTAR_VEICULOS_COM_MOTORISTAS']
LISTAR_VEICULOS_SEM_MOTORISTAS: int = config.menu_veiculo_opts['LISTAR_VEICULOS_SEM_MOTORISTAS']
VOLTAR_AO_MENU_PRINCIPAL: int = config.menu_veiculo_opts['SAIR']


def create_vehicle() -> None:
    """
    Exibi o menu de cadastro de veiculo e pede ao usuário
    as informações para o cadastro do mesmo

    Returns:
        None:
    """
    while True:
        stop: bool = True

        veiculo_view.show_menu_add_vehicle()

        # Dados do veiculo
        data: dict[str, any] = {
            'placa': handle_input.form(msg='Placa: '),
            'tipo': handle_input.form(msg='Tipo: ', expected=['MOTO', 'CARRO']),
            'motorista': None
        }

        is_successful: bool = veiculo_model.add_vehicle(data=data)

        if is_successful:
            view.sucess_msg(msg='Veículo criado com sucesso')
        else:
            view.warning_msg(msg='Veículo já foi cadastrado')

        create_another: bool = handle_input.confirm(msg='Cadastrar outro veículo')
        if create_another:
            stop = False

        if stop:
            break


def handle_edit_remove_menu(data):
    """
    Manipula as entradas de seleção de menu para criação ou remoção de motoristas
    """

    def _update_vehicle_(cur_data: dict[str, any]) -> None:
        """
        Alterar dados do veiculo

        Args:
            cur_data: dict[str, any]

        Returns:
            None:
        """
        vehicle_driver: object = cur_data['motorista']

        if vehicle_driver:
            confirm_remove_driver = handle_input.confirm(msg='Remover motorista')

            if confirm_remove_driver:
                cur_data.update({'motorista': None})
                view.sucess_msg(msg='Motorista removido com sucesso')
            return

        confirm_add_driver = handle_input.confirm(msg='Adicionar motorista')

        if confirm_add_driver:
            while True:
                stop: bool = True

                new_driver = handle_input.form(msg='CPF do motorista: ')

                driver = model.search_between_modules(
                    motorista_model.get_by_cpf, param=new_driver)

                driver_exists = len(driver) != 0

                has_vehicle = False
                vehicles = veiculo_model.get_all_vehicles_with_drivers()
                if len(vehicles) != 0:
                    for vehicle in vehicles:
                        if vehicle['motorista'] == cur_data['motorista']:
                            has_vehicle = True

                if not driver_exists:
                    view.warning_msg(msg='Motorista não existe')

                if has_vehicle:
                    view.warning_msg(msg='Motorista já possui um veículo')

                if not has_vehicle and driver_exists:
                    cur_data.update({'motorista': new_driver})
                    veiculo_model.update_vehicle(data=cur_data)
                    view.sucess_msg(msg='Motorista adicionado com sucesso')
                    break

                try_again = handle_input.confirm('Tentar novamente')
                if try_again:
                    stop = False

                if stop:
                    break

    def _remove_vehicle_(user_id: str) -> None:
        """
        Remover veiculo

        Args:
            user_id:

        Returns:
            None:
        """
        confirm_delete: bool = handle_input.confirm(msg='Deseja remover este veículo')

        if confirm_delete:
            veiculo_model.remove_vehicle(user_id=user_id)
            view.sucess_msg(msg='Veículo removido com sucesso')

    view.render_menu_edit_remove()

    edit_menu_max_options: int = 3
    user_opt: int = handle_input.menu(menu_max_opts=edit_menu_max_options)

    opt_edit: int = 1
    opt_remove: int = 2
    opt_exit: int = 3

    if user_opt == opt_exit:
        load_menu()
        return

    if user_opt == opt_edit:
        _update_vehicle_(cur_data=data)

    if user_opt == opt_remove:
        _remove_vehicle_(user_id=data['id'])


def search_by_license_plate() -> None:
    """
    Filtrando veiculo por placa

    Returns:
        None:
    """
    value: str = handle_input.form(msg='Placa: ')
    result: list[dict[str, any]] = veiculo_model.get_by_license_plate(value=value)

    view.render_search_results(search_result=result)

    if len(result) > 0:
        handle_edit_remove_menu(data=result[0])


def search_all_vehicles_with_drivers() -> None:
    """
    Filtrando todos os veiculos que possuem motorista

    Returns:
        None:
    """
    result: list[dict[str, any]] = veiculo_model.get_all_vehicles_with_drivers()

    view.render_search_results(search_result=result)


def search_all_vehicles_without_drivers() -> None:
    """
    Filtrando todos os veiculos que não possuem motorista

    Returns:
        None:
    """
    result: list[dict[str, any]] = veiculo_model.get_all_vehicles_without_drivers()

    view.render_search_results(search_result=result)


menu_opts: dict[int, Callable[[], None] | Callable[[], None] | Callable[[], None] | Callable[[], None]] = {
    CADASTRAR_VEICULO: create_vehicle,
    BUSCAR_PLACA: search_by_license_plate,
    LISTAR_VEICULOS_COM_MOTORISTAS: search_all_vehicles_with_drivers,
    LISTAR_VEICULOS_SEM_MOTORISTAS: search_all_vehicles_without_drivers,
}


def load_menu() -> None:
    """
    Exibi o menu de veiculo e pede ao usuário
    escolher uma das opções do menu

    Returns:
        None:
    """
    veiculo_view.show()

    user_opt: int = handle_input.menu(menu_max_opts=MAX_OPTIONS)

    if user_opt == VOLTAR_AO_MENU_PRINCIPAL:
        view.exit_msg(msg='Voltando ao menu principal')
        menu_principal_controller.load_menu()
        return

    menu_opts[user_opt]()

    handle_input.enter_to_continue()
    load_menu()
