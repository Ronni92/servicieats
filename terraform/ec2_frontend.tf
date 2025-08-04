# 1. variables.tf
variable "aws_region" {
  description = "Región de AWS"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tipo de instancia EC2"
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI de Ubuntu 22.04 LTS"
  default     = "ami-053b0d53c279acc90"
}

variable "key_name" {
  description = "Nombre del par de claves SSH"
  default     = "mi_clave_ssh"
}

variable "frontend_security_group" {
  description = "Nombre del Security Group para el frontend"
  default     = "frontend-sg"
}
