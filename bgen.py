"""
Simple blog generator written in python
SheatNoisette - 2019
MIT Licence
"""

import sys
from Generator import Misc
from Generator import createProject
from Generator import buildProject

class BlogGen():
    """Simple blog generator written in python."""

    def __init__(self):
        pass


    def runCli(self, params):

        # Get number of arguments
        paramsLength = len(params)

        # Get command name
        command = ""

        # Override command name
        if paramsLength != 0:
            command = params.pop(0)
            paramsLength -= 1

        # Run command
        if command in {"c", "create"} and paramsLength == 2:

            print("Creating BlogGen template " + str(params[0]) + " at " + str(params[1]) + "...")

            # Create object
            createWebsite = createProject.createBGProject()

            # Create template at selected path
            createWebsite.generate(params[0], params[1])

        elif command in {"b", "build"} and paramsLength == 1:
            print("Building website...")

            genWebsite = buildProject.websiteGenerator()
            genWebsite.build(params[0])

        else:
            print(Misc.getLogo() + "\n" + Misc.getHelp())

if __name__ == '__main__':

    # Get program arguments
    programArgs = sys.argv

    # Drop the script name
    programArgs.pop(0)

    # Create a new instance of BlogGen
    bg = BlogGen()

    # Run tool
    bg.runCli(programArgs)
