#!/usr/bin/env bash

HASH="$(docker ps | grep cs-flash-cards | awk '{ print $1 }')"

if [[ ! -z "${HASH}" ]]; then
    docker kill $(docker ps | grep cs-flash-cards | awk '{ print $1 }')
    docker rm cs-flash-cards
fi
