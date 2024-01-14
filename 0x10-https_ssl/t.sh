#!/usr/bin/env bash
#
# shellcheck disable=SC2086
if [ "$#" -gt 1 ]
then
	res=$(dig "$1"| grep -A1 'ANSWER SECTION:')
	rec=$(echo "$res" | awk 'NR==2' | awk '{print $4}')
	ip=$(echo "$res" | awk 'NR==2' | cut -d ' ' -f3)
	echo $ip
else
	echo "The subdomain www is a A record and points to [DESTINATION]"
	echo "The subdomain lb-01 is a A record and points to [DESTINATION]"
	echo "The subdomain web-01 is a A record and points to [DESTINATION]"
	echo "The subdomain web-02 is a A record and points to [DESTINATION]"
fi
