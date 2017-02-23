# Pair-Programming Exercise #1

Objective: Create a git repository, add files, edit files and commit changes. Repeat. Push to your github repo.

Open the Terminal

`git init`

See what's in the repository

`git status`

Create a file and add some text

`nano HelloWorld.txt`

Add the file to the repo

`git add HelloWorld.txt`

Commit the file to the repo

`git commit -m "My first commit."`

Edit the file and write down one thing you like about data.

`nano HelloWorld.txt`

Add to git and commit changes.

`git add HelloWorld.txt`

Check the status of the repo:

`git status`

Commit the file:

`git commit -m "Commenting why data is important."`

Check the status again:

`git status`

Repeat this process 3-5 times until you get comfortable editing files and pushing them to the repo. Try adding new files and folders as well.

Add your repo to git.

Goto github.com and click the + button to add a new repo. Copy the url of the repo to your clipboard

More details at: https://help.github.com/articles/adding-a-remote/

`git remote add origin {repo_url}`

`git pull origin master`

Now add the files from your current directory and push them to repo on github.

`git add .
git commit -m "Adding all local files"
git push origin master`
