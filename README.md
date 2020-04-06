# agileManage
The goal is to automate the process completed after sprint planning. This involves dependency limitations, capacity allocation, and task ordering. I usually do this by hand, and an example can be found on DI2E Confluence. 

# Planning
## Objective
![Overview](pics/overview)

**Stage 2 = output of sprint goes into input of sprint retrospective to get metrics?
## Constraints
- Task transition cost – want a person working on a minimum number of tasks per sprint
- Task options (1 developer to 1 task)
- Good input – need to conduct a proper sprint planning meeting; garbage in, garbage out

## Components

### Meeting
- Input: Schedule meeting 
- Output: Developer capacity, task estimate, task decomposition, task dependencies, Need/External/Optional/High-priority (NEO-H) backup for each task, developer-task matching availability

### Automation
- Input: Meeting output
- Output: Solution for schedule: metrics (on capacity), task ordering, task allocation, minimizes cost, fits within constraints

### Schedule
- Input: Automation output
- Output: Prettified graph, easy export/import into management tools

## Diagram
![Diagram](pics/diagram)

## Algorithm Pseudo-Code
1. Get inputs 

- Meeting inputs: (Developer capacity, task estimate, task decomposition, task dependencies, Need/External/Optional/High-priority (NEO-H) backup for each task, developer-task matching availability)

- Algorithm control inputs

2. Determine capacity (developer/management split)

3. Assign required tasks to developers (tasks where only one person is optional to work on it)

4. Assign subsequent likely tasks (if developer is working on task ‘x’, they probably will also work on all tasks dependent on ‘x’)

5. Algorithm search for complete solution

- If no complete solution, loosen constraints (allow for marked, over

- Repeat until constraints are loosened too much. Return “recommendation: lengthen sprint or change sprint goal”

6. Outputs (Solution for schedule: metrics (on capacity), task ordering, task allocation, minimizes cost, fits within constraints)


## Algorithm Types
1. Random Search
2. (?) Approximation algorith/formal algorithm
3. Machine learning/gradient descent/objective function?

## Code Design 
- Algorithm [has] algorithm controls (IE: Fibonacci task estimate where 2 points is about 1 day)
- Team member -> developer/manager [has] tasks, capacity
- Tasks [has] Task estimate, parent tasks, child tasks, NEO-H tags, assigned developer, dependent on, is depended by 


## Targeted Coding Skills

1. Test Driven Development

2. Python Classes