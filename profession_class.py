class Profession:

    def __init__(self, name, hours, score=0):
        self.name = name
        self.hours = hours
        self.score = score
        # self.project = 0
    def switch_score(self, score):  # נתינת או שינוי ציון
        self.score = score