#!/opt/local/bin/python2.5

import console
import fileIO

configurator = fileIO.Configuration("twshrc")
configuration = configurator.getUserInfo()
cli = console.Console(configuration['user'],configuration['password'])
cli.cmdloop()
