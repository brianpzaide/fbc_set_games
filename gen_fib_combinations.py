import itertools
import random

elements = ['a', 'b', 'c', 'd', 'e']
blocks = {'a':1, 'b':1, 'c':2, 'd':3, 'e':5}


def display(hr, mn):
    dspl = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
    for el in hr:
        dspl[el] += 1
    for el in mn:
        dspl[el] += 2
    
    print(dspl)


def main():
    cmbs = []
    for i in range(1, len(blocks)+1):
        temp = ["".join(k) for k in itertools.combinations(elements, i)]
        cmbs.extend(temp)
    
    print(len(cmbs))
    print(cmbs)

    for i in range(10):
        hr, mn = random.choice(cmbs), random.choice(cmbs)
        display(hr, mn)
        print(f'hours: {hr}, minutes: {mn}')



if __name__ == '__main__':
    main()