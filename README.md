# Task 1
_names wrapped by "<>" should be replaced by you in way it needs_
## PyCharm:

1. Open PyCharm
2. On the "Welcome to PyCharm" window click "Checkout from Version Control"
3. Select Git
4. Enter "https://github.com/3Pi0FomTatuin/Task1.git" into URL input
5. Choose Directory
6. Click "Yes" in a opened prompt
7. On the main menu, choose File | Settings | Project: <project name> | Project Interpreter
8. Click on the cogwheel (settings button)
9. Click "Add"
10. Configure virtual environment and click "OK"; "Apply"
11. Exit settings window
12. Wait for skeleton building tasks
13. In the "Project" tool window (by default located on the left of the screen) right click on init/init.py and select " 'Run init' "
14. On the main menu, choose Tools | Run manage.py task. The manage.py utility starts in its own console.
15. Type `runserver`
	
## From Terminal:

1. Go to root of the project (e.g. \<project folder root>="D:\\") 
	* Unix
	
		`cd <project folder root>`
	* Windows
	
		`cd /d <project folder root>`

2. Clone the project from GitHub

	`git clone https://github.com/3Pi0FomTatuin/Task1.git`

3. Go to the project directory

	`cd Task1`
		
4. Create virtual environment
	(for additional information visit [Creation of virtual environments](https://docs.python.org/3/library/venv.html)) 
	* Unix
		
		`python3 -m venv venv/`
	* Windows
	
		Determine your python 3 path (e.g. \<python path>=D:\\Programs\\Python36\\python.exe)
		
		`where python`
		
		and run
		
		`<python path> -m venv venv/`
		
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