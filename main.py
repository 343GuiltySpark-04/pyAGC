# PyAGC
# Victor Mout

# Define RAM and ROM
class memory:
    bank1 = [0] * 400
    bank2 = [0] * 400
    bank3 = [0] * 400
    activeBank = bank1
    RAM = [0] * 2048 + activeBank

# CPU object
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
        if instruction.__contains__('AD') and not instruction.__contains__('ADS'):
            self.A = self.A + int(splitInstruction[1], 0)
            # DEBUG
            print("(AD) Register A: " + str(self.A))
        # ADS instruction. Adds the contents of a given memory cell and writes it into the accumulator.
        if instruction.__contains__('ADS'):
            memory.RAM[int(splitInstruction[1], 0)] = memory.RAM[int(splitInstruction[1], 0)] + self.A
            # DEBUG
            print("(ADS) Memory Address: " + str(memory.RAM[int(splitInstruction[1], 0)]))
        # CA instruction. Copies contents of a given memory cell into the accumulator.
        if instruction.__contains__('CA'):
            self.A = memory.RAM[int(splitInstruction[1], 0)]
            # DEBUG
            print("(CA) Register A: " + str(self.A))
        # TS instruction. Sets contents of a given memory cell to the contents of the accumulator.
        if instruction.__contains__('TS'):
            memory.RAM[int(splitInstruction[1], 0)] = self.A
            # DEBUG
            print("(TS) New memory value: " + str(memory.RAM[int(splitInstruction[1], 0)]))
        # XCH instruction. Swaps contents of the accumulator with given memory address.
        if instruction.__contains__('XCH'):
            self.Q = self.A
            self.A = memory.RAM[int(splitInstruction[1], 0)]
            memory.RAM[int(splitInstruction[1], 0)] = self.Q
            # DEBUG
            print("(XCH) Accumulator: ", str(self.A))
            print("(XCH) Memory address: ", memory.RAM[int(splitInstruction[1], 0)])


# Main instruction
def main():

    CPU.A = 0x10
    memory.RAM[0x200] = 0x20
    CPU.processInstruction(instruction="", self=CPU)


# name/main run check
if __name__ == '__main__':
    main()
