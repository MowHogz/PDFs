import time 
import threading 
class snake: 
    def __init__(self, height, width, name, user): 
        self.height = height 
        self.width = width
        self.name = name 
        self.direction = "Right"
        self.d = "r"
        self.user = user
        self.t = threading.Thread(target= self.game, args=())
        self.num = 0 
        self.mat = creator(self.height, self.width, ' ')
        print ("This is me ")
        self.body = [[0,0]]
        self.t.start()
    def game(self):
        while True:
            time.sleep(1)
            self.run()
            text = self.display()
            #self.user.manager.bot.bot.edit_message_text(text, self.user.id, self.user.board_id)
            self.user.send(text)
            #print ("Height", self.height, "Name", self.name)

    def update_direction(self):
        if self.direction == "Right":
            self.d = "r"
        elif self.direction == "Left":
            self.d = "l"
        elif self.direction == "Up":
            self.d = "u"
        elif self.direction == "Down":
            self.d = "d"

    def run(self): 
        print ("Chocolate")
        head = self.body[0]
        new_head = head[:]
        self.update_direction()


        if self.d == "r":
            new_head[1] += 1
        
        elif self.d == "l":
            new_head[1] -= 1
        
        elif self.d == "u":
            new_head[0] -= 1
        
        elif self.d == "d":
            new_head[0] += 1

        if self.check_if_safe(new_head):
            self.body.insert(0,new_head)
            
            #remove tail 
    def check_if_safe(self, head):
        y = head[0]
        x = head[1]

        #if collides 
        if y > self.height or y < 0 or x > self.width or x < 0 : 
            return False 

        #if new locatin is safe 
        if head not in self.body:
            return True
        
        return False





        pass
    def display(self):
        mat = creator(self.height, self.width, '‏‏‎ ‎')

        for unit in self.body:
            mat[unit[0]][unit[1]] = 'X'
        
        text = printer(mat)
        print (text)

        self.num += 1
        return text

def printer(matrix):
    text = ""
    for row in range(len(matrix)):
        text += "\n"
        for column in range(len(matrix[0])):
            text += matrix[row][column]
    return text

def creator(height, width, default_space):
    mat = []
    for row in range(height):
        mat.append([])
        for column in range(width):
            mat[row].append(default_space)
    return mat