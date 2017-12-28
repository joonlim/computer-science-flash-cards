#!/usr/bin/env bash

IMAGE_ID="$(docker images | grep cs-flash-cards | awk '{ print $3 }')"

if [[ ! -z "${IMAGE_ID}" ]]; then
    docker rmi "${IMAGE_ID}"
fi
