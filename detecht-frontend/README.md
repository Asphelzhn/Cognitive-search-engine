# Welcome to Detecht Frontend
Here we will be using Angular 8 to develop the frontend. 

### OBS
Everything that is going to be written in the terminal should be done inside the folder: \
`the-detecht-cognitive-search-engine/detecht-frontend/`


## Getting started

### Install and update NPM
To get started check if you have npm installed on your computer, in terminal write
`npm -v`.
The version should be at least 
`6.11.3`.
If you dont have NPM installed, go to npmjs.com and install it. \
If it is a older version, in terminal write
`npm install -g npm`.
If you get a error write instead
`sudo npm install -g npm`.

### Install (or update) angular cli
In terminal write
`npm install -g @angular/cli`.
If you get a error write instead
`sudo npm install -g @angular/cli`.

### Check all is done correctly
In terminal write 
`git status`,
the last row should be \
`nothing to commit, working tree clean` \
If you do not have a clean working tree, please go directly to your teamleader before continue! \
\
In terminal write
`ng v`,
the version should be at least: 
`Angular CLI: 8.3.5`.\
If your CLI version is not up to date, please go directly to your teamleader before continue!



## Code Standard

### Indentation style
All code shall be indented according to WebStorm standard. 

### Class names
Class names should be Capital CamelCased, example ClassName, the name should also be a substantive

### Variable names
Variable names should be camelCased and describe the class, example className

### Component names
The name should be a clear description of what the component does, this should be done by 1-2 words. \
If the component is a child to another component it should be grouped under the parent, see section "Create a child component to parent component".\
Small letters and word divided with "-" ex: `component-name`

### Service names
The name should be a clear description of what the service does, it shall not contain service since the name will be
`service-name.service.ts`
and therefore is already in the name. 

### Data Types
##### PLEASE group data types together in the same files.
Data types for uses in components shall be created in 
`data-types.ts`. \
Data types that is received over an api shall be declared in
`network-data-types.ts`
and shall not contain any functions
 


## Workflow
See notes on drive about workflow.
For different cli commands see further down 

### To serve the application 
Write in terminal
`ng serve`. 
Or press the green play button in the top right corner of WebStorm

#### To stop serve the application
In the terminal serving the application press Ctrl + C
Or press the red square up in the top right corner of WebStorm where the play-button were

### Create a component
Write in terminal
`ng generate component component-name`
#### Create a child component to parent component
Write in terminal
`ng generate component parent-name/child-name`

### Create a service
Write in terminal
`ng generate service service-name`



## To install a module / library / node package / etc. 
### Talk to your teamleader first
In terminal write 
`npm install module-name --save`.


## Any questions?
Talk to your teamleader, who will gladly help or get help from others! :)


# Production
#### For production to server see
https://stackoverflow.com/questions/57960260/angular-8-set-production-environment-for-api-base-url
