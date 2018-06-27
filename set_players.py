from bearlibterminal import terminal

import config

bgcolor_normal = config.BGCOLOR_NORMAL
bgcolor_lighted = config.BGCOLOR_LIGHTED
PEACEFUL = config.PEACEFUL

LEFT_QUOTES = '<<< '
RIGHT_QUOTES = ' >>>'
NOT_SELECTED = '0'
NOT_SELECTED_MESSAGE = '???'


class SetPlayers:

    def __init__(self, roles):
        self.count_of_players = len(roles)
        self.roles = self.set_roles(roles)
        self.count_of_roles = len(self.roles)
        self.position = 0
        self.indexes_of_roles = [-1] * self.count_of_players
        self.busy_indexes = []
        self.finish = False

    def set_roles(self, roles):
        count_of_piesfull = roles.count(PEACEFUL)
        for i in range(count_of_piesfull):
            roles.remove(PEACEFUL)
        return roles

    def print(self):
        for i in range(self.count_of_roles):
            text = self.roles[i]
            if i == self.position:
                terminal.bkcolor(bgcolor_lighted)
            terminal.printf(2, 6 + i, text)
            terminal.bkcolor(bgcolor_normal)
            text = str(self.indexes_of_roles[i] + 1)
            if text == NOT_SELECTED:
                text = NOT_SELECTED_MESSAGE
            if i == self.position:
                text = LEFT_QUOTES + text + RIGHT_QUOTES
            text = text.center(20)
            terminal.printf(22, 6 + i, text)
        terminal.refresh()

    def up(self):
        self.position = (self.position - 1) % self.count_of_roles
        self.print()

    def down(self):
        self.position = (self.position + 1) % self.count_of_roles
        self.print()

    def next(self):
        current_index = self.indexes_of_roles[self.position]
        new_index = (current_index + 1) % self.count_of_players
        if current_index != -1:
            self.busy_indexes.remove(current_index)
        while new_index in self.busy_indexes:
            new_index = (new_index + 1) % self.count_of_players
        self.indexes_of_roles[self.position] = new_index
        self.busy_indexes.append(new_index)
        self.print()

    def prev(self):
        current_index = self.indexes_of_roles[self.position]
        if current_index == -1:
            new_index = self.count_of_players - 1
        else:
            new_index = (current_index - 1) % self.count_of_players
        if current_index != -1:
            self.busy_indexes.remove(current_index)
        while new_index in self.busy_indexes:
            new_index = (new_index - 1) % self.count_of_players
        self.indexes_of_roles[self.position] = new_index
        self.busy_indexes.append(new_index)
        self.print()

    def get_roles_indexes(self):
        self.print()
        key = None
        while not self.finish:
            while (key not in [terminal.TK_DOWN, terminal.TK_UP, terminal.TK_LEFT, terminal.TK_RIGHT, terminal.TK_ENTER,
                               terminal.TK_ESCAPE]) and not self.finish:
                key = terminal.read()
            if key == terminal.TK_DOWN:
                self.down()
            elif key == terminal.TK_UP:
                self.up()
            elif key == terminal.TK_RIGHT:
                self.next()
            elif key == terminal.TK_LEFT:
                self.prev()
            elif key == terminal.TK_ENTER:
                if self.indexes_of_roles.count(-1) == self.count_of_players - self.count_of_roles:
                    self.finish = True
            while terminal.has_input():
                key = terminal.read()
            if not self.finish:
                key = terminal.read()

    def get_roles(self):
        self.get_roles_indexes()
        players_list = [0] * self.count_of_players
        for i in range(self.count_of_roles):
            index = self.indexes_of_roles[i]
            role = self.roles[i]
            players_list[index] = role
        for i in range(self.count_of_players):
            if players_list[i] == 0:
                players_list[i] = PEACEFUL
        return players_list
