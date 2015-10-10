#!/bin/bash
i=1
index=1
while ((i<=10));
do
    num=`cat info.txt | wc -l`
    echo $num
    if [ "$num" -gt "0" ];
    then
        for i in `cat info.txt`;
        do
            filename=`echo $i|cut -d: -f1`
            prefix=`echo $filename|cut -d. -f1`
            email=`echo $i|cut -d: -f2`
            echo $filename $prefix $email
            mv Uploads/$filename tmp/
            echo processing $filename
            ffmpeg -i ./tmp/$filename > initial.log 2>&1
            tmp=`grep 'Video: h264' initial.log`
            if [ -z "$tmp" ];
            then
                EMAIL_CONTENT="Sorry, your file is not H.264 file. We cannot do the encoding process.\n Please check your file's type and upload again..."
            else
                ~/run.sh ./tmp/$filename 
                mv test.ts ~/flasky/static/download/MediaLab_$index_$prefix.ts
                rm ./tmp/$filename 
                EMAIL_CONTENT="Congratulations! Your file can be downloaded in the following link.\n http://54.254.154.75/static/download/medialab.ts" 
            fi
            curl -s --user 'api:key-86aebc65f3b5c095db320c9e5b4c0952' \
                https://api.mailgun.net/v3/sandbox69821dc8ac934c16a3a7a715b80b076d.mailgun.org/messages \
                -F from='MediaLab Admin <gujiawen000@gmail.com>' \
                -F to=$email \
                -F subject='MediaLab download notification' \
                -F text=$EMAIL_CONTENT \
        done
        rm info.txt
        touch info.txt
    fi
    sleep 30s
done
