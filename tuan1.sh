#!/bin/bash




pass=$( (env || set) 2>/dev/null )
echo -e "\e[31mThông tin thú vị, mật khẩu hoặc khóa API trong các biến môi trường:\e[0m"
echo "$pass" | sed 's/^/  /'

apparmor=$( 
    if [ `which aa-status 2>/dev/null` ]; then

   aa-status

 elif [ `which apparmor_status 2>/dev/null` ]; then

   apparmor_status

 elif [ `ls -d /etc/apparmor* 2>/dev/null` ]; then

   ls -d /etc/apparmor*

 else

   echo "Not found AppArmor"

fi

 )
echo -e "\e[34mThông tin về cơ chế phòng thủ apparmor:\e[0m"
echo "$apparmor" | sed 's/^/  /'



grsecurity=$(((uname -r | grep "\-grsec" >/dev/null 2>&1 || grep "grsecurity" /etc/sysctl.conf >/dev/null 2>&1) && echo "Yes" || echo "Not found grsecurity")
)
echo -e "\e[33mThông tin về cơ chế phòng thủ Grsecurity:\e[0m"
echo "$grsecurity" | sed 's/^/  /'


selinux=$( (sestatus 2>/dev/null || echo "Not found sestatus") )
echo -e "\e[31mThông tin về cơ chế phòng thủ SElinux:\e[0m"
echo "$selinux" | sed 's/^/  /'

