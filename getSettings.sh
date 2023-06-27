#!/bin/bash

INDEX=""
APIKEY=""
PORT="7700"

URL="http://localhost:$PORT/indexes/$INDEX---notes/settings"

curl \
  -X GET $URL \
  -H "Authorization: Bearer $APIKEY"
