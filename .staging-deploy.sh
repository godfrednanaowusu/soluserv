#!/bin/bash
#Get servers list
set -f
string=$STAGING_SERVER
array=(${string//,/ })
#Iterate servers for deploy and pull last commit
for i in "${!array[@]}";
do    
    echo "Staging Deployment Started on server ${array[i]}"   
    ssh -T git@gitlab.com
    #git clone -b development git@gitlab.com:soluserv/soluserv.git soluserv # run this in /var/www/
    ssh -o StrictHostKeyChecking=no ubuntu@${array[i]} "sudo mkdir -p /var/www/soluserv && sudo chmod -R 777 /var/www/soluserv && cd /var/www/soluserv && git stash && git pull && source /var/www/soluserv/soluservenv/bin/activate && pip install -r /var/www/soluserv/requirements.txt && python manage.py migrate && sudo systemctl restart nginx && sudo systemctl restart gunicorn"
    echo "Staging Deployment Completed"  
done

