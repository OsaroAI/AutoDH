#!/usr/bin/env bash

cat > ~/.pypirc <<EOL
[distutils]
index-servers = osaro-default
[osaro-default]
repository = https://osaro.jfrog.io/artifactory/api/pypi/local-pypi-prod
username = $PYPI_USERNAME
password = $PYPI_PASSWORD
EOL

