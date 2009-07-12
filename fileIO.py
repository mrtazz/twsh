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
        self.filepath = filepath        
        # regex definitions for configurations
        self.re_username = re.compile("username=")
        self.re_password = re.compile("password=")
        self.re_refreshtime = re.compile("refreshtime=")
        self.re_usessl = re.compile("usessl=")
        
        self.readConfigFile(self.filepath)       
        
    def readConfigFile(self, filepath):
        ''' The config file specified via filepath is opened and
            the values are read and stored in the object variables
        '''
        try:
            self.f = open(self.filepath, 'r')
            for line in self.f:
                if self.re_username.match(line):
                    self.username = self.re_username.sub("",line).rstrip(' \n')
                elif self.re_password.match(line):
                    self.password = self.re_password.sub("",line).rstrip(' \n')
                elif self.re_refreshtime.match(line):
                    self.refreshtime = self.re_refreshtime.sub("",line).rstrip(' \n')
                elif self.re_usessl.match(line):
                    self.usessl = self.re_usessl.sub("",line).rstrip(' \n')
                else:
                    pass
            self.f.close()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
    def getUserInfo(self):
        ''' This function returns the user infos read from the
            file as a dictionary
        '''
        self.ret = {'user': self.username, 'password':self.password,'refreshtime': self.refreshtime, 'ssl': self.usessl}
        return self.ret