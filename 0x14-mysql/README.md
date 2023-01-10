**Installing mysql on both servers**

* task-0 in this directory installs a specific version of mysql

* task-1 steps:
- run the script with : cat mysql | sudo mysql -hlocalhost -uroot -p
- when it prompts for password, password is: root
- note "mysql" is the name of the file. Name can vary/differ from yours(task-1)
* to check if successful, run: mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"  with "projectcorrection280hbtn" as password

* For task-2 and 3, I entered the commands manually
