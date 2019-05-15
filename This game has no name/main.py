class Player:
    def ready(self, new_start, new_ready):
        if self.first is False:
            old_ = getattr(self, self.old)
            setattr(self, new_ready, old_)
            delattr(self, self.old)
        if self.first is True:
            self.first = False
            setattr(self, new_ready, self.ready)
            delattr(Player, 'ready')
        self.old = new_ready
        self.game.name_start = new_start


def play(obj_game):
    player = Player()
    player.old = 'ready'
    player.game = obj_game
    player.game.name_start = 'start'
    player.first = True
    while True:
        getattr(obj_game, player.game.name_start)(player)
