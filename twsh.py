#!/opt/local/bin/python

import console
import fileIO
import os

homedir = os.path.expanduser("~")
configurator = fileIO.Configuration(homedir+"/.twshrc")
configuration = configurator.getUserInfo()
cli = console.Console(configuration['user'],configuration['password'])
cli.cmdloop()
