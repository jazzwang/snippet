#!/bin/bash
if [ $1 == ""]; exit 1; fi
export user_id = $1

curl -s -k -H "Authorization: Basic ${base64_usr_pwd}" \
"${base_url}/activity?maxResults=300&streams=user+IS+${user_id}" -o ${user_id}.xml