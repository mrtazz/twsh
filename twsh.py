#!/opt/local/bin/python

import console
import fileIO

configurator = fileIO.Configuration("twshrc")
configuration = configurator.getUserInfo()
cli = console.Console(configuration['user'],configuration['password'])
cli.cmdloop()
