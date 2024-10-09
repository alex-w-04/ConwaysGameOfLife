class Field:
    def __init__(self, x, y):
        self.x_field = x
        self.y_field = y
        self.field = [[0 for _ in range(self.x_field+2)] for _ in range(self.y_field+2)] 
    

    def show(self):
        for y in range(1, self.y_field):
            line = str(self.field[y]).strip("[]")[1:-2]
            print(line.replace(",", ""))
    
    def place(self, y, x, val:int):
        self.field[y][x] = val
        return self
    
    def empty(self):
        self.field = [[0 for _ in range(self.x_field+2)] for _ in range(self.y_field+2)] 
        return self.field
    

    def count_neightbours(self, y , x):
        left = x-1
        right = x+1
        top = y-1
        bottom = y + 1
        
        if left < 1:
            left = -2
        if right > self.x_field :
            right = 1
        if top < 1:
            top = -2
        if bottom > self.y_field :
            bottom = 1

        proofArr = [self.field[top][left], self.field[top][x], self.field[top][right], self.field[y][left], self.field[y][right], self.field[bottom][left], self.field[bottom][x], self.field[bottom][right] ]
        count = proofArr.count(1)
        return count



    def run_show(self, t):
        for x in range(t):
            copy_field = [[0 for _ in range(self.x_field+2)] for _ in range(self.y_field+2)] 
            for y in range(1,self.y_field+1):
                for x in range(1,self.x_field+1):
                    count = self.count_neightbours(y,x)
                    if self.field[y][x] == 1:
                        if count == 2 or count == 3:
                            copy_field[y][x] = 1
                        else:
                            copy_field[y][x] = 0
                    else: 
                        if count == 3:
                            copy_field[y][x] = 1
                        else:
                            copy_field[y][x] = 0

                    
            self.field = copy_field
            self.show()
            print("")
    
    def run_return(self):
        
        copy_field = [[0 for _ in range(self.x_field+2)] for _ in range(self.y_field+2)] 
        for y in range(1,self.y_field+1):
            for x in range(1,self.x_field+1):
                count = self.count_neightbours(y,x)
                if self.field[y][x] == 1:
                    if count == 2 or count == 3:
                        copy_field[y][x] = 1
                    else:
                        copy_field[y][x] = 0
                else: 
                    if count == 3:
                        copy_field[y][x] = 1
                    else:
                        copy_field[y][x] = 0

                
        self.field = copy_field
        return self.field
        


def main():

    field = Field(30,15)
    field = field.place(12,4,1)
    field = field.place(13,4,1)
    field = field.place(14,4,1)
    field = field.place(12,5,1)
    field = field.place(14,5,1)
    field = field.place(12,6,1)
    field = field.place(14,6,1)
    field = field.place(12,8,1)
    field = field.place(14,8,1)
    field = field.place(12,9,1)
    field = field.place(14,9,1)
    field = field.place(12,10,1)
    field = field.place(13,10,1)
    field = field.place(14,10,1)
    field.show()
    print("")
    field.run_show(4)    
    


if __name__ == '__main__':
    main()