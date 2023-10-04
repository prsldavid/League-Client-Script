import os
import winshell
import psutil

"""
Written by: one and only DAVAABAYAR PUREVDASH
"""


def is_process_running(process_name):
    '''Check if there is any running process that contains the given name.'''
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def main():
    # Check if LeagueClient is running
    if is_process_running("LeagueClient.exe"):
        return  # Exit if it is running

    shortcut_name = "LeagueClient"
    exe_path = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"

    # Delete existing shortcut if it exists
    desktop_path = winshell.desktop()
    existing_shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")
    if os.path.exists(existing_shortcut_path):
        os.remove(existing_shortcut_path)

    # Create a new shortcut with the specified properties
    winshell.CreateShortcut(Path=existing_shortcut_path, Target=exe_path, Arguments="--locale=\"en_US\"")

if __name__ == "__main__":
    main()
