class Matr:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("\t".join([f'{a:3}' for a in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            z = [[int(self.matrix[line][a]) + int(other.matrix[line][a]) for a in range(len(self.matrix[line]))] for line in range(len(self.matrix))]
            return Matr(z)
        except IndexError:
            return 'Матрицы для сложения должны быть c одинаковым количеством компонентов!'


matr_1 = Matr([[10, 8], [12, -6], [14, 4]])
matr_2 = Matr([[1, 11], [-2, 13], [3, 15]])

print(matr_1 + matr_2)
