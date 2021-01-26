from CPU import CPU
class Instruction:
    def __init__(self):
        self.instIndex


cpu = CPU()
class ADInstr(Instruction):
    def AD(self, adress):
        cpu.A = adress

    def __init__(self):
        self.instIndex = "ADD"