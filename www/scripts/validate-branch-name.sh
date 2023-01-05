#!/usr/bin/env bash
local_branch_name="$(git rev-parse --abbrev-ref HEAD)"

valid_branch_regex='^((feature|fix|hotfix|release|support|dev|main|HEAD)\/[a-zA-Z0-9\-]+)$'

message="❌ Meeera mano este branch tiene un nombre feo. Intenta algo como:\n\n$valid_branch_regex\n\n"

if [[ ! $local_branch_name =~ $valid_branch_regex ]]; then
    printf "$message"
    exit 1
fi

exit 0
