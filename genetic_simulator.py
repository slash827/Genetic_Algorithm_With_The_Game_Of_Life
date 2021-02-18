from plotting import *
import time, random


def crossover_boards(methuselah1: np.ndarray, methuselah2: np.ndarray):
    """takes two boards and create the crossover board of them"""
    probability = random.randint(1, 10)
    if probability <= CROSSOVER_PROBABILITY:
        length = 5
        new_meth = np.add(np.zeros(shape=(5, 5)), methuselah1)
        for i in range(length-1):
            new_meth[i][:length-1-i] = methuselah2[i][:length-1-i]
        return new_meth


def mutate_board(methuselah: np.ndarray):
    """takes one board and create a mutation if occurs"""
    probability = random.randint(1, 10)
    # the mutation happens only with a probability
    if probability <= MUTATION_PROBABILITY:
        # change the state of a single, random cell in the configuration
        for i in range(AMOUNT_OF_CELLS_TO_MUTATE):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            methuselah[x][y] = 1 - methuselah[x][y]


def select_and_crossover(weights, population_array):
    """select 2 different parents to reproduce using roulette selection"""
    indexes = list(range(len(population_array)))
    first, second = random.choices(indexes, weights=weights, k=2)
    while first == second:
        first, second = random.choices(indexes, weights=weights, k=2)

    parents_tuples = [population_array[first], population_array[second]]
    return crossover_boards(parents_tuples[0][0], parents_tuples[1][0])


def remove_least_fit(required_length: int, population_array: list):
    """gets a larger population and removes the least fits from it"""
    while required_length < len(population_array):
        grades = [item[1] for item in population_array]
        minimal = min(grades)
        for i in range(len(population_array)):
            if population_array[i][1] == minimal:
                del population_array[i]
                break


def genetic_end_condition(size, population_array: list):
    """returns true if found a grade of at least the grade we expected to get"""
    grades = [item[1] for item in population_array]
    great_grades = [grade for grade in grades if grade >= END_CONDITION_DICTIONARY[size]]
    if great_grades:
        return True
    return False


def check_if_population_similar(grades: list):
    """checking whether the whole population converged to a similar methuselah"""
    average_grade = sum(grades) / len(grades)
    reduced_grades = [abs(grade - average_grade) for grade in grades]
    reduced_grades = [item for item in reduced_grades if item > 0.1]
    if len(reduced_grades) < 2:
        print(f'reduced grades are: {reduced_grades}')
        return True

    return False


def run_one_genetic_generation(size, population_array: list):
    required_length = POPULATION_SIZE
    # we make the first and second crossovers

    weights = [item[1] for item in population_array]
    new_boards = []
    for i in range(NEW_CHILD_PER_GENERATION):
        new_board = select_and_crossover(weights, population_array)
        if new_board is None:
            continue  # in case no crossover occurred

        # we will insert the new board only if he is a valid methuselah
        new_board = calc_meth_grade(size, new_board)
        grade = new_board[1]
        if grade is not None and grade > 0:
            new_boards.append(new_board)

    # here we apply mutation with a certain probability
    for new_board in new_boards:
        mutate_board(new_board[0])

    # if a crossover succeeded we insert it to the population
    for new_board in new_boards:
        if new_board is not None and new_board[0] is not None:
            population_array.append(new_board)

    remove_least_fit(required_length, population_array)


def genetic_algorithm(size, population_array: list):
    amount_of_generations = 0
    grades = [item[1] for item in population_array]
    grades_matrix = [grades]
    while amount_of_generations < CA_GENERATION_TEST_AMOUNT and not check_if_population_similar(grades)\
            and not genetic_end_condition(size, population_array):

        run_one_genetic_generation(size, population_array)

        amount_of_generations += 1
        print(f'generation now is: {amount_of_generations}')
        grades = [item[1] for item in population_array]
        grades_matrix.append(grades)
        print(f'grades currently are: {grades}')

    print(population_array)
    return grades_matrix


def main(size):
    """here we create the initial population then activates the genetic algorithm on them"""
    population_array = []
    for meth in methuselah_array:
        population_array.append(calc_meth_grade(size, meth))

    print(f'the initial methuselahs grades are: {[item[1] for item in population_array]}')
    grades_matrix = genetic_algorithm(size, population_array)
    present_statistics(grades_matrix)



if __name__ == '__main__':
    start = time.time()
    main(10)
    end = time.time()
    print(f'\ntime passes is: {end - start}')
