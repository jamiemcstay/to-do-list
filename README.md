![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# To Do List Application

## A Python command line tool
>This application is a Python command line To Do List manager. Users can add, view, remove, and mark tasks as complete through an intuitive command line interface.

## Table of Contents
 1. [ Pre-Project Planning ](#pre-project-planning)  
 2. [ Features Left to Implement ](#features-left-to-implement)  
 3. [ Technology used ](#technology-used) 
 4. [ Testing ](#testing)  
 5. [ Bugs ](#bugs)  
 6. [ Deployment](#deployment)
 7. [ Credits](#credits)
 8. [ Content](#content)  
 9. [ Acknowledgements](#acknowledgements)

<a name="pre-project-planning"></a>
### Pre-Project Planning

> For this project,  I aimed to create a simple command line To Do List application in Python. The Goal was to build a tool that helps users manage their tasks through a straightforward interface.

I mapped out the applications flow in a diagram to understand the user interactions and task management logic required. This helped in structuring the project and identifying key features and functionalities. Please see below for flow diagram. 

![Figjam Flow Diagram](assets/images/to-do-list-flow-chart.png)

### Application Structure

#### Task Management

- **Add Tasks**: Allows users to add new tasks with the description and due date.
- **View Tasks**: Displays a list of all tasks wit their status.
- **Remove Tasks**: Enable users to remove tasks from the list.
- **Mark Tasks Complete**: Marks tasks as complete and updates their status.

#### Data Management

- **JSON STORAGE**: Tasks are saved in a `tasks.json` file for persistence.
- **Data Validation**: Ensures that data entered by the user is correctly formatted.

#### User Interaction

- **Command Line Interface**: The user interacts with the application via a command line menu with options to manage tasks. 

## Program Flow
> When the user starts the application, they are greeted with a menu:

**Main Menu**: 
![Main Menu](assets/images/main-menu.png)

> The user can choose to view tasks, add new tasks, remove tasks, or mark tasks as complete.

**Add Tasks**: 
![Add a task](assets/images/add-tasks.png)
> A user is prompted to enter a task description, due date, and priority level.

**View Tasks**:
![View Tasks](assets/images/view-tasks.png)
> A user can view their list of tasks. 

**Remove Tasks**:
![Remove Tasks](assets/images/remove-tasks.png)
> A user can see a list of tasks and choose a task number to remove from their task list. 

**Mark Tasks Complete**:
![Mark Tasks Complete](assets/images/mark-tasks-complete.png)
> A user can see their list of tasks and choose a task number to mark as complete. 

**Press m to return to main menu**:
![Press m to return to menu](assets/images/mark-tasks-complete.png)
> When in any function in the program, the user has the option to return to the main menu by keying 'm' and pressing enter.

<a name="features-left-to-implement"></a>
### Features Left to Implement

- **Task Editing**: Implement functinality to edit existing tasks.
- **Task Sorting**: Add options to sort tasks by due date or priority. 
- **Search Funcionality**: Allow users to search for tasks by keywords or status.
- **Advanced Filtering**: Provide filters to view tasks based on specific criteria. 

<a name="technology-used"></a>
### Technology Used

- **Python**: The programming language used to build the application.
- **JSON**: File format used for data storage and retrieval.
- **Figma**: Used for editing images. 
- **Gitpod**: IDE used to develop program. 
- **Github**: Used to build repository. 

<a name="testing"></a>
### Testing

The following tests were undertaken by me and 2 housemates. 

#### Manual Testing

| Test | Result |
|--|--|
| Program starts and displays the main menu | Pass |
| User can add a new task and see it in the the list | Pass |
| A user can remove a task and see it disappear from the list | Pass |
| A user can mark a task as complete and see its status updated | Pass |
| User can view the tasks and see their current status | Pass |

#### Error Handling

| Test | Expected Result | Actual Result | Pass/Fail |
|--|--|--|--|
| Adding a task with an invalid date format | Error message displayed | Error message displayed | Pass |
| Adding a task with an invalid priority entry | Error message displayed | Error message displayed |  Pass |
| Removing a task that doesn't exist | Error message displayed | Error message displayed | Pass |
| Entering non integers into remove task | Error message displayed | Error message displayed | Pass |
| Entering non integers into remove task | Error message displayed | Error message displayed | Pass |
| Entering no integers into mark tasks complete input | Error message displayed | Error message displayed | Pass |
| Entering no integers into mark tasks complete input | Error message displayed | Error message displayed | Pass |
| Entering no existant task number into mark tasks complete input | Error message displayed | Error message displayed | Pass |
| Entering an task number for task already complete into  mark tasks complete input | Error message displayed | Error message displayed | Pass |

<a name="bugs"></a>
### Identified Bugs

| Issue | Action | Result |
|--|--|--|--|
| Heading reprinting in terminal view as OS method in clear screen function not working in deployment | Use xzy instead | Fixed |
| Extra space added by using backslash (/) in long statements | Seperated long print statements intom seperate print statements | Fixed |

<a name="deployment"></a>
##  Deployment

I set up an account on Heroku.

I went to the create new app button.

Named the app with a unique name.

Selected my region.

Clicked create app. 

I clicked on the settings tab.

I clicked on Add Buildpack and picked Python and Node.Js (in that order)

I clicked on the deploy section.

I clicked on Github and confirmed I wanted to connect to github. 

I then searched for my repository name and named it to-do-list.

I then clicked connect. 

I then enabled automatic deploys.

The app was successfully deployed.

Clicked view app to view the mock terminal. 

<a name="credits"><\a>
## Credits

I used multiple resources to understand the best way to build this program in Python. 

### [Programming with Mosh](https://www.youtube.com/watch?v=9OeznAkyQz4&ab_channel=ProgrammingwithMosh)
-  Helped to understand working with lists. 

### [Python OS Module](https://www.w3schools.com/python/module_os.asp)
- Helped with understanding working with the OS module.

### [How to use JSON in Python](https://www.youtube.com/watch?v=-51jxlQaxyA&ab_channel=TechWithTim)
- Helped to understand Python. 

<a name="content"></a>
## Content and Resources









