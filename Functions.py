FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read and return items in a text file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write items in a text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(__name__)
# if __name__ == "__main__":
    # print("Hello")
