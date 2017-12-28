#!/usr/bin/env bash

CONTAINER_ID="$(docker ps | grep cs-flash-cards | awk '{ print $1 }')"

if [[ ! -z "${CONTAINER_ID}" ]]; then
    docker kill "${CONTAINER_ID}"
    docker rm cs-flash-cards
fi
