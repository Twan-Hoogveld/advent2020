class Person:
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.treesPassed = 0

    def move(self,posX = 3, posY = 1):
        self.positionX += posX
        self.positionY += posY

    def __str__(self):
        return f'X[{self.positionX}],Y[{self.positionY}]'

    def checkForTree(self,sym):
        if sym == '#':
            self.treesPassed += 1

with open("inp.txt") as f:

    me = Person()

    field = []
    for line in f:
        line = line.strip('\n')
        field.append(list(line))

    while(me.positionY < len(field)):

        if(me.positionY == 322):
            me.move()
            me.checkForTree(field[me.positionY - 1][me.positionX])
            print(me.treesPassed)
            break

        try:
            me.move()
            me.checkForTree(field[me.positionY][me.positionX])
        except IndexError:
            #Double the list in size before checking, no index error.
            field[me.positionY] = field[me.positionY] * 100
            me.checkForTree(field[me.positionY][me.positionX])
