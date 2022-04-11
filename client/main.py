from src.controller import Controller


controller = Controller()
while True:
    arg = input(">>> ")
    if arg == 'q':
        exit()
    controller.handle(arg)

