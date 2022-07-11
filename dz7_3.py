class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join([' 🐽 ' * rows for _ in range(self.nums // rows)]) + '\n' + ' 🌀 ' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __sub__(self, other):
        print('Deduction of your cells: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 else "You can't deduct that..."

    def __add__(self, other):
        print('Sum of your cells: ')
        return Cell(self.nums + other.nums)

    def __floordiv__(self, other):
        print('Rounded off result of division of your cells: ')
        return Cell(self.nums // other.nums)

    def __mul__(self, other):
        print('Result of multiplication of your cells: ')
        return Cell(self.nums * other.nums)


c_1 = Cell(12)
c_2 = Cell(7)

print(c_1 - c_2)
print()
print(c_1 + c_2)
print()
print(c_1 // c_2)
print()
print(c_1 * c_2)

print()
print(c_2.make_order(3))
