{
  "Version": "2012-10-17",
    "Statement": [
        {
              "Effect": "Allow",
              "Action": "sts:AssumeRole"
        },
        {
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": [
                "arn:aws:logs:${region}:${account}:log-group:/aws/lambda/processKinesisRecords"
            ],
            "Effect": "Allow"
        }
   ]
}
