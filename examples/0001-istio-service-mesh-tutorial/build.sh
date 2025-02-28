#!/bin/bash

# commonly used for debugging purposes
# where it prints each command before it's being printed
set -x


VER="${VER:-latest}"
LESSON="${LESSON:-lesson000}"
PROFILE="${PROFILE:-imalamin}"

docker build -t ${PROFILE}/practice-app-${LESSON}:${VER} -f practice-app/Dockerfile --platform linux/amd64 practice-app
docker push ${PROFILE}/practice-app-${LESSON}:${VER}
