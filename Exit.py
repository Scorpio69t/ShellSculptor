from Command import Command
import sys


def valid_code(exit_code) -> bool:
    try:
        int(exit_code)
    except ValueError:
        return False
    else:
        return True


class Exit(Command):

    def execute(self):
        if len(self._argument) == 1:
            exit()
        elif len(self._argument) == 2:
            exit_code = self._argument[1]
            if valid_code(exit_code):
                exit()
            else:
                print(f"exit: non-integer exit code provided: {self._argument[1]}", file=sys.stderr)
        elif len(self._argument) > 2:
            print("exit: too many arguments", file=sys.stderr)

