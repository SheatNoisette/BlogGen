"""
Misc functions
"""

def getHelp():
    return """c / create <name> <path>- Create a new BlogGen Project\nb / build <path> - Generate website"""

def getLogo():
    toolLogo = """
     _______  ___      _______  _______  _______  _______  __    _
    |  _    ||   |    |       ||       ||       ||       ||  |  | |
    | |_|   ||   |    |   _   ||    ___||    ___||    ___||   |_| |
    |       ||   |    |  | |  ||   | __ |   | __ |   |___ |       |
    |  _   | |   |___ |  |_|  ||   ||  ||   ||  ||    ___||  _    |
    | |_|   ||       ||       ||   |_| ||   |_| ||   |___ | | |   |
    |_______||_______||_______||_______||_______||_______||_|  |__|

    """
    return toolLogo

def getBasicTOML():
    """Basic TOML configuration file for BlogGen"""

    toml = """[BlogGen]\nProjectFolder = "$NAME"\nWebsiteTitle = "$NAME" \nWebsiteLink = "www.example.com" \nTemplateFolder = "templates"
    """
    return toml

def getSimpleMarkdown():
    """Simple Markdown document"""

    md = """|---
|PageName:Index
|PageTitle:Index
|Type:Home
|---
# Welcome to my website!
"""
    return md

def getSimpleWebpage():

    headPage = """
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>$NAME - $PAGENAME</title>
  </head>
  <body>
"""
    bodyPage = """
    </body>
    </html>
"""
    return (headPage, bodyPage)
