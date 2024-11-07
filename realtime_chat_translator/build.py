
import PyInstaller.__main__

#only for windows
PyInstaller.__main__.run([
     'twitchChatTranslator.py',
        '--clean',
        '--onefile',
        '--hidden-import=pywin32',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=twitchChatTranslator.exe'
])