resource "aws_kinesis_stream" "test_stream" {
  name        = "KinesisTest"
  shard_count = 1
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = templatefile("lambda_role.tpl", { region=var.region, account = var.account, function = var.function})
}

resource "aws_lambda_function" "test_lambda" {
  filename         = var.file
  function_name    = var.function
  role             = aws_iam_role.iam_for_lambda.arn
  handler          = var.handler
  source_code_hash = filebase64sha256(var.file)
  runtime          = var.run_time
}

resource "aws_s3_bucket" "test" {
  bucket = var.bucket 
}

resource "aws_s3_bucket_policy" "test" {
  bucket = aws_s3_bucket.test.id

  policy = templatefile("bucket_policy.tpl", { region=var.region, account = var.account, function = var.function, lambda_arn = aws_lambda_function.test_lambda.arn})
}
