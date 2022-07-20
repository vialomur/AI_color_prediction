from Node import Node_t
import random

EXP_OUTPUT = 0.8
Inp = 0.5
LEARN_RATE = 0.4

rand_weights = [random.uniform(-0.1,0.1)  for i in range(3)]
node = Node_t(rand_weights,0)

with open("test.txt", "r") as fp:
    lines = fp.readlines()
    eof = fp.tell()
    fp.seek(0)

    poprawnych_wynikow = 0
    ile = 0
    jaki = 0
    while eof != fp.tell():
        # print(fp.readline(),end='')
        lst_inputs = fp.readline()
        lst_inputs_float = [float(x) for x in lst_inputs.split()]

        print(
            f"inputs:{lst_inputs_float[0]},{lst_inputs_float[1]},{lst_inputs_float[2]} exp_out:{lst_inputs_float[3]}")

        wynik = node.learn_node(lst_inputs_float, LEARN_RATE)

        if abs(lst_inputs_float[3] - wynik) < 0.5:
            poprawnych_wynikow += 1

        ile += 1
        node.display()

print(f"poprawnych:{poprawnych_wynikow} ile:{ile}")
