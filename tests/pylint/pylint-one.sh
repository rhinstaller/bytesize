#!/bin/bash
#
# $1 -- python source to run pylint on
#

if [ $# -lt 1 ]; then
    # no source, just exit
    exit 1
fi

file_suffix="$(eval echo \$$#|sed s?/?_?g)"

pylint_output="$(pylint \
    --msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}' \
    -r n --disable=C,R --rcfile=/dev/null \
    --dummy-variables-rgx=_ \
    --ignored-classes=Popen,TransactionSet \
    --defining-attr-methods=__init__,_grabObjects,initialize,reset,start,setUp \
    --load-plugins=intl,pointless-override \
    $DISABLED_WARN_OPTIONS \
    $DISABLED_ERR_OPTIONS \
    $NON_STRICT_OPTIONS "$@" 2>&1 | \
    egrep -v -f "$FALSE_POSITIVES" \
    )"

# I0011 is the informational "Locally disabling ...." message
if [ -n "$(echo "$pylint_output" | fgrep -v '************* Module ' |\
          grep -v '^I0011:')" ]; then
    # Replace the Module line with the actual filename
    pylint_output="$(echo "$pylint_output" | sed "s|\* Module .*|* Module $(eval echo \$$#)|")"
    echo "$pylint_output" > pylint-out_$file_suffix
    touch "pylint-$file_suffix-failed"
fi
