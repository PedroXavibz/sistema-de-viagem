"""
Manipula a entrada dos usuários e exibi novos
submenus com opção de cadastro, edição e busca
"""


from datetime import datetime

from ..config import menu_viagem_opts
from ..utils import handle_input, date_convert
from ..models import viagem_model, veiculo_model, model
from ..views import view, viagem_view
from . import menu_principal_controller

MAX_OPTIONS: int = menu_viagem_opts['MAX_OPTIONS']

CRIAR_VIAGEM: int = menu_viagem_opts['CRIAR_VIAGEM']
FINALIZAR_VIAGEM_POR_PLACA: int = menu_viagem_opts['FINALIZAR_VIAGEM_POR_PLACA']
VIAGENS_ATIVAS: int = menu_viagem_opts['VIAGENS_ATIVAS']
VEICULOS_EM_VIAGEM: int = menu_viagem_opts['VEICULOS_EM_VIAGEM']
VEICULOS_DISPONIVEIS: int = menu_viagem_opts['VEICULOS_DISPONIVEIS']
LISTAR_TODAS_AS_VIAGENS: int = menu_viagem_opts['LISTAR_TODAS_AS_VIAGENS']
LISTAR_VIAGENS_POR_PERIODO: int = menu_viagem_opts['LISTAR_VIAGENS_POR_PERIODO']
VOLTAR_AO_MENU_PRINCIPAL: int = menu_viagem_opts['SAIR']


def _verify_if_vehicule_in_without_driver_(data: dict[str, any]) -> bool:
    """
    Verifica se o veiculo que vai ser cadastrado para viagem não esta sem motorista

    Args:
        data: dict[str, any]

    Returns:
        bool:
    """
    # Verificando se o veiculo existe (veiculos que não possuem motorista)
    all_vehicles_without_drivers: list[dict[str, any]] = model.search_between_modules(
        veiculo_model.get_all_vehicles_without_drivers)

    vehicule_in_vehicules_without_driver: bool = False

    if len(all_vehicles_without_drivers) != 0:
        for vehicle in all_vehicles_without_drivers:
            if vehicle['placa'] == data['veiculo']:
                vehicule_in_vehicules_without_driver = vehicle['motorista'] is None
                break

    if vehicule_in_vehicules_without_driver:
        view.warning_msg(msg='Veículo não possui motorista')

    return vehicule_in_vehicules_without_driver


def _verify_if_vehicule_in_with_driver_(data: dict[str, any]) -> bool:
    """
    Verifica se o veiculo que vai ser cadastrado possui motorista e se ele existe

    Args:
        data: dict[str, any]

    Returns:
        bool:
    """
    # Verificando se o veiculo existe (veiculos que possuem motorista)
    all_vehicles_with_drivers: list[dict[str, any]] = model.search_between_modules(
        search_function=veiculo_model.get_all_vehicles_with_drivers)

    vehicule_in_vehicules_with_driver: bool = False

    if len(all_vehicles_with_drivers) != 0:
        for vehicle in all_vehicles_with_drivers:
            if vehicle['placa'] == data['veiculo']:
                vehicule_in_vehicules_with_driver = True
                break

    if not vehicule_in_vehicules_with_driver:
        view.warning_msg(msg='Veículo não existe')

    return vehicule_in_vehicules_with_driver


def create_viagem() -> None:
    """
    Exibi o menu de cadastro de viagem e pede ao usuário
    as informações para o cadastro do mesmo

    Returns:
        None:
    """
    while True:
        stop = True

        viagem_view.show_menu_add_travel()

        # Dados da viagem
        data: dict[str, any] = {
            'veiculo': handle_input.form(msg='Placa do veículo: '),
            'rota': handle_input.form(msg='Rota: '),
            'data': handle_input.form(msg='Data: ', regex=r'(\d{2})/(\d{2})/(\d{4})', regex_model='DD/MM/YYYY'),
            'status': True
        }

        vehicule_in_vehicules_without_driver: bool = _verify_if_vehicule_in_without_driver_(
            data=data)
        if vehicule_in_vehicules_without_driver:
            try_again = handle_input.confirm('Tentar novamente')
            if try_again:
                continue
            return

        vehicule_in_vehicules_with_driver: bool = _verify_if_vehicule_in_with_driver_(
            data=data)
        if not vehicule_in_vehicules_with_driver:
            try_again = handle_input.confirm('Tentar novamente')
            if try_again:
                continue
            return

        # Cadastrando viagem
        vehicule_avaliable: bool = viagem_model.add_travel(data=data)
        if not vehicule_avaliable:
            msg = 'Uma viagem com este veículo já foi cadastrada'
            view.warning_msg(msg=msg)
        else:
            msg = 'Nava viagem cadastrada com sucesso'
            view.sucess_msg(msg=msg)

        create_another: bool = handle_input.confirm('Criar uma nova viagem')
        if create_another:
            stop = False

        if stop:
            break


def end_travel_by_license_plate() -> None:
    """
    Finaliza uma viagem ativa

    Returns:
        None:
    """
    while True:
        stop: bool = True

        value: str = handle_input.form(msg='Placa do veículo: ')

        confirm: bool = handle_input.confirm('Deseja continuar')

        if not confirm:
            break

        vehicule = model.search_between_modules(
            search_function=veiculo_model.get_by_license_plate, param=value)

        if len(vehicule) == 0:
            view.warning_msg('Veículo não cadastrado')
            try_again = handle_input.confirm(msg='Tentar novamente')
            if try_again:
                continue
            return

        result: list[dict[str, any]] = viagem_model.get_current_travels()
        vehicules_in_travel_exist: bool = False
        for item in result:
            if item['veiculo'] == value:
                item.update({'status': False})
                viagem_model.update_travel(data=item)
                vehicules_in_travel_exist = True
                break

        if vehicules_in_travel_exist:
            view.sucess_msg(msg='Viagem finalizada com sucesso')
        else:
            view.warning_msg(msg='Veículo não está em um viagem')

        finish_another = handle_input.confirm(
            msg='Deseja finalizar outra viagem')
        if finish_another:
            stop = False

        if stop:
            break


def search_all_travels() -> None:
    """
    Exibi todas as viagens

    Returns:
        None:
    """
    result: list[dict[str, any]] = viagem_model.get_all_travels()
    view.render_search_results(search_result=result)


def current_travels() -> None:
    """
    Exibi todas as viagens ativas

    Returns:
        None:
    """
    result: list[dict[str, any]] = viagem_model.get_current_travels()
    view.render_search_results(result)


def search_all_by_period_travels() -> None:
    """
    Exibi todas as viagens por periodo

    Returns:
        None: 
    """
    from_period: str = handle_input.form(msg='Da data: ',
                                         regex=r'(\d{2})/(\d{2})/(\d{4})',
                                         regex_model='DD/MM/YYYY')

    to_period: str = handle_input.form(msg='Até a data: ',
                                       regex=r'(\d{2})/(\d{2})/(\d{4})',
                                       regex_model='DD/MM/YYYY')

    from_period_in_date: datetime = date_convert.convert_string_to_date(
        string=from_period)

    to_period_in_date: datetime = date_convert.convert_string_to_date(
        string=to_period)

    print()

    if isinstance(from_period_in_date, bool) or isinstance(to_period_in_date, bool):
        view.warning_msg('Valores de data não possuem sentido')
        return

    if to_period_in_date < from_period_in_date:
        msg = ('Primera data é maior do que a segunda, não é ' +
               'possível fazer uma consulta nesse período')
        view.warning_msg(msg=msg)
        return

    result: list[dict[str, any]] = viagem_model.get_travels_by_period(
        from_period=from_period_in_date, to_period=to_period_in_date)

    view.render_search_results(search_result=result)


def _get_veichules_in_travel_(result: list[dict[str, any]]) -> list[[dict, any]]:
    """
    Busca por veículos que estão em viagem

    Returns:
        list[[dict, any]:
    """
    all_vehicles: list[str] = []
    if len(result) > 0:
        for item in result:
            vehicule = model.search_between_modules(
                search_function=veiculo_model.get_by_license_plate, param=item['veiculo'])
            all_vehicles.append(vehicule[0])

    return all_vehicles


def vehicules_in_travel() -> None:
    """
    Exibi todos os veículos em viagem

    Returns:
        None:
    """
    result = viagem_model.get_current_travels()
    all_vehicles = _get_veichules_in_travel_(result=result)
    view.render_search_results(search_result=all_vehicles)


def vehicules_avaliables() -> None:
    """
    Exibi todos os veículos disponíveis para viagem

    Returns:
        None:
    """
    travels: list[dict[str, any]] = viagem_model.get_current_travels()

    result: list[any] = []
    vehicles_not_avaliables: list[any] = _get_veichules_in_travel_(
        result=travels)

    all_vehicles: list[dict[str, any]] = model.search_between_modules(
        search_function=veiculo_model.get_all_vehicles_with_drivers)

    for veichule in all_vehicles:
        result.append(veichule)
        if veichule in vehicles_not_avaliables:
            result.remove(veichule)

    view.render_search_results(search_result=result)


menu_opts = {
    CRIAR_VIAGEM: create_viagem,
    FINALIZAR_VIAGEM_POR_PLACA: end_travel_by_license_plate,
    VIAGENS_ATIVAS: current_travels,
    VEICULOS_EM_VIAGEM: vehicules_in_travel,
    VEICULOS_DISPONIVEIS: vehicules_avaliables,
    LISTAR_TODAS_AS_VIAGENS: search_all_travels,
    LISTAR_VIAGENS_POR_PERIODO: search_all_by_period_travels
}


def load_menu() -> None:
    """
    Exibi o menu de veiculo e pede ao usuário
    escolher uma das opções do menu

    Returns:
        None:
    """
    viagem_view.show()

    user_opt: int = handle_input.menu(menu_max_opts=MAX_OPTIONS)

    if user_opt == VOLTAR_AO_MENU_PRINCIPAL:
        view.exit_msg(msg='Voltando ao menu principal')
        menu_principal_controller.load_menu()
        return

    menu_opts[user_opt]()

    handle_input.enter_to_continue()
    load_menu()
