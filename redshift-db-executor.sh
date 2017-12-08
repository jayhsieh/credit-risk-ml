#
# this script executes the first command line argument 
# (usually a .sql script in this directory)
#
# the sed statement at the end is to replace the spaces and pipe output from 
# redshift with commas. this logic is mac osx specific
#
# the password magic is using the mac keychain. usage described here:
# https://wiki.remitly.com/display/DEV/Neil%27s+Cheatsheet
#
# -displayResult param is so that the query actually displays to standard out
# 
# -feedback param is to eliminate noisy info from the command program
#
# example use is (from blended directory) 
# . ./redshift-db-executor.sh extract_market_rates.sql
#
java -jar /usr/local/sql/java/sqlworkbench.jar -url=jdbc:postgresql://dw.remitly.internal:5439/dev -driver=org.postgresql.Driver -username=mikef -password=$(get-redshift-pw) -driverJar=/users/mikefoster/postgres-java/postgresql-9.4.1211.jre6.jar -displayResult=true -feedback=false -script=$1 | sed 's/[[:space:]]*|[[:space:]]*/,/g' 
