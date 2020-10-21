# Intro To MongoDB

## Commands

### Read / Insert / Find
`show collections` - Show all collections in current DB
`coll = db.myFirstMDB;` - Assign DB to variable
`coll.insert({first: 'john', last: 'lennon', dob: '09/10/1940'});` Insert Data
`coll.find()` - Find all documents in collection
`coll.find({gender: 'f'})` - Find
`coll.find({gender: 'f', nationality: 'english'})` - Find AND
`coll.find({gender:"f", $or: [{nationality:"american"}, {nationality:"irish"}]});` - Find OR
`coll.find({gender: 'f', $or: [{nationality: 'american'}, {nationality: 'irish'}]}).sort({nationality: 1});` Find OR with sort (number in sort is sort mode)

### Update / Delete
`coll.update({nationality: 'irish'}, {$set: {hair_colour: 'blue'}})` - Updates the first positive document with new Data
`coll.update({nationality: 'irish'}, {$set: {hair_colour: 'purple'}},{multi:true})` - Updates all positive documents with new Data

`coll.remove({first: 'kate', last: 'bush'})` - Delete records

## Linking to Pyhton

Required
`pip3 install dnspython`
`pip3 install pymongo`

On Atlas MongoDB select Clusters>Connect>Connect_Your_Application> Select Python and Version then copy the "Mongo URI" (srv string). NEVER PUBLISH THIS TO GITHUB
NEVER PUBLISH TO GITHUB - Usernames, Passwords, SecretKeys, APIs

This information is hidden in an env.py file.

1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
2. If you don't have one already, create a file named .gitignore  in the root directory of your project.
3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text to it: env.py and __pychache__/ 
4. At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” underneath you can assign your environment variables using the following syntax: 
os.environ["Variable Name Here"] = "Value of Variable Goes Here" 
Example: os.environ["SECRET_KEY"] = "ohsosecret"
5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project or settings.py file for Django project. Add this under your other imports at the top of the file. 
from os import path
if path.exists("env.py"):
  import env 
The if statement here is so that the env.py file is only pulled when working on your code in your workspace, not when it is deployed on heroku. For deployment you can set your environment variables in the heroku dashboard in settings > config vars.
6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed using the following syntax: 
SECRET_KEY = os.environ.get('SECRET_KEY') 
Make sure you save all your files before testing if it works.

