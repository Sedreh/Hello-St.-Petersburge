import os
import sys

from Task9 import *


def main(args):
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            path = cwd.path if not cmdargs else cmdargs[0]
            cwd = Directory(os.path.join(cwd.path, path))
        elif cmd == 'cat':
            path = cwd.path if not cmdargs else cmdargs[0]
            file = File(path)
            print(file.getcontent())
        elif cmd == 'head':
            path = cwd.path if not cmdargs else cmdargs[0]
            file = File(path)
            print(file.getcontent(max_lines))
        elif cmd == 'tail':
            path = cwd.path if not cmdargs else cmdargs[0]
            file = File(path)
            print(file.getcontent(max_lines, head = False))
        elif cmd == 'pwd':
            print(cwd.path)
        elif cmd == 'touch':
            path = cwd.path if not cmdargs else cmdargs[0]
            file = File(path)
            file.create()
        elif cmd == 'find':
            name = "." if not cmdargs else cmdargs[0]
            sub_dir = cwd.getsubdirectory(name)
            print("\n".join([file.path for file in sub_dir.files()]))
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
