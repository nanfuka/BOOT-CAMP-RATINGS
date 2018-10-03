class Bootcamper:
    def __init__(self, username):
        self.username = username
        self.scores = []

    def view_scores(self):
        score = print('Hello {}, these are your scores as of today: {}')
        return score.format(self.username, self.scores)


        