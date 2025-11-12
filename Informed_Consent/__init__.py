from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Informed_Consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_TASKS = 10


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

class Informed_Consent(Page):
    pass


page_sequence = [Informed_Consent]