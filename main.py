import sys
import json
import os.path
import datetime

def createJSON ():
    list_json_template = {'tasks':{},'task_count':0}
    with open('list.json', 'w') as outfile:
        json.dump(list_json_template, outfile)

def add():
    #Init new task with status todo, created and updated time
    time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    task_id = 0
    task_data = {
        "description" : "",
        "status" : "todo",
        "createdAt" :  time,
        "updatedAt" : time,
    }

    #Get the index for the new task
    try:
        with open('list.json', 'r') as file:
            data = json.load(file)
        task_id = data['task_count'] + 1
    except:
        print("Error in index. Please contact support")
    
    #Get de description from CIL arguments
    try:
        task_data['description'] = ' '.join(sys.argv[2:])
    except:
        print('Error.Description of task is required in arguments')
    
    #Update Json file
    data['tasks'] [f'{task_id}']= task_data
    data['task_count'] = task_id
    file.close()
    with open('list.json', 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()
    print("Successfully added the task")
    
def update():
    time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    try:
        with open('list.json', 'r') as file:
            data = json.load(file)
        task = data['tasks'][f'{sys.argv[2]}']
        if sys.argv[3:]:
            task['description'] = ' '.join(sys.argv[3:])
        else:
            print('There is not a descrption')
            task['description'] = 'None'
        task["updatedAt"] = time
        data['tasks'][f'{sys.argv[2]}'] = task
    except KeyError:
        print('Index error. Task do not exist')
    except: 
        print('Error retreiving data.')
    file.close()
    with open('list.json', 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()


def delete():
    try:
        with open('list.json', 'r') as file:
            data = json.load(file)
            data['tasks'].pop(f'{sys.argv[2]}')
        file.close()
        with open('list.json', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()
    except KeyError:
        print('Index error. Task do not exist')
    except: 
        print('Error retreiving data.')

def inprg():
    print('Inprg')

def done():
    print('Done')

def list():
    
    with open('list.json', 'r') as file:
        data = json.load(file)
    if len(sys.argv)<3:
        print(data['tasks'])
    else:
         consult = sys.argv[2].lower()
         print(data['tasks'][consult])
        
    
if __name__ == '__main__':
    if not os.path.exists('list.json'):
        createJSON()
    globals()[sys.argv[1].lower()]()
    

