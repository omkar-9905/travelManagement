variable "bucket_name" {
  type = string
  description = "The name of our bucket"
}

variable "bucket_location" {
  type = string
  default = "us-central1"
}

variable "project_id" {
  type = string 
}

variable "storage_class" {
  type = string
}

variable "zone"{
    type = string
    default = "us-central1-a"
}

variable "google_compute_instance" {
    type = string
    description = "projectprovision" 
}

variable "google_compute_instance_name" {
    type = string
    description = "projectprovision" 
}


variable "google_compute_instance_location" {
    type = string
    description = "google compute engine location" 
  
}

variable "image"{
    type = string
    description = "image name"
}
#name = "testprovision0810"
variable "network" {
    type = string
    description = "network name"
    default = "default"
  
}