#!/bin/sh
echo "Installing"
chmod 777 /usr/local/share/kwdesktop/*
su si  -c "/usr/local/share/kwdesktop/kw-insight-cmd-installer.linux.sh --agree -i /home/si/kwdesktop/ --klocwork-server 10.221.57.29:8080 --license-server 10.223.10.21:27000"
su si -c "cp /usr/local/share/kwdesktop/kwcheck_create_wr.sh /home/si/kwdesktop/bin"
su si -c "cp /usr/local/share/kwdesktop/kw_check_run_wr.sh /home/si/kwdesktop/bin"
su si -c "cp /usr/local/share/kwdesktop/kwshell_wr.sh /home/si/kwdesktop/bin"
