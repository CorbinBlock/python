import subprocess
import os


def open_programs():
    # define paths to executables
    driveletter = "C:"
    basepath = "\\Program Files\\"
    basepath86 = "\\Program Files (x86)\\"
    # shortcutpath = "\\ProgramData\\Microsoft\\Windows\\StartMenu\\Programs"
    chrome = os.path.join(driveletter, basepath, "Google\\Chrome\\Application\\chrome.exe")
    notepadplusplus = os.path.join(driveletter, basepath86, "Notepad++\\notepad++.exe")
    vscode = os.path.join(driveletter, basepath, "Microsoft VS Code\\bin\\code.cmd")
    keepass = os.path.join(driveletter, basepath86, "KeePass Password Safe 2\\KeePass.exe")
    # outlook = os.path.join(driveletter, shortcutpath,"Outlook.lnk")
    # TODO - fix Outlook
    outlook = os.path.join(driveletter, basepath, "Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
    pycharm = os.path.join(driveletter, basepath, "JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe")
    onenote = os.path.join(driveletter, basepath, "Microsoft Office\\root\\Office16\\ONENOTE.EXE")
    winSCP = os.path.join(driveletter, basepath86, "WinSCP\\WinSCP.exe")
    sophos = os.path.join(driveletter, basepath86, "Sophos\\Sophos Home\\SophosUI.exe")
    spotify = os.path.join(driveletter, "\\Users\\Corbin\\AppData\\Roaming\\Spotify\\Spotify.exe")
    githubdesktop = os.path.join(driveletter, "\\Users\\Corbin\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")


    # arrange into list and store length
    list = [vscode, notepadplusplus, keepass, outlook, chrome, onenote, winSCP, sophos, spotify, githubdesktop] # pycharm
    length = len(list)
    # iterate through list to open all programs
    for i in range(length):
        subprocess.Popen(list[i]) 

open_programs()
