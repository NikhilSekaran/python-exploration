# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class CustomError(Exception):
    def __init__(self, message=None):
        self.error_code = 200
        self.message = message
        super().__init__(self.message)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    if name == 'Name1':
        raise CustomError(message="print failed due to CustomError")
    elif name == 'Name2':
        raise Exception("print failed for due to Exception")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        # print_hi('PyCharm')
        print_hi('Name1') # output is: 'print failed due to CustomError' all
        # attributes of CustomerError class can be accessed as well
        # print_hi('Name2')   # output is: 'print failed for due to Exception'
    except Exception as e:
        if isinstance(e, CustomError):
            print(e.error_code)
            print(e.message)
        else:
            print(e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
