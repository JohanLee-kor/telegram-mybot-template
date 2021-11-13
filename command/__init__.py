from . import help, start

__all__ = ['help', 'start', 'unknown']


# command_callback = {
#     'help': help.do,
#     'start': start.do
# }
#
#
# def create(command_name):
#     return CommandHandler(command_name, command_callback[command_name])

def unknown():
    pass
