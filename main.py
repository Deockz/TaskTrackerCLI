import sys
import json
import os.path

def createJSON ():
    list_json_template = {'tasks':{'Done':{},'Todo':{},'Inprg':{}}}
    with open('list.json', 'w') as outfile:
        json.dump(list_json_template, outfile)

def add():
    print('add')
    

def update():
    print('Update')

def delete():
    print('Delete')

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
    globals()[sys.argv[1]]()
    

