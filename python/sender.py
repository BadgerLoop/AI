import riffle

riffle.SetFabricLocal()
# riffle.SetLogLevelDebug()


class Send(riffle.Domain):

    def onJoin(self):

        while True:
            userInput = raw_input("Enter something to send: ")
            s = self.call("message", userInput).wait(str)
            print s #this is the response from the backend

if __name__ == '__main__':
    app = riffle.Domain("xs.demo.test")
    Send("example", superdomain=app).join()
    exit()