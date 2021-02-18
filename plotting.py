import matplotlib.pyplot as plt
from matplotlib import colors
from board_functions import *
from methuselah_lists import *


def present_statistics(grades_matrix: list):
    """plots a scatter of the average fitness of the population through the generations"""
    for x in range(len(grades_matrix)):
        avg_grade = sum(grades_matrix[x]) / len(grades_matrix[0])
        min_grade = min(grades_matrix[x])
        plt.scatter(x, avg_grade, color='blue')
        plt.scatter(x, min_grade, color='orange')

    if MUTATION_PROBABILITY >= 7:
        mutation_level = "very high"
    elif MUTATION_PROBABILITY >= 4:
        mutation_level = "medium"
    else:
        mutation_level = "low"

    plt.title(f"fitness through generations {mutation_level} mutation")
    plt.xlabel("Generation")
    plt.ylabel("Population's fitness")
    plt.show()


def present_methuselah(methuselah: np.ndarray, title: str):
    """plots the matrix of the methuselah"""
    cmap = colors.ListedColormap(['White','Black'])
    plt.figure(figsize=(4,4))
    plt.pcolor(methuselah[::-1],cmap=cmap,edgecolors='k', linewidths=3)
    plt.title(title)
    plt.show()


def test_specific_meth(size, methuselah: np.ndarray):
    """plots the the methuselah in different stages of his life"""
    board1 = Board.create_board_from_methuselah(size, methuselah)
    present_methuselah(board1.grid, 'the methuselah at generation 0')

    board1.next_amount_of_generations(100)
    grade = grade_methuselah(board1)
    present_methuselah(board1.most_lived_grid, "the methuselah at it's peak")
    present_methuselah(board1.grid, "the methuselah after 100 generations")

    print(f'its grade is: {grade}')
    print(f"it's most lived age is: {board1.most_lived_age}")
    print(f"it's most lives were: {board1.most_lives_so_far}")
    return board1


def calc_meth_grade(size, methuselah):
    """check whether a configuration is a valid methuselah and calculates it's fitness/grade"""
    if methuselah is None:
        return None
    board1 = Board.create_board_from_methuselah(size, methuselah)
    is_valid_meth = board1.is_valid_meth_board()
    if is_valid_meth:
        grade = grade_methuselah(board1)
    else:
        grade = 0
    return [methuselah, grade]


def test_size_correlation():
    grades_per_size_matrix = []
    for size in range(10, 26):
        print(f'current size is: {size}')

        population_array = []
        for meth in methuselah_array:
            population_array.append(calc_meth_grade(size, meth))

        current_grades = [item[1] for item in population_array]
        grades_per_size_matrix.append(current_grades)
    plot_size_correlation(grades_per_size_matrix)


def plot_size_correlation(grades_per_size_matrix: list):
    """plots a scatter of the average fitness of the population through the generations"""
    for x in range(len(grades_per_size_matrix)):
        avg_grade = sum(grades_per_size_matrix[x]) / len(grades_per_size_matrix[0])
        plt.scatter(x + 10, avg_grade, color='green')

    plt.title(f"Methuselah Fitness vs World Size")
    plt.xlabel("World Size")
    plt.ylabel("Average methuselah fitness")
    plt.show()


def main():
    meth = np.array([[1., 1., 0., 0., 0.],
       [0., 0., 1., 0., 1.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 1.]])

    test_specific_meth(15, meth)


if __name__ == '__main__':
    main()
