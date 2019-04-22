"""
Generate a simple BlogGen website
SheatNoisette - 2019
MIT Licence
"""

import os
from Generator import Misc

class createBGProject():
    """Create a simple template for BlogGen"""
    def __init__(self):
        pass

    def generate(self, name, path):

        # Set new project path
        projectPath = path+"/"+name+"/"

        try:
            # Make Website directory
            print("Creating project folder...")
            os.makedirs(projectPath, exist_ok=False)

            # Adding templates dir
            print("Creating template folder...")
            os.makedirs(projectPath+"templates/", exist_ok=True)

            # Add static folder
            print("Creating template folder...")
            os.makedirs(projectPath+"static/", exist_ok=True)

            # Adding basic configuration file
            print("Creating config file...")

            configToml = open(projectPath+"config.toml", "w")
            configToml.write(self.createConfig(name))
            configToml.close()

            # Adding index
            print("Creating Index Markdown...")

            indexFile = open(projectPath+"static/index.md", "w")
            indexFile.write(Misc.getSimpleMarkdown())
            indexFile.close()

            # Adding index
            print("Adding basic template...")

            # Get minimal page
            webpage = Misc.getSimpleWebpage()

            webHeadFile = open(projectPath+"templates/head.html", "w")
            webBodyFile = open(projectPath+"templates/body.html", "w")

            webHeadFile.write(webpage[0])
            webBodyFile.write(webpage[1])

            webHeadFile.close()
            webBodyFile.close()

        except Exception:
            pass
        pass

    def createConfig(self, name):
        """Create a basic TOML file"""

        basicToml = Misc.getBasicTOML()
        basicToml = basicToml.replace("$NAME", name)

        return basicToml
