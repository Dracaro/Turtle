# Open Forum


## Getting Started 🤩🤗:

- Fork this repo (button on top)
- Clone on your local machine

```
git clone https://github.com/Dracaro/Turtle.git

```
- Navigate to project directory.
```
cd Hacktoberfest2022
```

- Create a new Branch

```markdown
git checkout -b my-new-branch
```
- Add your contribution
```
git add .
```
- Commit your changes.

```markdown
git commit -m "Relevant message"
```
- Then push 
```
git push origin my-new-branch
```


- Create a new pull request from your forked repository

<br>

## Avoid Conflicts {Syncing your fork}

An easy way to avoid conflicts is to add an 'upstream' for your git repo, as other PR's may be merged while you're working on your branch/fork.   

```terminal
git remote add upstream https://github.com/dracaro/Turtle.git
```

You can verify that the new remote has been added by typing
```terminal
git remote -v
```

To pull any new changes from your parent repo simply run
```terminal
git merge upstream/master
```
