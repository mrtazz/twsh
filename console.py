import sys
import cmd
import readline
import TweetUpdateThread
try:
    import twitter
except:
    print "error while loading twitter module."
    sys.exit()
import os

# Color definitions
color = {
            'RESET' : "\033[0m",
            'RED' : "\033[31m",
            'BLACK' : "\033[30m",
            'GREEN' : "\033[32m",
            'YELLOW' : "\033[33m",
            'BLUE' : "\033[34m",
            'PURPLE' : "\033[35m",
            'CYAN' : "\033[36m",
        }


class Console(cmd.Cmd):
    ''' This class creates the CLI with the whole UI stuff '''

    def __init__(self, configuration):
        ''' The shell is initialized with a twsh prompt and
            and an intro message. Also the background thread
            to fetch new tweets is started here
        '''
        self.configuration = configuration
        try:
            cmd.Cmd.__init__(self)
            self.prompt = color[configuration['prompt']]+"twsh> "+color[configuration['RESET']]
            #self.intro = "When I grow up, I get to be a twitter shell"
            self.updater = TweetUpdateThread.TweetUpdateThread(self, "hello", 30)
            self.api = twitter.Api(self.configuration['username'],self.configuration['password'])
            #self.updater.start()
        except:
            print "Init failed."
            raise
            #self.updater.setend()
            sys.exit(-1)
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
        try:
            self.statuses = self.api.GetUserTimeline(friend, 20)
        except:
            print "Could not get user timeline."
            sys.exit(-1)
            
        self.statuses.reverse()
        print "Public status messages for %s:" % (friend)
        for s in self.statuses:
            print '%s%s: %s' % (color[self.configuration['timestamp']],s.relative_created_at,color[self.configuration['RESET']])
            print '%s>> %s%s' % (color[self.configuration['prompt']],color[self.configuration['RESET']],s.text.encode("utf-8"))
                    
    def do_friends(self, args):
        ''' Print the list of friends for the authenticated user '''
        try:
            self.friends = self.api.GetFriends()
        except:
            print "Could not get friends list."
            sys.exit(-1)
            
        print "You are following:"
        for f in self.friends:
            print '+ %s%s%s' % (color[self.configuration['screennames']],f.screen_name,color[self.configuration['RESET']])

    def do_refresh(self,args=False):
        ''' Get the tweets of your friends '''
        try:
            updates = self.api.GetFriendsTimeline()
        except:
            print "Could not get friends timeline."
            sys.exit(-1)
            
        updates.reverse()
        for u in updates:
            print '%s%s %s%s: %s' % (color[self.configuration['screennames']],u.user.name.encode("utf-8"),
                                        color[self.configuration['timestamp']],u.relative_created_at,
                                        color[self.configuration['RESET']])
            print '%s>> %s%s' % (color[self.configuration['prompt']],color['RESET'],u.text.encode("utf-8"))
            
    def do_tweet(self,args):
        ''' Post a new tweet'''
        try:
            self.api.PostUpdate(args)
        except:
            print "Could not post update."
            sys.exit(-1)
