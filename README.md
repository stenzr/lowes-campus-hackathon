## store-navigation


###### approach :
        Developed a RESTful api in Flask-RESTful to provide endpoints for the below 3 frontend tasks for an android application for the user to enter the product name/product list.
        Through which the user can perform the following tasks:
        
        1. Search for the location details of the product.
        2. Provide the list of products to get the respective aisle numbers.
        3. Get an optimal path for the shopping trip for the list of products.

        Developed 

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

`git clone https://github.com/stenzr/store-navigation.git`

###### press enter


##### cd to this project directory

`cd store-navigation`

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












