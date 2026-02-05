#!/bin/bash
#Get servers list
set -f
string=$PRODUCTION_SERVER
array=(${string//,/ })
#Iterate servers for deploy and pull last commit
for i in "${!array[@]}";
do    
    echo "Production Deployment Started on server ${array[i]}"   
    ssh -T git@gitlab.com
    #git clone -b master git@gitlab.com:growforme/growforme.git growforme # run this in /var/www/
    ssh -o StrictHostKeyChecking=no ubuntu@${array[i]} "sudo mkdir -p /var/soluserv && sudo chmod -R 777 /var/soluserv && cd /var/soluserv && git stash && git pull && pipenv install && python manage.py migrate && sudo systemctl restart nginx && sudo systemctl restart gunicorn && sudo systemctl restart redis.service && sudo systemctl restart supervisord.service && sudo systemctl restart supervisor"
    echo "Production Deployment Completed"  
done

