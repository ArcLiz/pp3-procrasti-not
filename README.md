# Procrasti-Not
## Introduction
Procrasti-Not is your friendly neighbourhood bot for your procrastination misfortunes.<br>As many of us struggle with keeping on track with the tasks we've set out for ourselves on a specific day, I decided to create a "friend" that helps decide the order the tasks will be completed and also offers incentive to do so.<br>

The app is developed in Python and presented in a web browser using the Code Institute Python Template which creates a mock terminal.<br><br>
![Multi-Mockup](docs/project_device_mockup.png)

[View the project here](url-to-project) - *Please note: To open any links in this document in a new browser tab, please press CTRL + Click.*

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [Strategy](#strategy)
      * [Site Goals](#Site-Goals)
      * [User Stories](#User-Stories)
    * [Scope](#scope)
    * [Structure](#structure)
      * [App Logic](#application-logic)
    * [Skeleton and Surface](#skeleton-and-surface)
      * [Text Layouts](#text-layouts)        
      * [Chromatics](#chromatics)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### Strategy
Procrasti-Not is intended to be a helpful tool for individuals struggling to keep on track with tasks set out for the day. <br>Many times, I find that the issue with procrastination stems from the inability to decide what to do, when. Procrasti-Not will help the user with this issue in a fun and engaging way, to hopefully allow the user to feel more time efficient throughout their day. 

#### User Stories
* As a user I want an app that makes managing my tasks efficiently easier
* As a user I want help with choosing which task to perform
* As a user I want the app to feel friendly, helpful and personalized
* As a user I want clear instructions about the app functions
* As a user I want to be able to see how many tasks remain
* As a user I want task completion to feel rewarding
* As a user I want to be able to view, edit, add and delete tasks

### Scope
In order for the tool to provide the user with the functionality and experience set out in the User Stories, I intend to write the information printed to the user in a "conversational" way, where the user is being guided, coached and cheered on by a friendly bot named Procrasti-Not. <br><br>    In addition to this, I plan to include the following features:
* A detailed "How it works" text that the user can choose to read
* An initial setup function that allows the user to enter multiple tasks at once
* A function that randomly choses a task for the user
* A function that, upon user confirmation, marks the current task as completed
* A completion tracker that informs the user how many tasks remain
* Functions that allows the user to view, edit, add and delete tasks

### Structure

#### Application Logic
Once the features of the app were identified, the next step was to plan the application logic.

This involved breaking down the app into 3 main tasks, as well as identifying the steps that the user would take to complete and navigate between each task, including mapping out any and all sub tasks that would be required. This step was crucial in understanding the flow of the app, and how each section would connect to the other. 

The flow of the app was originally sketched out using pen and paper, but I later used [draw.io](https://app.diagrams.net/) for a more visually presentable flow chart which you can see below.
![Logic Flow Chart](docs/flowchart.png)

In addition to the above, I found that the app worked smoother if an "escape option" was added in to every user input. The user can at any point of the app input a zero (0) to be brought back to the SETUP MENU.

### Skeleton and Surface
#### Text Layouts
Due to the nature of the project, in which the webpage layout and design is not a factor, I still wanted the application to look inviting. I therefore sketched the look of the main menus beforehand, simply by using [Notepad++](https://notepad-plus-plus.org/downloads/), in order for the information that the user gains at any one particular view to be easily interpreted.

I chose to make clear divides between menu headers, general information and user interaction options.

Below you'll find screenshots of the mockup layouts.
![Text Layouts](docs/textmockups.png)

#### Chromatics
During the development of the project, I realised that long white text blocks on black background makes it difficult to distinguish whether information is important or not. As such, I wanted to find a way to make promts and interactions stand out to increase usability. At project inception I was unaware of the fact that even terminal text can be colored, but I somehow stumbled upon a [forum post](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal) where this was discussed. 

![Chromatics](docs/chromatics.png)

The color scheme I chose for different levels of importance was loosely based on color psychology. Green was chosen for text that needs to "semi-stand out" to the user, as it is a calming and reassuring color that does not feel overly aggressive or attention-grabbing. Cyan, on the other hand, was chosen for text that needs to be of even higher importance, as it is a color that conveys professionalism, and a sense of importance. Finally, red was chosen for very important information, as it is a color that naturally draws attention and is commonly associated with warnings and danger.

## Features
Names, screenshots and descriptions of all the features.

## Future Enhancements
List of any features that should, could or might be implemented in the future.
* Ability to store user information (incl. task lists)
  * Description of Feature and reason for why it might be added

## Testing
Documentation of all tests that has been done on the project.
### Feature Testing
![Excel Sheet of Tests](link/to/image)

### Validator Testing
* Python Checker - The python code was evaluated u
  * Outcome ![View Image of Report](link/to/image)


### Notable Bugs
#### Reported - Solved
* Item 1
* Item 2
* Item 3

#### Reported - Not Solved
* Item 1
* Item 2
* Item 3

## Deployment

The project was deployed using Heroku. The steps to deploy are as follows:

*Heroku Deployment - Project Creation and Settings*<br>
1. Sign up or Log in to [Heroku](https://heroku.com/)
2. Once in your dashboard, select "New" and then "Create New App"
3. Give your project a name (must be unique), select your region and confirm "create app"<br>

You'll now be taken to the Heroku Deployment Tab. In order to use the Code Institute mock terminal template for your deployed project, you'll need to do the following:

4. Navigate to the "Settings" tab
5. Click "Reveal Config Vars" to add a configuration variable with Key: **PORT** and Value: **8000**
6. Click "Add Buildpack" and add the packs **Python** and **NodeJS**
    * *Note that the order of added buildpacks have meaning. In this case, Python should be the first (top) and NodeJS second (bottom)*

*Heroku Deployment - Deploying a Github Repository*<br>
1. Navigate to the "Deployment" tab
2. Select "GitHub - Connect" under Deployment method and follow the steps necessary to connect your GitHub account
3. Select your GitHub account from the droplist, enter your repository name and click search
4. Choose "Connect" at the correct repository to connect the repo to your Heroku app
5. Further down on the Deployment page, you'll find "Automatic deploys" and "Manual deploy"
    * For automatic, choose the branch you wish to deploy and click "Enable Automatic Deploys".<br> This allows Heroku to automatically rebuild your app when your Github repository is updated
    * For manual, choose the branch you wish to deploy and click "Deploy Branch"
6. Once Heroku is finished with the build process you will be notified with a "Your App Was Successfully Deployed" message and a link to the app

*Forking the GitHub Repository*<br>

If you wish to make a copy of the repository to your own GitHub account, you can do so by "Forking" it.<br>
This will give you a full working copy of the project, but ensures that no changes you make affect the original repository.
1. Navigate to the GitHub repository while logged into your account
2. In your top right, click the Fork button
3. Chose the name you want to give your version of the repository *(automatically filled in as the original project name)*
4. Click the green "Create fork" button

*Cloning the GitHub Repository*<br>

If you wish to download a local version of the repository to be worked on, you can do that too. That is referred to as "Cloning".<br>
The steps to cloning the repository are as follows:
1. Navigate to the GitHub repository while logged into your account
2. Click the <>Code dropdown button
3. Make sure that HTTPS is chosen, then copy the repository link to the clipboard<br>
*Git must be installed for the next steps to work*<br>
4. Open the IDE you're working in
5. Type "git clone (the url link you just copied)" into the terminal

The project will now be on your local machine to use or save. This can be a good way to back up versions of your own work too.

## Credits

### Utilised Libraries

- Built in - **os**
- Built in - **sys**
- Built in - **time**
- Built in - **random**

### Code
* Item 1
* Item 2
* Item 3

### Acknowledgements
Individuals worthy of special mention.
* Person 1 - For...
* Person 2 - For...