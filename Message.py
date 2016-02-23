class Message():

    def __init__(self):
        self.message = ""

    def addMessage(self, message):
        self.message += message

    def displayMessage(self):
        print(self.message)
