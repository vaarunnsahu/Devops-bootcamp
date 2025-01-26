# ecs task definition -> will use 1 template.
#  ecs cluser
# ecs service -> will map this to load balancer 


# ecs cluster
resource "aws_ecs_cluster" "main" {
  name = "${var.environment}-${var.app_name}-cluster"
}

# ebuilding template
data "template_file" "services" {
  template = file(var.flask_app_template_file)
  vars     = local.flask_ecs_services_vars
}

# ecs task definition
resource "aws_ecs_task_definition" "services" {
  family                   = "${var.environment}-${var.app_name}"
  network_mode             = "awsvpc"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  cpu                      = var.flask_app_cpu
  memory                   = var.flask_app_memory
  requires_compatibilities = ["FARGATE"]
  container_definitions    = data.template_file.services.rendered

  tags = {
    Environment = var.environment
    Application = var.app_name
  }
}