# 1. git is the version control tool that tracks changes locally github is the online platform where you host and share your git repositories

# 2. terminal is the application you open to type commands command line is the interface where you actually type them

# 3. local repo is the copy of your project on your computer remote repo is the version stored on github or another server

# 4. version control is a system that tracks changes to files lets you go back to previous versions and helps with collaboration

# 5. staging area is the place where you put changes before committing them

# 6. git add puts your changed files into the staging area ready to be committed

# 7. git commit saves the staged changes into the local repository with a message describing what you did

# 8. git push sends your commits from the local repository to the remote repository on github

# 9. git status shows which files are changed staged or untracked

# 10. git pull updates your local repository with the latest changes from the remote repository

# 11. pwd prints the path of the current directory you are in

# 12. ls lists all files and folders in the current directory

# 13. cd changes the current directory to another one

# 14. nano opens a simple text editor in the terminal

# 15. touch creates a new empty file

# 16. mv moves or renames files or directories

# 17. rm deletes files or directories

# 18. cat displays the contents of a file in the terminal



# --- #

# pwd

#ls

#cd ~/brianna_repo
#git pull

#mv homework.py ../judy_decal/homework/

#cd ../judy_decal/homework/

#cat homework.py

#git add *
#git commit -m "message"
#git push

#git pull
#git push
#this error occurred because judy tried to push to a repository that updated changes in between her changes resulting in a merge conflict

#cd ~/Recent/

def checkDataType(a):
    return str(type(a))

def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

def sumWithLoop(numbers):
    s = 0
    for n in numbers:
        s += n
    return s

def duplicateList(l):
    s = []
    for n in l:
        s.append(n)
        s.append(n)
    return s

def square(num): #added colon
    return num * num


result = duplicateList([6,7,420])
print(result)