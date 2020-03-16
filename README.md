## lowes-campus-challenge-project

### team name: __ROhAR__ 
#### team members: 1. Rohit Kumar  2. Harsh Agrawal

#### Problem statement attempted: Number 3
###### statement :
        `Build a solution to help the` `customers find products in the` `store and help them navigate to the` `corresponding aisle/shelf. If there` `is a shopping list, provide the `best` `shopping trip to complete `the` purchases`

###### approach :
        Developed an android application frontend for the user to enter the product name/product list.
        Through which the user can perform the following tasks:
        
        1. Search for the location details of the product.
        2. Provide the list of products to get the respective aisle numbers.
        3. Get an optimal path for the shopping trip for the list of products.

        Developed a RESTful api in Flask-RESTful in backend to provide endpoints for the above 3 frontend tasks.

###### database:
        Web scraped the lowes site directory website to get the:
            1. Department Names
            2. Sub-Category names of the respective departments
            3. Products 

----

----
 
##### project directory:
            1. app.py // the flask application to create the backend server and provide API end-points
            2. lowesProductDatabase.db // the sqlite database used by the application. Created by web scraping Lowes site Directory website
            3. Android/   // the android application codebase
            4. requirements.txt // the python3 libraries required for the project
            5. Procfile  // for Heroku deployment of the API

---- 


----
### Build Details:

### to build the project on your system

###### cd to your project directory
`cd <dir path>`


##### open a terminal and type the following

`git clone https://github.com/stenzr/lowes-campus-hackathon.git`

###### press enter


##### cd to this project directory

`cd lowes-campus-hackathon`

###### press enter

-----

### For Starting the Backend Server

#### create a python virtual environment 

`sudo apt install python3-venv`

###### press enter

`enter your password`

###### enter your system user password


###### create the environment

`python3 -m venv venv1`

###### press enter


###### activate the environment

`source venv1/bin/activate`

###### press enter


###### install the required project python libraries

`pip3 install -r requirements.txt`

###### press enter


#### start the server

`python3 app.py`

###### press ctrl+c to stop the server

----

### Building the Android Application

install Android Studio in your system










