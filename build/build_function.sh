#!/bin/bash

C_DIR="$(cd -- "$(dirname "$0/")" >/dev/null 2>&1 ; pwd -P)"
TMP_DIR=$(mktemp -d -t ci-XXXX)

cp $C_DIR/../app/*py $TMP_DIR
# cp -R $C_DIR/../app/lib $TMP_DIR/
# cp $C_DIR/../app/src/output/requirements.txt $TMP_DIR

cd $TMP_DIR
# pip3 install --target=. -r requirements.txt
find . -type d -name '*_pycache_*' -exec rm -rf {} +
zip -r $C_DIR/function.zip ./*
