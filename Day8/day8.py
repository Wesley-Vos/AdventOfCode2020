def fix_loop(instructions):
    for line, instruction in enumerate(instructions):
        optcode = instruction[0:3]
        operand = instruction[4:]
        if optcode in ("jmp", "nop"):
            instruct_cp = instructions.copy()
            instruct_cp[line] = ("jmp" if optcode ==
                                 "nop" else "nop") + operand
            game_console = Console(instruct_cp)
            if game_console.boot():
                break


class Console:
    def __init__(self, instructions, report_loop=False):
        self.instructions = instructions
        self.report_loop = report_loop

    def boot(self):
        PC = 0
        accumulator = 0
        used_lines = []
        while PC < len(self.instructions):
            if PC in used_lines:
                if self.report_loop:
                    print("CRITICAL | Loop detected, accumulator is", accumulator)
                return 0
            used_lines.append(PC)
            optcode = self.instructions[PC][0:3]
            operand = int(self.instructions[PC][4:])
            accumulator += operand if optcode == "acc" else 0
            PC += operand if optcode == "jmp" else 1
        print("SUCCESS | Booted successfull, accumulator is", accumulator)
        return 1


def main():
    instructions = file.input("inputs/day8.txt")

    print("Boot for the first time")
    game_console = Console(instructions, report_loop=True)
    game_console.boot()
    print("Try to avoid loop by replacing one 'jmp' instruction with 'nop'")
    fix_loop(instructions)


if __name__ == "__main__":
    main()
