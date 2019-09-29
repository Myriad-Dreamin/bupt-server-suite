#!/usr/bin/env bash

read -p "input name: " name
read -p "input email: " email
# read -p "input password: " -s password

# echo $name $email $password
git config --global user.name $name
git config --global user.email $email
# git config --global user.pass
