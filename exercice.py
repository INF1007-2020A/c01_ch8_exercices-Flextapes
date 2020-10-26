#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import math

# TODO: Définissez vos fonction ici
def comparateur(name_file_1: str, name_file_2: str):
    with open(name_file_1, "r") as f1, open(name_file_2, "r") as f2:
        same = True

        while same:
            a = f1.read()
            b = f2.read()

            same = a == b
    return same

def triple_space(name_of_the_file: str):
    with open(name_of_the_file, "r") as f3:
        data = f3.read()
        triple = data.replace(' ', '   ')
        #et je sais plus comment on remplace :(
                    


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(comparateur(fichier1, fichier2))
    pass
