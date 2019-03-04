#!/bin/bash

for each in $(ls); do
	if [[ -d $each/py ]]; then
		echo $each
		pushd $each/py > /dev/null; nosetests; popd > /dev/null
	fi
done
