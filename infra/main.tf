terraform {
  required_version = ">=1.0"

  backend "gcs" {
    bucket  = "novachok-infra-state"
    prefix  = "erp/terraform.tfstate"
  }

  required_providers {

  }
}

provider "google" {
  credentials = file("key.json")
  project     = "artinet-webserver"
  region      = "europe-central2"
}