#!/bin/bash

zip function.zip ProcessKinesisRecords.py
sleep 0.5
aws lambda update-function-code --function-name processKinesisRecords --zip-file fileb://function.zip --endpoint-url=http://localhost:4566
