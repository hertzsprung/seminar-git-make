intro
=====
AUDIENCE:
- hands up who's broken code and not known why
- hands up who has to collaborate on projects with other people
- hands up who gets paranoid that all their graphs are up-to-date when including them in a report

- make: a build automation tool
- git: a revision control system

make
====
concepts
--------
WRITE ON BOARD:
- rule
- target
- prerequisite
- commands

demonstration
-------------
We are starting a project about the weather at Heathrow.
So far we have three things:
- a data file
- a python source file that creates a plot of the data
- a LaTeX report

We must ensure that any changes are reflected in the final PDF report.

	cd make-demo
	ls
	vi Makefile -- identify a rule, target, prerequisite, command
	make report.pdf
	o report.pdf -- TADA!
	make report.pdf -- doesn't do anything -- make is smart!
	vi heathrow-sun.dat and make a change
	make report.pdf -- redraws graph and recompiles PDF report -- make is smart!

git
===
concepts
--------
WRITE ON BOARD:
- repository
- commit

demonstration
-------------
	mkdir myproject
	cd myproject
	git init
	vi my_report.txt (write a couple of lines of text)
	git status
	git add my_report.txt
	git status
	git commit -m "initial revision of my report"
	git status
	git log
	vi my_report.txt (modify a line, add a line, delete a line)
	git status
	git add my_report.txt
	git commit -m "a modification to my report"
	git log
	git diff --word-diff (copy commit hashes)
	git checkout <hash> -- my_report.txt
	git status
	git diff --staged
	git commit -m "rollback change to report"
	git log

distribution with github
------------------------
- lets you collaborate on a project with many people at once
- example: alice and bob are collaborating on an article about fog

	- move to BLUE "alice" tab
	(with a repo that's already set up)
	vi fog.txt
	- AUDIENCE: suggest another type of fog (e.g. advection fog)
	git commit -m "add another type of fog"
	git push
	- view on github: commit tab, view file contents
	- move to GREEN "bob" tab
	vi fog.txt -- file is out of date, doesn't include alice's latest change!
	git pull
	vi fog.txt -- file is now up to date!


WRAP-UP
=======
We've seen:
- how to ensure your report includes up-to-date graphs and data
- how to keep a complete history of your work
- how to collaborate on a project using GitHub
