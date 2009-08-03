#!/opt/local/bin/python

import console
import configuration
import os

homedir = os.path.expanduser("~")
config = configuration.Configuration(homedir+"/.twshrc")
conf = config.get_configuration()
cli = console.Console(conf)
cli.cmdloop()
