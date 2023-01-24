'''''
1. step you need to install git 
2. go to the terminal and write
  $git --version
if you have git 2... ans something go to third step
3.Now let Git know who you are. This is important for version control systems, as each Git commit uses this information:

 $git config --global user.name "w3schools-test"
 $git config --global user.email "test@w3schools.com"

Change the user name and e-mail address to your own. You will probably also want to use this when registering to GitHub later on.

4.Creating Git Folder

  $mkdir myproject
  $cd myproject

mkdir makes a new directory.
cd changes the current working directory


5.Initialize Git
Once you have navigated to the correct folder, you can initialize Git on that folder:

  $git init 
 Initialized empty Git repository in /Users/user/myproject/.git/


6.yout need to create fileto initialized git folder and add it
  $git add file name 

7.Git Commit
Adding commits keep track of our progress and changes as we work. Git considers each commit change point or "save point". It is a point in the project you can go back to if you find a bug, or want to make a change.

When we commit, we should always include a message.

 $git commit -m "Some your changes description

And check the status of our repository. But this time, we will use the --short option to see the changes in a more compact way:

  $git status
Note: Short status flags are:

?? - Untracked files
A - Files added to stage
M - Modified files
D - Deleted files

8.Git Branch
In Git, a branch is a new/separate version of the main repository.

Let's say you have a large project, and you need to update the design on it.

Branches allow you to work on different parts of a project without impacting the main branch.

When the work is complete, a branch can be merged with the main project.

You can even switch between branches and work on different projects without them interfering with each other.

Branching in Git is very lightweight and fast!

-
New Git Branch
-

$git branch branch name

-
Let's confirm that we have created a new branch:
-
$git branch
  hello-world-images
* master


Switch branch
  $git checkout hello-world-images
  $Switched to branch 'hello-world-images'
  
9.And Finally after commit your should to push the commit to remote repository
1.Create account on Github
2.Create repository and add project folder
3.copy your https lik 
4.Open the terminal and go to your project folder
5.and write $git remote add origin yout link
6.Now we are going to push our master branch to the origin url, and set it as the default remote branch
 $git push --set-upstream origin master

'''