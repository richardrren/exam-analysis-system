import PyInstaller.__main__
import os
import sys
import platform

print("="*50)
print("Exam Analysis System - Build Script")
print("="*50)
print()

system = platform.system()
print(f"Building for:", system)
print()

if system == "Windows":
    path_sep = ";"
    exe_ext = ".exe"
else:
    path_sep = ":"
    exe_ext = ""

pyinstaller_args = [
    'main.py',
    '--name=ExamAnalysisSystem',
    '--windowed',
    '--onedir',
    f'--add-data=config.py{path_sep}.',
    f'--add-data=pdf_parser.py{path_sep}.',
    f'--add-data=ai_client.py{path_sep}.',
    f'--add-data=excel_generator.py{path_sep}.',
    f'--add-data=node{path_sep}node',
    '--hidden-import=pandas',
    '--hidden-import=openpyxl',
    '--hidden-import=numpy',
    '--hidden-import=requests',
    '--hidden-import=tkinter',
    '--hidden-import=tkinter.ttk',
    '--hidden-import=tkinter.scrolledtext',
    '--hidden-import=tkinter.filedialog',
    '--hidden-import=tkinter.messagebox',
    '--hidden-import=subprocess',
    '--hidden-import=threading',
    '--clean',
    '--noconfirm'
]

print("Running PyInstaller...")
print()

try:
    PyInstaller.__main__.run(pyinstaller_args)

    if system == "Windows":
        dist_dir = 'dist\\ExamAnalysisSystem'
    else:
        dist_dir = 'dist/ExamAnalysisSystem'

    print()
    print("="*50)
    print("BUILD COMPLETE!")
    print("="*50)
    print()
    if system == "Windows":
        print("Program folder: dist\\ExamAnalysisSystem\\")
        print()
        print("Files created:")
        print("  - ExamAnalysisSystem.exe    (Main Application)")
        print("  - node/                     (Local Node.js + mineru-open-api)")
        print()
        print("Distribution:")
        print("  1. Zip the entire 'ExamAnalysisSystem' folder")
        print("  2. Send the ZIP to users")
        print("  3. Users double-click ExamAnalysisSystem.exe directly!")
    else:
        print("Program folder: dist/ExamAnalysisSystem/")
        print()
        print("Files created:")
        print("  - ExamAnalysisSystem          (Main Application)")
        print("  - node/                        (Local Node.js + mineru-open-api)")
        print()
        print("Distribution:")
        print("  1. Tar/Gzip the entire 'ExamAnalysisSystem' folder")
        print("  2. Send the archive to users")
        print("  3. Users run ExamAnalysisSystem directly!")
        print("  4. Or use build.sh script is provided for convenience")
    print()
    print("Note: Everything is included locally!")
    print("No installation required for users!")
    print("="*50)

except Exception as e:
    print(f"Build error: {e}")
    print()
    print("Try running manually:")
    print("pip install -r requirements.txt")
    if system == "Windows":
        print("python -m PyInstaller main.py --windowed --onedir --name=ExamAnalysisSystem")
    else:
        print("python3 -m PyInstaller main.py --windowed --onedir --name=ExamAnalysisSystem")