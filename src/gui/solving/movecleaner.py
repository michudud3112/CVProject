from src.gui.solving.cube import cube
from src.gui.solving.move import move


class movecleaner:
    def __init__(self, thiscube):
        self.cube = thiscube

    def clean(self):
        moves_cleaned = []
        pointer = 0
        next = 1
        while pointer + next != len(self.cube.moves):
            total = self.cube.moves[pointer].num
            while self.cube.moves[pointer].direction == self.cube.moves[pointer + next].direction:
                total += self.cube.moves[pointer + next].num
                next += 1

            moves_cleaned.append(
                move(self.cube.moves[pointer].direction, total % 4))
            pointer += next
            next = 1
        self.cube.moves = moves_cleaned
