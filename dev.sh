#!/bin/bash

docker run \
	-ti \
	-p 8000:8000 \
	-v $(pwd)/src/app:/src \
	-v $(pwd)/.key.json:/gcp/key.json:ro \
	--env GOOGLE_APPLICATION_CREDENTIALS=/gcp/key.json \
	erp-api \
	uvicorn main:app --proxy-headers --reload --host 0.0.0.0 --port 8000
