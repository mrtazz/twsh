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
        self.re_prompt=re.compile("prompt=")
        self.re_timestamp=re.compile("timestamp=")
        self.re_screennames=re.compile("screennames=")
        # read data from configfile
        self.read_config_file(self.filepath)       
        
    def read_config_file(self, filepath):
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
                elif self.re_prompt.match(line):
                    self.configuration['prompt'] = self.re_prompt.sub("",line).rstrip(' \n').upper()
                elif self.re_timestamp.match(line):
                    self.configuration['timestamp'] = self.re_timestamp.sub("",line).rstrip(' \n').upper()
                elif self.re_screennames.match(line):
                    self.configuration['screennames'] = self.re_screennames.sub("",line).rstrip(' \n').upper()
                else:
                    pass
            self.f.close()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
    def get_configuration(self):
        ''' This function returns the configuration data
        '''
        return self.configuration