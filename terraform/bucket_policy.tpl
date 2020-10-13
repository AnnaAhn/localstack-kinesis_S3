{
    "Version": "2012-10-17",
    "Id": "MYBUCKETPOLICY",
    "Statement": [
        {
        "Sid": "LambdaAllow",
        "Effect": "ALLOW",
        "Principal": "${lambda_arn}",
        "Action": "s3:*",
        "Resource": "aws_s3_bucket.test.arn/*"
        }
    ]
}
