import numpy as np

GOOD_METH_RATIO = 5
END_CONDITION_DICTIONARY = {10: 8, 15: 11, 20:13, 25:15}
CA_GENERATION_TEST_AMOUNT = 100
NEW_CHILD_PER_GENERATION = 2
POPULATION_SIZE = 10
AMOUNT_OF_CELLS_TO_MUTATE = 3

CROSSOVER_PROBABILITY = 10  # out of 10
MUTATION_PROBABILITY = 10  # out of 10

# the board size will be 10X10, 15X15, 20X20
BOARD_SIZES = [10, 15, 20]

methuselah_array = [np.array([ [0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 1],
                               [0, 1, 1, 0, 1],
                               [1, 0, 0, 1, 0],
                               [1, 1, 0, 0, 0]])]

methuselah_array.append(np.array([ [0, 1, 0, 0, 0],
                                   [1, 1, 1, 0, 1],
                                   [1, 0, 1, 0, 1],
                                   [1, 0, 0, 0, 1],
                                   [0, 1, 1, 0, 0]]))

methuselah_array.append(np.array([ [1, 1, 0, 0, 0],
                                   [0, 0, 1, 0, 1],
                                   [0, 0, 1, 0, 1],
                                   [1, 1, 0, 1, 1],
                                   [0, 0, 1, 0, 0]]))

methuselah_array.append(np.array([ [0, 0, 0, 0, 0],
                                   [1, 1, 1, 0, 1],
                                   [0, 1, 0, 1, 0],
                                   [0, 0, 0, 1, 1],
                                   [0, 0, 0, 0, 1]]))

methuselah_array.append(np.array([ [0, 0, 0, 0, 1],
                                   [0, 0, 0, 1, 1],
                                   [0, 0, 1, 1, 0],
                                   [1, 1, 1, 0, 0],
                                   [1, 0, 0, 0, 0]]))

methuselah_array.append(np.array([ [0, 0, 0, 1, 1],
                                   [0, 1, 1, 0, 1],
                                   [0, 1, 1, 0, 1],
                                   [0, 1, 0, 0, 1],
                                   [0, 1, 0, 0, 0]]))

methuselah_array.append(np.array([ [0, 0, 1, 1, 1],
                                   [0, 0, 0, 0, 1],
                                   [0, 0, 1, 1, 0],
                                   [0, 0, 0, 1, 1],
                                   [0, 0, 0, 1, 0]]))

methuselah_array.append(np.array([ [0, 0, 0, 0, 1],
                                   [1, 1, 1, 0, 1],
                                   [0, 0, 1, 0, 1],
                                   [0, 0, 1, 1, 0],
                                   [0, 0, 0, 1, 1]]))

methuselah_array.append(np.array([ [0, 0, 1, 1, 1],
                                   [0, 0, 0, 0, 1],
                                   [0, 0, 1, 1, 1],
                                   [0, 0, 1, 0, 1],
                                   [0, 0, 1, 1, 1]]))

methuselah_array.append(np.array([ [1, 1, 1, 1, 1],
                                   [1, 0, 1, 0, 1],
                                   [1, 0, 1, 0, 1],
                                   [1, 1, 0, 0, 0],
                                   [0, 1, 0, 0, 0]]))
