#!/bin/bash

INDEX=""
APIKEY=""
PORT="7700"

URL="http://localhost:$PORT/indexes/$INDEX---notes/settings"

curl \
  -X PATCH $URL \
  -H "Authorization: Bearer $APIKEY" \
  -H 'Content-Type: application/json' \
  --data-binary '{
    "searchableAttributes": [
      "text",
      "cw"
    ],
    "sortableAttributes": [
      "createdAt"
    ],
    "filterableAttributes": [
      "createdAt",
      "userId",
      "userHost",
      "channelId",
      "tags"
    ],
    "typoTolerance": {
      "enabled": false
    },
    "pagination": {
      "maxTotalHits": 10000
    }
}'
