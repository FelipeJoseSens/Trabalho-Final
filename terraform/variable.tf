# terraform/variables.tf

variable "aws_region" {
  description = "Região da AWS para criar os recursos"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tipo da instância EC2"
  type        = string
  default     = "t2.micro" # Compatível com o nível gratuito da AWS
}

variable "ssh_key_name" {
  description = "Nome do par de chaves SSH a ser criado na AWS"
  type        = string
  default     = "trabalho-final-key"
}