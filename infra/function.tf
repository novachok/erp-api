resource "google_cloudfunctions_function" "function" {
  name                  = "api"
  description           = "ERP API function"
  runtime               = "python39"
  available_memory_mb   = 128
  source_archive_bucket = "novachok-infra-state"
  source_archive_object = "erp/function.zip"
  trigger_http          = true
  entry_point           = "handler"
}

resource "google_cloudfunctions_function_iam_member" "function_invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name
  role           = "roles/cloudfunctions.invoker"
  member         = "allUsers"
}
