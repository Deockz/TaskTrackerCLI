##Task Tracker CLI

#About
Task Tracker CLI is a programm that help to keep tracking of your task and the status of these.
To use it you have 5 functions described below:

Add
'''bash
python main.py add 'Description og the task
'''
With this function a new taks will be created. Task ID, created time and updated time will be populated automaclly.
The status of a new task always will be 'todo'

Update. 
Sintax: python main.py update 'TaskID' 'New Description'
USe this fuction to change the description of a task. The Updated At property will be change.
(If you need the TaskID please go to 'List' fuction)

Delete. 
Sintax: python main.py update 'TaskID'
Function use to delete tasks

Status.
Sintax: python main.py status 'NewStatus' 'TaskID'
Fuction to change the status of the tasks. The status available are: Todo, Done and INPRG (In Progress). The Updated At property will be change.

List.
Sintax: python main.py list         or         python main.py list 'Status'
Fuction that show all the tasks stored in JSON file. An argument can be added to specify the tasks filtered by status.


Project from:
https://roadmap.sh/projects/task-tracker

