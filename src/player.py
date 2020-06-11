# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, job):
        self.name = name
        self.current_room = current_room
        self.job = job()

    def __repr__(self):
        return '{' + f'name: {self.name}, current_room: {self.current_room}, job: {self.job}' + '}'

    def __str__(self):
        return f'Player: {self.name}\nCurrently in: {self.current_room}\nJob: {str(self.job)}'