#!/bin/bash

# start all clusters

start-all.sh

# clear hdfs directory

hadoop fs -rm -r /task1

# turn off safe mode

hadoop dfsadmin -safemode leave

# copy input data to hdfs directory

hadoop fs -mkdir /task1

hadoop fs -put ./Parking_Violations_Issued_-_Fiscal_Year_2023.csv /task1

# hadoop streaming

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
        -file ../../FinalProject1/Parking/mapper.py -mapper ../../FinalProject1/Parking/mapper.py \
        -file ../../FinalProject1/Parking/reducer.py -reducer ../../FinalProject1/Parking/reducer.py \
        -input /task1/Parking_Violations_Issued_-_Fiscal_Year_2023.csv \
        -output /task1/output


# access the output

hadoop fs -cat /task1/output/part-00000

# clean the file system

hadoop fs -rm -r /task1

# shut down all clusters

stop-all.sh