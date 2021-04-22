#2.0.0 - Beta 
# we made some temporary changes (left commented out) used to send the album cover for Beta testing 
from main import download
from snake import snake 
class user:
    def __init__(self,manager, client_info,location , message = " ", admin = False):
        
        self.manager = manager 
        self.admin = admin          #bool
        self.client_info = client_info
        try:    self.name = client_info['first_name']
        except: self.name = "Unknown"

        self.id = client_info['id']
        self.location = location
        self.download = download(self.location)
        self.snake = snake(10,10,"Ruby", self)

        self.count = 0
    def send(self, message):
        return self.manager.bot.send_message(self.id, message)
        
    def run(self, message):
        if self.count > 0:
            if message == "Right":
                self.snake = snake(10,10,"Ruby", self)
                self.snake.t.start()
                self.send("Good Game!\n Press Right to start again")
            self.snake.direction = message
            #self.manager.bot.edit_message_text(text, self.id, self.board_id)
        else: 
            
            self.count += 1
            
            self.send("The bot has received message number " + str(self.count))
            self.board_id = self.send("This is gonna be the board game").message_id
            
            print (self.board_id)
            
            #self.snake.run(message)
            
            
            return "You have accessed the run function of the user, You have done this {} times".format(self.count)
