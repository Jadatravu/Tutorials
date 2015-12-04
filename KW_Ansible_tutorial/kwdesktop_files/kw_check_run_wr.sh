#!/bin/sh
/home/si/kwdesktop/bin/kwcheck run --verbose -F quiet -j auto -pd ~/klocwork_projects/$1/kwlp -sd ~/klocwork_projects/$1/kwps --always-on @$2 --plugin-mode --output-encoding=UTF-8 --lang en
