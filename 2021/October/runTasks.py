import sys

class Task:
    def __init__(self, taskId, priority, dependencies):
        self.id = taskId
        self.pr = priority
        self.dep = dependencies
        
    def __str__(self):
        return "({}, {}, {})".format(self.id, self.pr, self.dep)
        
# Complete the functions below.
tasks = []

def addTask(taskId, priority, dependencies):
    tasks.append(Task(taskId, priority, dependencies))

def runAllTasks():
    
    tasks.sort(key=lambda task: task.pr, reverse = True)
    
    for task in tasks:
        print(task)
    
    index = 0
    
    completed_tasks = {}
    
    while len(tasks) > 0:
        
        all_dependencies_satisfied = True
        
        if len(tasks[index].dep) > 0:
            
            for dependency in tasks[index].dep:
                if dependency not in completed_tasks:
                    all_dependencies_satisfied = False
            
        if len(tasks[index].dep) == 0 or all_dependencies_satisfied:
            runTask(tasks[index].id)
            completed_tasks[tasks[index].id] = True
            del tasks[index]
            index = -1
            
        index += 1
            

# You can ingore the stuff below this, it is just for reading in
# the problem

def runTask(taskId):
    print("Ran task: " + str(taskId))

'''
addTask(1, 5, [2])
addTask(2, 0, [])
runAllTasks()
'''
addTask(1, 5, [2])
addTask(2, 10, [])
addTask(3, 20, [1,2])
addTask(4, 0, [2])
addTask(5, 15, [2])
runAllTasks()