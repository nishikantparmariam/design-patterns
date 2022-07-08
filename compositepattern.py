class TodoList:

    def display(self):
        raise NotImplemented


class Todo(TodoList):

    def __init__(self, depth):
        self.depth = depth

    def display(self):
        print('{ }', end="")


class Project(TodoList):

    def __init__(self, todolists, depth):
        self.todolists = todolists
        self.depth = depth


    def display(self):       
        print('{', end="")
        for todolist in self.todolists:
            todolist.display()  
        print('}', end="")


def main():

    todo1 = Todo(1)

    todo21 = Todo(2)
    todo22 = Todo(2)
    todo2 = Project([todo21, todo22],1)
    todo311 = Todo(3) 
    todo312 = Todo(3)
    todo31 = Project([todo311, todo312],2)
    todo32 = Todo(2)
    todo33 = Todo(2)
    todo3 = Project([todo31, todo32, todo33],1)
    todo4 = Todo(1)   

    todo = Project([todo1, todo2, todo3, todo4], 0)

    todo.display()



main()
