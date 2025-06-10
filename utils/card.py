class Symbol:

    icon = ["♥", "♦", "♣", "♠"]                                                    
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


    def __init__(self, icon: str, color: str):
        self.color = color
        self.icon = icon           


    def __str__(self):   
        return f"{self.color} {self.icon }"                                         

class Card(Symbol):

    def __init__(self, icon, value, color):
        super().__init__(icon, color)                                           
        self.value = value


    def __str__(self):                                                             
           return f" {self.value} {self.icon} {self.color}"