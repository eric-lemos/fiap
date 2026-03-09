#!/bin/bash

http__status_code=$(curl --write-out "%{http_code}" --silent --output /dev/null https://adopet-frontend-cypress.vercel.app/home)

echo "$http__status_code"