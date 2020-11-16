#!/usr/bin/bash
# This is a simple shell script that makes my git commits every day

commit="$(date +'%b %d %Y')"

if [[ $( python3 index.py ) =~ "> System engaged ..." ]];then
  git add .
  git commit -m "$commit"
  git push -u origin master
  echo "200 OK"
else
  echo "FAILD"
fi
