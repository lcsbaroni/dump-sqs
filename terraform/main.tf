module "user_queue" {
  source  = "terraform-aws-modules/sqs/aws"
  version = "~> 2.0"

  name = var.queue_name

  tags = {
    Service     = "user"
    Environment = "dev"
  }
}