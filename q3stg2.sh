#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file mapgramq3_stg2.py reducegramq3_stg2.py -mapper mapgramq3_stg2.py -reducer reducegramq3_stg2.py
