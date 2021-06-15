from cx_Freeze import setup, Executable

base = None

executables = [Executable("ss.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="<Screenshot>",
    options=options,
    version="0.11",
    description='Screenshot Progrm',
    executables=executables
)
