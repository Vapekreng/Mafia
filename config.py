FONT_SIZE = 24
BGCOLOR_NORMAL = 'black'
BGCOLOR_LIGHTED = 'dark grey'
SCREEN_WIDTH = 80
X_START_POSITION = 0
MAX_ROLE_NAME_LENGTH = 15

# Названия ролей игроков

ROGUE = 'Жулик'
LOVER = 'Любовница'
BOSS = 'Босс мафии'
HEIR = 'Наследник'
MAFIA = 'Мафия'
KILLER = 'Киллер'
MANIAC = 'Маньяк'
FROSTBITE = 'Отморозок'
DOCTOR = 'Доктор'
COP = 'Комиссар'
JOURNALIST = 'Журналист'
PRIEST = 'Священник'
WITNESS = 'Свидетель'
PEACEFUL = 'Мирный житель'
JUDGE = 'Судья'
IMMORTAL = 'Бессмертный'
LAWYER = 'Адвокат'
WEREWOLF = 'Оборотень'
VOTING = 'Голосование'
DEAD = 'Мертв'

MAFIA_FRACTION = 'mafia'

# Список всех ролей
ROLES_LIST = [ROGUE, LOVER, BOSS, HEIR, MAFIA, KILLER, MANIAC, FROSTBITE, DOCTOR,
              COP, JOURNALIST, PRIEST, WITNESS, PEACEFUL, JUDGE, IMMORTAL, LAWYER,
              WEREWOLF]

# Активные роли расставлены в том порядке, в каком они просыпаются ночью
QUEUE = [ROGUE, LOVER, BOSS, MAFIA, KILLER, MANIAC, FROSTBITE, DOCTOR, COP,
         JOURNALIST, PRIEST, WITNESS]

ROLE_PROPETIES = dict()
# [Отображаемое имя, максимальное количество игроков данной роли, фракция, просыпается ночью или нет]
ROLE_PROPETIES[LOVER] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[ROGUE] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[BOSS] = {'max count in game': 1, 'fraction': 'mafia', 'is active': True}
ROLE_PROPETIES[HEIR] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[MAFIA] = {'max count in game': 100, 'fraction': 'mafia', 'is active': True}
ROLE_PROPETIES[KILLER] = {'max count in game': 1, 'fraction': 'mafia', 'is active': True}
ROLE_PROPETIES[MANIAC] = {'max count in game': 1, 'fraction': 'maniac', 'is active': True}
ROLE_PROPETIES[FROSTBITE] = {'max count in game': 1, 'fraction': 'frostbite', 'is active': True}
ROLE_PROPETIES[DOCTOR] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[COP] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[JOURNALIST] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[PRIEST] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[WITNESS] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': True}
ROLE_PROPETIES[PEACEFUL] = {'max count in game': 100, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[JUDGE] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[IMMORTAL] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[LAWYER] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[WEREWOLF] = {'max count in game': 1, 'fraction': 'peacefull', 'is active': False}
ROLE_PROPETIES[VOTING] = {'max count in game': 0, 'fraction': None, 'is active': False}


ACTION_MESSAGES = {}

ACTION_MESSAGES[LOVER] = ['Просыпается любовница', 'Блокирует способность цели на эту ночь']
ACTION_MESSAGES[ROGUE] = ['Просыпается жулик', 'На эту ночь становится копией выбранного игрока']
ACTION_MESSAGES[BOSS] = ['Просыпается мафия', 'Ищет копа']
ACTION_MESSAGES[MAFIA] = ['Просыпается мафия', 'Совершает убийство']
ACTION_MESSAGES[KILLER] = ['Просыпается мафия', 'Совершает убийство']
ACTION_MESSAGES[MANIAC] = ['Просыпается маньяк', 'Совершает убийство']
ACTION_MESSAGES[FROSTBITE] = ['Просыпается отморозок','Убивает любого игрока с активной ролью']
ACTION_MESSAGES[DOCTOR] = ['Просыпается доктор', 'Лечит любого игрока']
ACTION_MESSAGES[COP] = ['Просыпается комиссар', 'Проверяет любого игрока - мафия он или нет']
ACTION_MESSAGES[JOURNALIST] = ['Просыпается журналист', 'Проверяет приннадлежат ли два игрока одной и той же фракции']
ACTION_MESSAGES[PRIEST] = ['Просыпается священник', 'Знакомится с любым игроком']
ACTION_MESSAGES[WITNESS] = ['Просыпается свидетель',
                            'Выбирает игрока. Если этого игрока убили этой ночью - узнает убийцу']
ACTION_MESSAGES[JUDGE] = ['Просыпается судья','Выносит приговор осужденному']
ACTION_MESSAGES[VOTING] = ['Начинается голосование','Выбирается игрок, которого отправят в тюрьму']

JUDGE_RESOLUTION = ['Казнить', 'Помиловать']
JUDGEMENT_RESULT = ['Игрок казнен!', 'Игрок помилован!']
LOVER_HAS_NO_TARGET = 'В эту ночь любовница не может никого заблокировать'
PLAYER_IS_BLOCKED_OR_KILLED = 'Действие отменено - игрок заблокирован или убит!'
IT_IS_NOT_COP = 'Это не коп...'
IT_IS_COP = 'Это коп!'
WEREWOLF_BECOMES_MAFIA = 'Мафия вне игры - оборотень становится мафией'
GOOD_NIGHT = 'Город засыпает'
GOOD_MORNING = 'Город просыпается'
GAME_OVER = 'Игра окончена'
KILLED_LIST = 'Список убитых ночью игроков:'
NO_KILLS_TONIGHT = 'Этой ночью никого не убили'
KILLED_INDEX = 'Убит ирок №'
SURVIVORS = 'Выжившие на данный момент:'
HEIR_BECOMES_BOSS = 'Босс мафии вне игры - наследник становится боссом!'
IT_IS_MAFIA = 'Это мафия!'
IT_IS_NOT_MAFIA = 'Это не мафия'
SIMILAR_FRACTIONS = 'Игроки из одной фракции'
DIFFERENT_FRACTIONS = 'Игроки из разных фракций'
PLAYER_IS_ALIVE = 'Игрок жив'
PLAYER_IS_DEAD = 'Игрок убит.'
KILLER_IS = 'Его убийца - игрок номер '
ROLE_IS_STOLED = 'Украдена роль, до конца ночи жулик это '
NOT_ACTIVE_ROLE = 'Роль не активна'

WINNERS_MESSAGE = {}

WINNERS_MESSAGE[ROLE_PROPETIES[PEACEFUL]['fraction']] = 'Победили мирные жители!'.center(SCREEN_WIDTH)
WINNERS_MESSAGE[ROLE_PROPETIES[MAFIA]['fraction']] = 'Победила мафия!'.center(SCREEN_WIDTH)
WINNERS_MESSAGE[ROLE_PROPETIES[MANIAC]['fraction']] = 'Победил маньяк!'.center(SCREEN_WIDTH)
WINNERS_MESSAGE[ROLE_PROPETIES[FROSTBITE]['fraction']] = 'Победил отморозок!'.center(SCREEN_WIDTH)

FIRST_NIGHT_MESSAGE = ['Первая ночь, ведущий знакомится с ролями игроков'.center(SCREEN_WIDTH),
                       'Никаких действий в эту ночь не происходит'.center(SCREEN_WIDTH)]