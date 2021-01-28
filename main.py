# PyAGC

class memory():
    RAM = [0] * 2048

class CPU(object):
    def __init__(self):
        self.A = 0x00
        self.B = 0x00
        self.LR = 0x00
        self.Q = 0x00
        self.Z = 0x00

    def processInstruction(self, instruction: str):
        splitInstruction = instruction.split()

        # AD instruction. Adds the contents of a given memory cell and writes it into the accumulator.
        if instruction.__contains__('AD'):
            self.A = self.A + int(splitInstruction[1], 0)
            # DEBUG
            print("Register A: " + str(self.A))
        # CA instruction. Copies contents of a given memory cell into the accumulator.
        if instruction.__contains__('CA'):
            self.A = memory.RAM[int(splitInstruction[1], 0)]
            # DEBUG
            print("Register A: " + str(self.A))
        # TS instruction. Sets contents of a given memory cell to the contents of the accumulator.
        if instruction.__contains__('TS'):
            memory.RAM[int(splitInstruction[1], 0)] = self.A
            # DEBUG
            print("New memory value: " + str(memory.RAM[int(splitInstruction[1], 0)]))

agcCPU = CPU()

def main():

    agcCPU.A = 0x10
    CPU.processInstruction(instruction="TS   0x200", self=agcCPU)

if __name__ == '__main__':
    main()

