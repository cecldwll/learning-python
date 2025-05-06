Chapter 3: How You Run Programs

Installing Python

Interactive Code
    Starting an Interactive REPL
    Where to Run: Code Folders
    What Not to Type: Prompts and Comments
    Other Python REPLs
    Running Code Interactively
    Why the Interactive Prompt?

Program Files
    A First Script
    Running Files with Command Lines
    Command-Line Usage Variations

Other Ways to Run Files
    Clicking and Tapping File Icons
    The IDLE Graphical User Interface
    Other IDEs for PythonSmartphone Apps
    WebAssembly for Browsers
    Jupyter Notebooks for Science
    Ahead-of-Time Compilers for Speed 
    Running Code in Code 
    Other Launch Options

Which Option Should I Use?



Summary/Notes:
    - A Python interactive session can be started by typing a Python command line in your system's console window.
    - You type system command lines in the same interface used to launch an interactive session by command line.
    - Coode in a script/module file can be run with system command lines, file icon clicks, imports and reloads, the exec built-in function, os module tools, and IDE GUI devices such as IDLE's Run->Run Module menu option.
    - Scripts that print and then exit cause the output file to disappear immediately, before you can view the output.
    - Python imports a module only once per process, by default, so if you've changed its source code and want to run the new version without stopping and restarting Python, you'll have to reload it.
    - Each module file is automatically a namespace--that is, a package of variables reflecting the assignments made at the top level of the file.
    - Each module's variables becomes an attribute of the module when it's imported and are accessed by "." qualification or from name copies.
    - Namespaces help avoid name collisions in Python programs: because each module file is a self-contained namespace, files must explicitly import other files in order to use their names.