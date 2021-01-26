from memory import *
from Instruction import *
class CPU(object):
    def __init__(self):
        self.A = Memory.RAM[0]
        self.B = Memory.RAM[1]
        self.LR = Memory.RAM[2]
        self.EB = Memory.RAM[3]
        self.FB = Memory.RAM[4]
        self.PC = Memory.RAM[5]
        self.BB = Memory.RAM[6]
        self.O = Memory.RAM[7]

    def run_instruction(inst: Instruction):
        if inst.instIndex == "ADD":
            ADInstr.AD()

