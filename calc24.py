from __future__ import division
import os
import itertools
import pickle
from fractions import Fraction


def find_all_combinations():
    four_ops = ['+', '-', '*', '/']
    four_nums = ['a', 'b', 'c', 'd']
    all_comb = []
    for x in itertools.permutations(four_nums):
        for op1 in four_ops:
            three_nums = ("({}{}{})".format(x[0], op1, x[1]), x[2], x[3])
            for y in itertools.permutations(three_nums):
                for op2 in four_ops:
                    two_nums = ("({}{}{})".format(y[0], op2, y[1]), y[2])
                    for z in itertools.permutations(two_nums):
                        for op3 in four_ops:
                            all_comb.append(("{}{}{}".format(z[0], op3, z[1])))
    print("{} possible combinations found".format(len(all_comb)))
    return all_comb


def comb_compressed(all_comb, four_nums=[3359, 3607, 4451, 4561]):
    results_cached = set()
    comb_left = []
    a, b, c, d = map(Fraction, four_nums)
    for comb in all_comb:
        eval_exp = eval(comb)
        if eval_exp in results_cached:
            continue
        else:
            comb_left.append(comb)
            results_cached.add(eval_exp)
    print("{} combinations after duplications removed".format(len(comb_left)))
    return set(comb_left)


try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache


@lru_cache(maxsize=None)
def all_combs():
    # if combs are saved in db before, load them into memory
    # if not, re-generate all possible combinations
    fn_db = "combs.db"
    if os.path.isfile(fn_db):
        with open(fn_db, "rb") as db:
            combs = pickle.load(db)
        print("{} combinations loaded from {}".format(len(combs), fn_db))
    else:
        combs = find_all_combinations()
        combs = comb_compressed(combs)
        with open(fn_db, "wb") as db:
            pickle.dump(combs, db)
    return combs


def all_solutions(four_nums):
    a, b, c, d = map(Fraction, four_nums)
    solutions = []
    for comb in all_combs():
        try:
            if eval(comb) == 24:
                solutions.append(comb.replace('a', str(a))
                                    .replace('b', str(b))
                                    .replace('c', str(c))
                                    .replace('d', str(d)))
        except ZeroDivisionError:
            continue
    return solutions


if __name__ == "__main__":
    while(1):
        four_nums_input = input("please enter 4 numbers(q to exit): ")
        if four_nums_input.strip() == "q":
            break
        four_nums = [int(n) for n in four_nums_input.split()]
        solutions = all_solutions(four_nums)
        if len(solutions) == 0:
            print("no solution found")
        for sol in set(solutions):
            print("{} = 24".format(sol))
