#!/usr/bin/env python
__author__ = "Prashant Shivarm Bhat"
__email__ = "PrashantShivaram@outlook.com"

import numpy as np
from transformer import ScaledArray, SelectedArray, ExtractedArray


# Future Work : Write decorator for checking whether generated individual is valid
# Future Work: Reinforcement learning
def grow_individual(pset, min_=3, max_=8):
    height = np.random.randint(low=min_, high=max_)
    individual = []
    idx = 1
    # Add unary operators if height is greater than 3
    if height > 3:
        # first 'unary' with input_matrix
        transformer = np.random.choice(pset.primitives[np.ndarray])
        individual.append(transformer)
        for arg_type in transformer.args[0:]:
            terminal = np.random.choice(pset.terminals[arg_type])
            individual.append(terminal)
        height -= 1

        # subsequent unary operators without input_matrix
        while height > 3:
            prim = []
            transformer = np.random.choice(pset.primitives[np.ndarray])
            individual = [transformer] + individual
            # input_matrix is skipped since it was included before
            for arg_type in transformer.args[1:]:
                terminal = np.random.choice(pset.terminals[arg_type])
                prim.append(terminal)
            # append to the primitive list
            individual = individual + prim
            height -= 1

    elif height <= 3:
        # np.ndarray is included only if it was not included before
        idx = 0
    # one scaler, one selector and one extractor is added to the tree
    scaler = np.random.choice(pset.primitives[ScaledArray])
    individual = [scaler] + individual
    for arg_type in scaler.args[idx:]:
        terminal = np.random.choice(pset.terminals[arg_type])
        individual.append(terminal)

    selector = np.random.choice(pset.primitives[SelectedArray])
    individual = [selector] + individual
    # np.ndarray is included only if it was not included before
    for arg_type in selector.args[1:]:
        terminal = np.random.choice(pset.terminals[arg_type])
        individual.append(terminal)

    extractor = np.random.choice(pset.primitives[ExtractedArray])
    individual = [extractor] + individual
    # np.ndarray is included only if it was not included before
    for arg_type in extractor.args[1:]:
        terminal = np.random.choice(pset.terminals[arg_type])
        individual.append(terminal)

    # individual as a list (iterable)
    return individual


def mate(ind_1, ind_2):
    return ind_1, ind_2

def mutate(ind):
    return ind,






























