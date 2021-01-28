# PyAGC
# Victor Mout, 2021
# GNU License
#
# C U R R E N T  I N S T R U C T I O N S #
# AD
# ADS
# CA
# TS
# XCH
# AUG

# TODO: Add line by line file reader
# TODO: Finish all instructions
# TODO: Add function logic
# TODO: Add I/O logic
# TODO: Add DSKY output
# TODO: Finish registers
# TODO: Add nessecary ROM data


# Define Memory and ROM
class Memory:
    UNSWITCHED_WRITABLE_Memory = [0] * 767
    SWITCHED_WRITABLE_BANK_Memory1 = [0] * 255
    SWITCHED_UNWRITABLE_BANK_Memory1 = [0] * 1024
    UNSWITCHED_UNWRITABLE_Memory = [0] * 2048
    ACTIVE_UNWRITABLE_BANK = SWITCHED_UNWRITABLE_BANK_Memory1
    ACTIVEBANK = SWITCHED_WRITABLE_BANK_Memory1
    Memory = UNSWITCHED_WRITABLE_Memory + ACTIVEBANK + ACTIVE_UNWRITABLE_BANK + UNSWITCHED_UNWRITABLE_Memory
    IO_SPACE = [0] * 511


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
        arg = Memory.Memory[int(splitInstruction[1], 0)]

        # AD instruction. Adds the contents of a given Memory cell and writes it into the accumulator.
        if instruction.__contains__('AD') and not instruction.__contains__('ADS'):
            self.A = self.A + Memory.Memory[int(splitInstruction[1], 0)]
            # DEBUG
            print("(AD) Register A: " + str(self.A))

        # ADS instruction. Adds the contents of a given Memory cell and writes it into the accumulator.
        if instruction.__contains__('ADS'):
            arg = arg + self.A
            # DEBUG
            print("(ADS) Memory Address: " + str(arg))

        # CA instruction. Copies contents of a given Memory cell into the accumulator.
        if instruction.__contains__('CA'):
            self.A = arg
            # DEBUG
            print("(CA) Register A: " + str(self.A))

        # TS instruction. Sets contents of a given Memory cell to the contents of the accumulator.
        if instruction.__contains__('TS'):
            Memory.Memory[int(splitInstruction[1], 0)] = self.A
            # DEBUG
            print("(TS) New Memory value: " + str(Memory.Memory[int(splitInstruction[1], 0)]))

        # XCH instruction. Swaps contents of the accumulator with given Memory address.
        if instruction.__contains__('XCH'):
            self.Q = self.A
            self.A = arg
            arg = self.Q
            # DEBUG
            print("(XCH) Accumulator: ", str(self.A))
            print("(XCH) Memory address: ", arg)

        # AUG instruction. Increments a positive value an negates a negative value.
        if instruction.__contains__('AUG'):
            if (arg > 0):
                arg = arg + 1
            if (arg < 0):
                arg = arg - 1
            else:
                pass
            # DEBUG
            print("(AUG) New Memory value: " + str(arg))


# Main function
def main():
    Memory.Memory[0x1FF] = 0x10
    Memory.Memory[0x200] = 0x10
    code = ["CA   0x1FF", "AD   0x200", "TS   0x1FF"]
    x = input("Instruction > ")
    CPU.processInstruction(instruction=x, self=CPU)
    main()


# name/main run check
if __name__ == '__main__':
    main()
