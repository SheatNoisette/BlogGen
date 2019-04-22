"""
Generate project for BlogGen
SheatNoisette - 2019
MIT Licence
"""

import toml
import mistune
#import markdown
import os

class websiteGenerator():
    """docstring for ."""
    def __init__(self):
        pass

    def build(self, path):

        # Load TOML config file
        config = self.loadConfig(path)

        # Make a export directory
        os.makedirs(path+"/exported/", exist_ok=True)

        # Create mistune instance
        mistuneMarkdown = mistune.Markdown()

        # Merge template and static but omit template files and markdown docs
        # @TODO!

        # find markdown files to be parsed
        markFiles = self.findMarkdownFile(path+"/static/")

        # Parse every markdown file and output to exported with hopefully the right path

        # 'Static' path length
        staticPathLength = len(path+"/static/")

        for file in markFiles:

            # Get output path - Remove Static path
            outputPath = file[0][staticPathLength:]

            # Create folder(s) if needed
            if len(outputPath) is not 0:
                os.makedirs("./"+config["BlogGen"]["ProjectFolder"]+"/exported/" + outputPath, exist_ok=True)

            # Make a file and parse content
            filePath = "./"+config["BlogGen"]["ProjectFolder"]+"/exported/" + outputPath + file[1].replace(".md", "") + ".html"
            outputFile = open(filePath, "w")

            # Get the markdown file proprieties
            fileProps = self.getMarkdown("./"+file[0]+file[1])

            # Parse markdown in document
            # Mistune
            markdownOut = mistuneMarkdown(fileProps[1])

            # Name of the page
            currentPageName = fileProps[0]["PageTitle"]

            # Output the html page
            outputFile.write(self.generatePage(config["BlogGen"]["WebsiteTitle"], currentPageName, path + "/" + config["BlogGen"]["TemplateFolder"], markdownOut))

            # Close file
            outputFile.close()

            print("-> " + str(filePath))

    def loadConfig(self, path):
        """Load the TOML config file"""

        parsedConfig = None

        try:
            # Try to open a the project config file
            tomlConfig = open(path+"/config.toml", "r")
            parsedConfig = toml.loads(tomlConfig.read())

        except Exception:
            raise Exception("Could not load config file")

        print("TOML '" + parsedConfig["BlogGen"]["WebsiteTitle"] + "' project config loaded")

        return parsedConfig

    def generatePage(self, projectName, pageName, templatePath, content):
        """Create a webpage using templates"""
        # @TODO: Keep templates in memory

        # Load templates
        try:
            headTemplate = open(templatePath+"/head.html")
            bodyTemplate = open(templatePath+"/body.html")

        except Exception:
            raise Exception("Couldn't load template files")

        # Load files
        headPage = headTemplate.read()
        bodyPage = bodyTemplate.read()

        # Add page title and project folder
        headPage = headPage.replace("$NAME", projectName)
        headPage = headPage.replace("$PAGENAME", pageName)

        return headPage + content + bodyPage

    def findMarkdownFile(self, path):
        """Find md file in directory"""
        mdFiles = []

        for root, d, files in os.walk("./"+path):

            for filename in files:
                # Join path and filename
                currentFile = os.path.join(root, filename)

                # Check the file extension
                if currentFile[-3:] == ".md":
                    # Add to the list and remove extension
                    currentFile = currentFile[:len(currentFile)-3]

                    # /!\ NASTY HACK
                    if root[-1:] is not "/":
                        root += "/"

                    mdFiles.append([root[2:], filename])

        return mdFiles

    def getMarkdown(self, path):
        """Return a tuple which contains ({Parameters}, 'markdown')"""

        mdFile = open(path, "r")
        # Get the content
        fileContent = mdFile.readlines()
        mdFile.close()

        # Length of the file
        fileLength = len(fileContent)

        # Set to true when we get the separator
        endParam = False

        # Markdown parameters
        parameters = {}
        # Effective content
        markdownContent = ""

        # Cursor for iterating
        fileCursor = 0

        while fileCursor < fileLength:

            # Remove \n
            fileContent[fileCursor] = fileContent[fileCursor].rstrip()

            # Add parameters until "|---" separator
            if fileContent[fileCursor] == "|---":
                endParam = True
                # Do not add "|---" as markdown
                fileCursor += 1

            if not endParam:
                if fileContent[fileCursor][:1] == "|":
                    # Extract parameters
                    currentLine = fileContent[fileCursor][1:]
                    currentParam = currentLine.split(":")

                    parameters[currentParam[0]] = currentParam[1]
                else:
                    print("Unknown option: " + fileContent[fileCursor])
            else:
                # Add markdown
                markdownContent += fileContent[fileCursor] + "\n"

            # Next line
            fileCursor += 1

        return (parameters, markdownContent)
