from bearlibterminal import terminal
import config

font_size = config.font_size
list_of_roles = config.roles_list
bgcolor_normal = config.bgcolor_normal
bgcolor_lighted = config.bgcolor_lighted

class Role_screen():

    def __init__(self):
        self.roles = list_of_roles
        self.count_of_roles = dict()
        for role in self.roles:
            self.count_of_roles[role] = 0
        self.position = 0
        self.length = len(self.roles) + 2
        self.finish = False
        self.total_players = 0

    def print(self):
        text = 'Выбор играющих ролей'.center(80)
        terminal.printf(0, 1, text)
        n = len(self.roles)
        for i in range(n):
            if i == self.position:
                terminal.bkcolor(bgcolor_lighted)
            terminal.printf(2, 4 + i, self.roles[i])
            terminal.bkcolor(bgcolor_normal)
            this_role_players = self.count_of_roles[self.roles[i]]
            text = str(this_role_players)
            if i == self.position:
                text = '<<< ' + text + ' >>>'
            text = text.center(40)
            terminal.printf(42, 4 + i, text)

        text = 'Всего игроков в игре: ' + str(self.total_players) + ' ' * 5
        terminal.printf(2, 4 + n + 2, text)
        text = 'Нажмите Enter, чтобы завершить выбор ролей'.center(80)
        terminal.printf(2, 4 + n + 4, text)
        terminal.refresh()

    def next(self):
        self.position = (self.position + 1) % (self.length - 2)
        self.print()

    def prev(self):
        self.position = (self.position - 1) % (self.length - 2)
        self.print()

    def add_player(self):
        role = self.roles[self.position]
        if self.count_of_roles[role] < config.role_propeties[role]['max count in game']:
            self.count_of_roles[role] += 1
            self.total_players += 1
            self.print()

    def del_player(self):
        role = self.roles[self.position]
        if self.count_of_roles[role] > 0:
            self.count_of_roles[role] -= 1
            self.total_players -= 1
            self.print()

    def get_roles(self):
        self.print()
        key = None
        while not self.finish:
            while (key not in [terminal.TK_DOWN, terminal.TK_UP, terminal.TK_LEFT, terminal.TK_RIGHT, terminal.TK_ENTER,
                              terminal.TK_ESCAPE]) and not self.finish:
                key = terminal.read()
            if key == terminal.TK_DOWN:
                self.next()
            elif key == terminal.TK_UP:
                self.prev()
            elif key == terminal.TK_RIGHT:
                self.add_player()
            elif key == terminal.TK_LEFT:
                self.del_player()
            elif key == terminal.TK_ENTER:
                self.finish = True
            while terminal.has_input():
                key = terminal.read()
            if not self.finish:
                key = terminal.read()
        return self.count_of_roles
