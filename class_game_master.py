from bearlibterminal import terminal
import class_select_role_screen, class_set_players_roles, config

role_propeties = config.role_propeties
class GameMaster:

    def __init__(self):
        self.players = []
        self.roles = []
        self.blocked_players = None
        self.lovers = None
        self.killed_players = []
        self.murders = None
        self.end_of_game = False
        self.queue = config.default_queue

    def set_roles(self):
        role_screen = class_select_role_screen.Role_screen()
        dict_of_roles = role_screen.get_roles()
        for role in dict_of_roles.keys():
            count = dict_of_roles[role]
            for i in range(count):
                self.roles.append(role)
        print(self.roles)

    def set_players(self):
        terminal.clear()
        terminal.printf(2, 2, 'Первая ночь, ведущий знакомится с ролями игроков'.center(80))
        terminal.printf(2, 4, 'Никаких действий в эту ночь не происходит'.center(80))
        select_roles_screen = class_set_players_roles.set_players_roles(self.roles)
        self.players = select_roles_screen.get_roles()

    def print_players_poles(self):
        pass


    def refresh_queue(self):
        pass


