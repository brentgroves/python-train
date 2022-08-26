#!/bin/bash
# python debug1.py
# ./debug2.sh
pipeline="TrialBalance"
export em=""
export emline=""
export dm=""
export line=""
export tm=""
export result=0

export pcn=""
export pcn_list="123681,300758"

export username=$(</etc/foo/username)
export password=$(</etc/foo/password)
export username2=$(</etc/foo/username2)
export password2=$(</etc/foo/password2)
export username3=$(</etc/foo/username3)
export password3=$(</etc/foo/password3)
export username4=$(</etc/foo/username4)
export password4=$(</etc/foo/password4)

# export em="none"
# export emline="none"
# export dm="none"
# export line="none"
# export tm="none"
# export result=0 

# printf "TrialBalance path= $PATH." | mail -s "Trial Balance Path" bgroves@buschegroup.com

# Development directory
cd reporting/restapi/pipeline


# reset variables
em=""
emline=""
dm=""
line=""
tm=""

# set pcn
pcn=123681

if [[ $result -eq 0 ]]
then # if/then branch
  script="AccountActivitySummaryGetOpenPeriodRange"
  cd ../AccountActivitySummaryGetOpenPeriodRange
  source AccountActivitySummaryGetOpenPeriodRange.sh 
fi

# reset variables
em=""
emline=""
dm=""
line=""
tm=""

# set pcn
pcn=300758

if [[ $result -eq 0 ]]
then # if/then branch
  script="AccountActivitySummaryGetOpenPeriodRange"
  cd ../AccountActivitySummaryGetOpenPeriodRange
  source AccountActivitySummaryGetOpenPeriodRange.sh 
fi


# reset variables
em=""
emline=""
dm=""
line=""
tm=""

# set pcn
pcn=123681

if [[ $result -eq 0 ]]
then # if/then branch
  script="AccountPeriodBalanceRecreateOpenPeriodRange"
  cd ../AccountPeriodBalanceRecreateOpenPeriodRange
  source AccountPeriodBalanceRecreateOpenPeriodRange.sh 
fi

# reset variables
em=""
emline=""
dm=""
line=""
tm=""

# set pcn
pcn=300758

if [[ $result -eq 0 ]]
then # if/then branch
  script="AccountPeriodBalanceRecreateOpenPeriodRange"
  cd ../AccountPeriodBalanceRecreateOpenPeriodRange
  source AccountPeriodBalanceRecreateOpenPeriodRange.sh 
fi

if [[ $result -ne 0 ]]
then # if/then branch
  printf "Pipeline terminated at $script\n"
  printf "Pipeline terminated on $script script." | mail -s "MCP Pipeline Failure" bgroves@buschegroup.com
else
  printf "Pipeline successfully terminated." | mail -s "MCP Pipeline Failure" bgroves@buschegroup.com
fi
