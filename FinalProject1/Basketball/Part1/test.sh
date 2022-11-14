#!/bin/bash

# start all clusters

start-all.sh

# clear hdfs directory

hadoop fs -rm -r /task1

# turn off safe mode

hadoop dfsadmin -safemode leave

# copy input data to hdfs directory

hadoop fs -mkdir /task1

hadoop fs -put ./shot_logs.csv /task1

# hadoop streaming

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
        -file ../../FinalProject1/Basketball/Part1/mapper.py -mapper ../../FinalProject1/Basketball/Part1/mapper.py \
        -file ../../FinalProject1/Basketball/Part1/reducer.py -reducer ../../FinalProject1/Basketball/Part1/reducer.py \
        -input /task1/shot_logs.csv \
        -output /task1/output


# access the output

hadoop fs -cat /task1/output/part-00000

# clean the file system

hadoop fs -rm -r /task1

# shut down all clusters

stop-all.sh