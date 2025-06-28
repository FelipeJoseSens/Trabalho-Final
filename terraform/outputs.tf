# terraform/outputs.tf

output "instance_public_ip" {
  description = "Endereço IP público da instância EC2"
  value       = aws_instance.web_server.public_ip
}

output "ssh_command" {
  description = "Comando para conectar via SSH na instância"
  value       = "ssh -i ${local_file.ssh_key_file.filename} ubuntu@${aws_instance.web_server.public_ip}"
}