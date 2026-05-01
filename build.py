import PyInstaller.__main__
import os
import shutil

print("="*50)
print("Exam Analysis System - Build Script")
print("="*50)
print()

pyinstaller_args = [
    'main.py',
    '--name=ExamAnalysisSystem',
    '--windowed',
    '--onedir',
    '--add-data=config.py;.',
    '--add-data=pdf_parser.py;.',
    '--add-data=ai_client.py;.',
    '--add-data=excel_generator.py;.',
    '--add-data=node;node',
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

    dist_dir = 'dist\\ExamAnalysisSystem'

    print()
    print("="*50)
    print("BUILD COMPLETE!")
    print("="*50)
    print()
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
    print()
    print("Note: Everything is included locally!")
    print("No installation required for users!")
    print("="*50)

except Exception as e:
    print(f"Build error: {e}")
    print()
    print("Try running manually:")
    print("pip install -r requirements.txt")
    print("python -m PyInstaller main.py --windowed --onedir --name=ExamAnalysisSystem")