# Task 1
_names wrapped by "$" sign should be replaced_
## PyCharm:

1. Open PyCharm
2. On the "Welcome to PyCharm" window click "Checkout from Version Control"
3. Select Git
4. Enter "https://github.com/3Pi0FomTatuin/Task1.git" into URL input
5. Choose Directory
6. Click "Yes" in a opened prompt
7. Go to File -> Settings -> Project: $PROJECT_NAME$ -> Project Interpreter
8. Click on the cogwheel (settings button)
9. Click "Add"
10. Configure virtual environment and click "OK"; "Apply"
11. Exit settings window
12. Wait for skeleton building tasks
13. In the "Project" tool window (by default located on the left of the screen) right click on init/init.py and select " 'Run init' "
14.
	
## From Terminal:

1. Go to root of the project (e.g. $PROJECT_FOLDER_ROOT$="D:\\") 
	* Unix
	
		`cd $PROJECT_FOLDER_ROOT$`
	* Windows
	
		`cd /d $PROJECT_FOLDER_ROOT$`

2. Clone the project from GitHub

	`git clone https://github.com/3Pi0FomTatuin/Task1.git`

3. Go to the project directory

	`cd Task1`
		
4. Create virtual environment
	(for additional information visit [Creation of virtual environments](https://docs.python.org/3/library/venv.html)) 
	* Unix
		
		`python3 -m venv venv/`
	* Windows
	
		Determine your python 3 path (e.g. $PYTHON_PATH$=D:\\Programs\\Python36\\python.exe)
		
		`where python`
		
		and run
		
		`$PYTHON_PATH$ -m venv venv/`
		
5. Start work on virtual environment
	* Unix
		
		`source venv/bin/activate`
	* Windows

		`venv\Scripts\activate.bat`
	
6. * Run initialization script with "nopycharm" argument
		
		`python init/init.py nopycharm`
	* or set Pycharm to False in the _init/init.py_ and run
		
		`python init/init.py`
		
7. Run server
	
	`python manage.py runserver`