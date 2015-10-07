#!/usr/bin
i=1
while ((i<=10));
do
    count=`ls Uploads/ | wc -l`
    if [ "$count" -gt "0" ];
    then 
        echo $count
        mv Uploads/* tmp/*
        filename='ls tmp/'
        echo $filename
        ffmpeg -i ./tmp/$filename -y ./download/medialab.ts
    fi
    sleep 30s
done
