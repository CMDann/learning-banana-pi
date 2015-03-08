#!/bin/bash

function gpio()
{
    local verb=$1
    local pin=$2
    local value=$3

    local pins=($GPIO_PINS)
    if [[ "$pin" -lt ${#pins[@]} ]]; then
        local pin=${pins[$pin]}
    fi

    local gpio_path=/sys/class/gpio
    local pin_path=$gpio_path/gpio$pin

    case $verb in
        read)
            cat $pin_path/value
        ;;

        write)
            echo $value > $pin_path/value
        ;;

        mode)
            if [ ! -e $pin_path ]; then
                echo $pin > $gpio_path/export
            fi
            echo $value > $pin_path/direction
        ;;

        *)
            echo "Usage: $0 mode [pin] [in|out]"
            echo "       $0 read [pin]"
            echo "       $0 write [pin] [0|1]"
            echo "If GPIO_PINS is an environment variable containing"
            echo "a space-delimited list of integers, then up to 17"
            echo "logical pins (0-16) will map to the physical pins"
            echo "specified in the list."
        ;;
    esac
}

if [ "$BASH_SOURCE" == "$0" ]; then
    gpio $@
fi
