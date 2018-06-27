from bearlibterminal import terminal
import config

ROLE_PROPETIES = config.ROLE_PROPETIES
BGCOLOR_NORMAL = config.BGCOLOR_NORMAL
BGCOLOR_LIGHTED = config.BGCOLOR_LIGHTED

MAFIA = config.MAFIA
BOSS = config.BOSS
HEIR = config.HEIR
KILLER = config.KILLER
DEAD = config.DEAD
WITNESS = config.WITNESS
LOVER = config.LOVER
JOURNALIST = config.JOURNALIST

count_of_spases = 1
target_zone_start_position_x = 2
target_zone_start_second_position_x = 40
target_zone_start_position_y = 6

TARGET_NAMBER_MESSAGE = 'Выбираем цель'
LEFT_QUOTES = '<<<'
RIGHT_QUOTES = '>>>'
NOT_SELECTED_TARGET_MESSAGE = '???'


class TargetZone:

    def __init__(self, current_player_role, players_list, last_acted_player_index=None):
        self.role = current_player_role
        self.players = players_list
        self.count_of_targets = 1
        if current_player_role == JOURNALIST:
            self.count_of_targets = 2
        self.suitable_targets_list = self.get_suitable_targets_list()
        self.current_targets = [-1] * self.count_of_targets
        self.current_position = 0
        self.count_of_players = len(self.players)
        self.finish = False
        self.last = last_acted_player_index

    def get_target(self):
        self.print()
        key = None
        while not self.finish:
            while (key not in [terminal.TK_DOWN, terminal.TK_UP, terminal.TK_LEFT, terminal.TK_RIGHT,
                               terminal.TK_ENTER]) and not self.finish:
                key = terminal.read()
            if key == terminal.TK_DOWN:
                self.down()
            elif key == terminal.TK_UP:
                self.up()
            elif key == terminal.TK_RIGHT:
                self.right()
            elif key == terminal.TK_LEFT:
                self.left()
            elif key == terminal.TK_ENTER:
                if -1 not in self.current_targets:
                    self.finish = True
            while terminal.has_input():
                key = terminal.read()
            if not self.finish:
                key = terminal.read()
        return self.current_targets

    def get_suitable_targets_list(self):
        targets = []
        fraction = ROLE_PROPETIES[self.role]['fraction']
        if fraction == ROLE_PROPETIES[MAFIA]['fraction']:
            bad_targets = [BOSS, HEIR, MAFIA, KILLER]
        else:
            bad_targets = [self.role]
        bad_targets.append(DEAD)
        for player in self.players:
            if player not in bad_targets:
                targets.append(player)
        return targets

    def print(self):
        for i in range(self.count_of_targets):
            self.print_position(i)

    def print_position(self, index_of_position):
        x = target_zone_start_position_x
        y = target_zone_start_position_y + index_of_position * count_of_spases
        text = TARGET_NAMBER_MESSAGE + str(index_of_position + 1)
        if index_of_position == self.current_position:
            terminal.bkcolor(BGCOLOR_LIGHTED)
        terminal.printf(x, y, text)
        terminal.bkcolor(BGCOLOR_NORMAL)
        x = target_zone_start_second_position_x
        target = self.current_targets[index_of_position]
        if target == -1:
            text = NOT_SELECTED_TARGET_MESSAGE
        else:
            text = str(target + 1)
        if index_of_position == self.current_position:
            text = LEFT_QUOTES + text + RIGHT_QUOTES
        text = text.center(20)
        terminal.printf(x, y, text)
        terminal.refresh()

    def up(self):
        self.current_position = (self.current_position - 1) % self.count_of_targets
        self.print()

    def down(self):
        self.current_position = (self.current_position + 1) % self.count_of_targets
        self.print()

    def right(self):
        current_target = self.current_targets[self.current_position]
        self.current_targets[self.current_position] = -1
        new_target_index = (current_target + 1) % self.count_of_players
        new_target_role = self.players[new_target_index]
        while self.check_role(new_target_role, new_target_index):
            new_target_index = (new_target_index + 1) % self.count_of_players
            new_target_role = self.players[new_target_index]
        self.current_targets[self.current_position] = new_target_index
        self.print()

    def left(self):
        current_target = self.current_targets[self.current_position]
        if current_target == -1:
            current_target = 0
        self.current_targets[self.current_position] = -1
        new_target_index = (current_target - 1) % self.count_of_players
        new_target_role = self.players[new_target_index]
        while self.check_role(new_target_role, new_target_index):
            new_target_index = (new_target_index - 1) % self.count_of_players
            new_target_role = self.players[new_target_index]
        self.current_targets[self.current_position] = new_target_index
        self.print()

    def check_role(self, new_target_role, new_target_index):
        wrong_targets = new_target_role not in self.suitable_targets_list
        busy_targets = new_target_index in self.current_targets
        last_target = new_target_index == self.last
        answer = wrong_targets or busy_targets or last_target
        return answer
