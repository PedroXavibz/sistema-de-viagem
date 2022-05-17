"""
Modulo principal de excução
"""

from src.controllers import menu_principal_controller


def main():
    """
    Função principal que irá ser ponto de partida de
    execução de outras funções
    """
    menu_principal_controller.load_menu()


if __name__ == '__main__':
    main()
