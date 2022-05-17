"""
O objetivo deste modulo é auxiliar na leitura de código, ao selecionarmos opções de menu.
"""

main_menu_opts: dict[str, int] = {
    'MAX_OPTIONS': 4,
    'MOTORISTA': 1,
    'VEICULO': 2,
    'VIAGEM': 3,
    'SAIR': 4
}


menu_motorista_opts: dict[str, int] = {
    'MAX_OPTIONS': 5,
    'CADASTRAR_MOTORISTA': 1,
    'BUSCAR_MOTORISTA_POR_CPF': 2,
    'LISTAR_POR_CARTEIRA': 3,
    'LISTAR_TODOS': 4,
    'SAIR': 5
}


menu_veiculo_opts: dict[str, int] = {
    'MAX_OPTIONS': 5,
    'CADASTRAR_VEICULO': 1,
    'BUSCAR_PLACA': 2,
    'LISTAR_VEICULOS_COM_MOTORISTAS': 3,
    'LISTAR_VEICULOS_SEM_MOTORISTAS': 4,
    'SAIR': 5
}


menu_viagem_opts: dict[str, int] = {
    'MAX_OPTIONS': 8,
    'CRIAR_VIAGEM': 1,
    'FINALIZAR_VIAGEM_POR_PLACA': 2,
    'VIAGENS_ATIVAS': 3,
    'VEICULOS_EM_VIAGEM': 4,
    'VEICULOS_DISPONIVEIS': 5,
    'LISTAR_TODAS_AS_VIAGENS': 6,
    'LISTAR_VIAGENS_POR_PERIODO': 7,
    'SAIR': 8
}
