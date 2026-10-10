# Production infrastructure. Changes require change-advisory approval.
resource "aws_db_instance" "checkout" {
  identifier        = "checkout-prod"
  engine            = "postgres"
  instance_class    = "db.r6g.large"
  allocated_storage = 200
  password          = var.db_password
}

variable "db_password" {
  sensitive = true
}
