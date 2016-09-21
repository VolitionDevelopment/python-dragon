class Menu:
    def __init__(self, options):
        self.options = options

    def print_menu(self):
        hambone = '===============================\n'

        for option in self.options:
            hambone += option.title + "\n"
        return hambone + "===============================\n\n>> "


class Option:
    def __init__(self, title, function):
        self.title = title
        self.function = function

    def execute(self):
        return self.function()
