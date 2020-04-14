#!/usr/bin/env bash
OUTPUT_PATH="/newsgroup_output"
TRAIN_PATH="/input_newsgroup/train" # previously named 'out'
TEST_PATH="/input_newsgroup/test"
DATASET="20newsgroup"
MIN_RANGE=0
MAX_RANGE=100

for split in "train"; do
    for epsilon_value in "1.2" "1.4" "1.6" "1.8" "2.0" "2.1" "2.2" "2.4" "2.5" "2.6" "2.8" "3.0"; do
        output_hdfs="${OUTPUT_PATH}_${epsilon_value}_${split}"
        if [[ "$split" = "train" ]]; then
            input_hdfs="$TRAIN_PATH"
        else
            input_hdfs="$TEST_PATH"
        fi
	HADOOP_CLASSPATH="$HADOOP_CLASSPATH:/opt/MyJarTests/commons-math3-3.6.1.jar" echo hadoop jar /opt/MyJarTests/newsgroupParma.jar parmanix.MapReduceEntrypoin
t "$input_hdfs" "$output_hdfs" "$DATASET" parmanix.NewsgroupWordCountMapper count "$epsilon_value" 1 "$MIN_RANGE" "$MAX_RANGE" 10000 15 100
    done
done

