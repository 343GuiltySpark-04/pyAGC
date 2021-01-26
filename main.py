# PyAGC
from memory import *

from Instruction import *



def main():
    cpu = CPU()
    Memory.RAM[0] = 5
    print(Memory.RAM[int("0xFFF", 0)])


if __name__ == '__main__':
    main()