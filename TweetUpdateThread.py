# thread class for updating tweets in the background       

import time
import threading
 
class TweetUpdateThread(threading.Thread):
        ''' thread class to fetch tweets in the background '''
        def __init__(self, cli_object, function, waittime):
            ''' At initialization some local variables are set:
                waittime = the time to wait between tweet fetches
                cli = the cli object from which the update cmd is called
                function = the update function to call from the cli object
                endme = boolean value to determine whether to stop the thread
                counter = counting the sleeps until the next update
            '''
            threading.Thread.__init__(self)
            self.waittime = waittime
            self.cli = cli_object
            self.function = function
            self.endme = False
            self.counter = 0
            
        def stop(self):
            ''' stop the thread '''
            threading.Thread.__stop(self)
            
        def run(self):
            ''' The thread is run here until the endme variable is set
                to true. While running the thread executes the passed 
                cli function in intervals of waittime. Time may differ if
                this thread is run a long time because of command execution
                delays. Has to be tested. The construct with checking the
                endme variable every second secures that the user doesn't
                have to wait another waittime interval (worst case) until
                the thread is ended
            '''
            while self.endme == False:
                if self.counter == self.waittime:
                    self.counter = 0
                    self.cli.do_hello("")
                else:
                    self.counter = self.counter + 1
                    time.sleep(1)
                
        def setend(self):
            ''' Interface to set the end of the thread '''
            self.endme = True