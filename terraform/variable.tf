#provider
variable "region"{
    default = "us-east-1"
}

variable "account"{
    default = "000000000000"
}

variable "bucket" {
    default = "test"
}


#lambda
variable "function"{
    default = "processKinesisRecords"
}
variable "run_time" {
    default = "python3.6"
}

variable "file" {
    default = "function.zip"
}

variable "handler" {
    default = "ProcessKinesisRecords.lambda_handler"
}


