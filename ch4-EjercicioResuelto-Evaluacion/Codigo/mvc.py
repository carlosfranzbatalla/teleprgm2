#!/usr/bin/python3
import sys
import controller


def main():
    print(sys.version)
    vControlador = controller.terminalController()
    vControlador.run()

if __name__ == '__main__':
    main()
    