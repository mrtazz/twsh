import cmd
import readline
import TweetUpdateThread
import twitter
import os

# Color definitions
RESET = "\033[0m"
RED = "\033[31m"
BLACK = "\033[30m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"

class Console(cmd.Cmd):
    ''' This class creates the CLI with the whole UI stuff '''

    def __init__(self, twuser, twpass):
        ''' The shell is initialized with a twsh prompt and
            and an intro message. Also the background thread
            to fetch new tweets is started here
        '''
        cmd.Cmd.__init__(self)
        self.prompt = RED+"twsh> "+RESET
        #self.intro = "When I grow up, I get to be a twitter shell"
        self.twuser = twuser
        self.twpass = twpass
        #self.updater = TweetUpdateThread.TweetUpdateThread(self, "hello", 30)
        self.api = twitter.Api(username=twuser, password=twpass)
        #self.updater.start()
        
    def preloop(self):
        ''' Stuff to execute before the cmd.loop starts.
            Only the array to hold the cmd history is setup here
        '''
        cmd.Cmd.preloop(self)
        self._hist = []
        os.system("clear")
        print "Fetching new tweets..."
        self.do_refresh()
        
    def precmd(self, line):
        ''' Code to be executed before the actual command. Here we add
            the command to the history and then we return the line to
            the cmd loop
        '''
        self._hist += [line.strip()]
        return line
        
    def default(self, line):
        ''' The default action for a command, which is not found in the
            available commands section
        '''
        print "Erm, maybe you meant something, like, completely different?"
        
    def postloop(self):
        ''' Stuff to execute when the cmd.loop exits. Here we call the
            standard cmd.postloop() and then print a nice exit message
        '''
        cmd.Cmd.postloop(self)
        print "Going home..."
    
    def emptyline(self):
        ''' When an empty line is entered, we just return another prompt
        '''
        pass
        
# available commands
    
    def do_hello(self,args):
        ''' By historical reason  '''
        print "Hello World!"
        
    def do_exit(self, args):
        ''' End the shell '''
        #self.updater.setend()
        return -1
        
    def do_logout(self, args):
        ''' End the shell '''
        return self.do_exit(args)
        
    def do_quit(self, args):
        ''' End the shell '''
        return self.do_exit(args)
        
    def do_public(self, friend):
        ''' Get the  public user time line '''
        self.statuses = self.api.GetUserTimeline(friend, 20)
        self.statuses.reverse()
        print "Public status messages for %s:" % (friend)
        for s in self.statuses:
            print '%s%s: %s' % (RED,s.relative_created_at,RESET)
            print '%s>> %s%s' % (PURPLE,RESET,s.text.encode("utf-8"))
                    
    def do_friends(self, args):
        ''' Print the list of friends for the authenticated user '''
        self.friends = self.api.GetFriends()
        print "You are following:"
        for f in self.friends:
            print '+ %s%s%s' % (CYAN,f.screen_name,RESET)

    def do_refresh(self):
        ''' Get the tweets of your friends '''
        updates = self.api.GetFriendsTimeline()
        updates.reverse()
        for u in updates:
            print '%s%s %s%s: %s' % (GREEN,u.user.name.encode("utf-8"),RED,u.relative_created_at,RESET)
            print '%s>> %s%s' % (PURPLE,RESET,u.text.encode("utf-8"))
            
    def do_tweet(self,args):
        ''' Post a new tweet'''
        self.api.PostUpdate(args)
