#!/bin/sh
echo "Project Directory" $1

if [ -d ~/klocwork_projects/$1 ]
then
   echo "klocwork local project directory exists"
   exit -1
fi

mkdir -p ~/klocwork_projects/$1

kwcheck create http://10.221.57.29:8080/$2 -pd ~/klocwork_projects/$1/kwlp -sd ~/klocwork_projects/$1/kwps

if [ $? == 0 ]
then
   echo  ~/klocwork_projects/$1
   echo "Klockwork local project created"
fi
