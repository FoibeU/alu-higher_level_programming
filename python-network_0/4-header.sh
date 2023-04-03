#!/bin/bash
# sends a GET request and sets a header to the URL
curl -sH "X-HolbertonSchool-User-Id" "${1}"
