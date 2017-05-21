from . import InstructionSet, byte, int

adaFruitServoSet = InstructionSet(name="adaFruitServo")

instructions = [
    [0, "setAdaPWM", byte + int]
]

for inst in instructions:
    id = inst[0]
    name = inst[1]
    types = inst[2]
    adaFruitServoSet.setInstruction(id, name, types)
