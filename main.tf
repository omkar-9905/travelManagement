provider "google" {
  project = var.project_id
  region  = var.zone
}

resource "google_compute_instance" "default" {
  name = var.google_compute_instance
  machine_type = var.google_compute_instance
  zone         = var.google_compute_instance_location
  boot_disk {
    initialize_params {
      image = var.image
    }
  }
  network_interface {
    network = "default"
    access_config {
    }
  }
}
resource "google_storage_bucket" "default"{
  name = var.bucket_name
  storage_class = var.storage_class
  location = var.bucket_location
}
output "ip" {
  value = google_compute_instance.default.network_interface[0]
}
