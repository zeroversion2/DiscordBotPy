from cmd import Cmd


class BotShell(Cmd):
    def do_exit(self, inp):
        print("bye")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))
