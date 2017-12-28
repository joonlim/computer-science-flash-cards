#!/usr/bin/env bash

IMAGE="cs-flash-cards"
BINDIR=${0%/*}

docker run -d -p 80:8000 --name "${IMAGE}" -v "$(realpath ${BINDIR})":/src/db "${IMAGE}"
