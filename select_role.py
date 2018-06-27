from bearlibterminal import terminal
import config

FONT_SIZE = config.FONT_SIZE
ROLES_LIST = config.ROLES_LIST
BGCOLOR_NORMAL = config.BGCOLOR_NORMAL
BGCOLOR_LIGHTED = config.BGCOLOR_LIGHTED
SCREEN_WIDTH = config.SCREEN_WIDTH

SCREEN_CAPTION = 'Выбор играющих ролей'
LEFT_QUOTES = '<<<'
RIGHT_QUOTES = '>>>'

class RoleScreen():

    def __init__(self):
        self.roles = ROLES_LIST
        self.count_of_roles = dict()
        for role in self.roles:
            self.count_of_roles[role] = 0
        self.position = 0
        self.length = len(self.roles) + 2
        self.finish = False
        self.total_players = 0

    def print(self):
        text = SCREEN_CAPTION.center(SCREEN_WIDTH)
        terminal.printf(0, 1, text)
        n = len(self.roles)
        for i in range(n):
            if i == self.position:
                terminal.bkcolor(BGCOLOR_LIGHTED)
            terminal.printf(2, 4 + i, self.roles[i])
            terminal.bkcolor(BGCOLOR_NORMAL)
            this_role_players = self.count_of_roles[self.roles[i]]
            text = str(this_role_players)
            if i == self.position:
                text = LEFT_QUOTES + text + RIGHT_QUOTES
            text = text.center(SCREEN_WIDTH // 2)
            terminal.printf(42, 4 + i, text)
        terminal.refresh()

    def next(self):
        self.position = (self.position + 1) % (self.length - 2)
        self.print()

    def prev(self):
        self.position = (self.position - 1) % (self.length - 2)
        self.print()

    def add_player(self):
        role = self.roles[self.position]
        if self.count_of_roles[role] < config.ROLE_PROPETIES[role]['max count in game']:
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
            while (key not in [terminal.TK_DOWN, terminal.TK_UP, terminal.TK_LEFT, terminal.TK_RIGHT,
                               terminal.TK_ENTER]) and not self.finish:
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