resource "aws_instance" "frontend" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 (cambia según región)
  instance_type = "t2.micro"

  tags = {
    Name = "frontend"
  }
}
