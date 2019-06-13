#!/bin/bash
REPO="$1";
echo -n  "Your present working directory is : "
pwd
echo "Are you sure you want to continue ? (y/n)"
read input
if [ "$input" = "y" ]
then
	mkdir $REPO
	cd $REPO
	git init
	cd ..
	python3 create.py $REPO
	cd $REPO
	git remote add origin https://github.com/User-Name/$REPO.git
	touch README.md
	git add --all
	git commit -m "First Commit"
	git push -u origin master
else
	exit 1
fi
