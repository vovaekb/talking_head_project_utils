#!/bin/bash

#fill in your credentials
USERNAME="USERNAME"
PASS="YOUR_PASS"

wget --user ${USERNAME} --password ${PASS}  -i download_files.list
