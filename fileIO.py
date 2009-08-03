import re
import sys

class Configuration:
    ''' This class provides storage for the application configuration
        and an interface to a configuration file
    '''

    def __init__(self, filepath):
        ''' On instantiation time the regexes for matching the 
            properties in the configuration file are set. Also
            the filepath is set and the file read function is
            executed
        '''
        # Color definitions
        self.color = {
                        'RESET' : "\033[0m",
                        'RED' : "\033[31m",
                        'BLACK' : "\033[30m",
                        'GREEN' : "\033[32m",
                        'YELLOW' : "\033[33m",
                        'BLUE' : "\033[34m",
                        'PURPLE' : "\033[35m",
                        'CYAN' : "\033[36m",
                    }
        self.configuration = { }
        self.filepath = filepath        
        # regex definitions for configurations
        self.re_username = re.compile("username=")
        self.re_password = re.compile("password=")
        self.re_refreshtime = re.compile("refreshtime=")
        self.re_usessl = re.compile("usessl=")
        # read data from configfile
        self.readConfigFile(self.filepath)       
        
    def readConfigFile(self, filepath):
        ''' The config file specified via filepath is opened and
            the values are read and stored in the object variables
        '''
        try:
            self.f = open(self.filepath, 'r')
            for line in self.f:
                if self.re_username.match(line):
                    self.configuration['username'] = self.re_username.sub("",line).rstrip(' \n')
                elif self.re_password.match(line):
                    self.configuration['password'] = self.re_password.sub("",line).rstrip(' \n')
                elif self.re_refreshtime.match(line):
                    self.configuration['refreshtime'] = self.re_refreshtime.sub("",line).rstrip(' \n')
                else:
                    pass
            self.f.close()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
    def getConfiguration(self):
        ''' This function returns the configuration data
        '''
        return self.configuration