
output "lambda_arn" {
    value = aws_lambda_function.test_lambda.arn
}

output "S3_arn" {
    value = aws_s3_bucket.test.arn
}
