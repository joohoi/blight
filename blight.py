#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string

# Modify this to match your configuration
BACKLIGHT_DIR = "/sys/class/backlight/intel_backlight"


try:
    with open(BACKLIGHT_DIR+"/max_brightness",'r') as fh:
        MAX_BRIGHTNESS = int("".join(fh.readlines()))

    with open(BACKLIGHT_DIR+"/brightness", 'r') as fh:
        CUR_BRIGHTNESS = int("".join(fh.readlines()))
except IOError:
    print("Error opening control files under {}".format(BACKLIGHT_DIR))
    sys.exit(-1)

def usage():
    print(("Control display backlight.\n"
          "Usage: {prog} [+|-]0-100% \n\n"
          "Examples:\n"
          "{prog} +15%\t - increase brightness by 15%\n"
          "{prog} -10%\t - decrease brightness by 10%\n"
          "{prog} 75% \t - set brightness to 75%\n").format(prog=sys.argv[0]))
    sys.exit(0)

def change_amount(verb, change_percent):
    amount = MAX_BRIGHTNESS * (float(change_percent)/100)
    if verb == "increase":
        new_value = CUR_BRIGHTNESS+amount
    elif verb == "decrease":
        new_value = CUR_BRIGHTNESS-amount
    elif verb == "set":
        new_value = amount

    if new_value > MAX_BRIGHTNESS:
        new_value = MAX_BRIGHTNESS
    elif new_value < 0:
        new_value = 0
    return int(new_value)

def sanitize_input(str_in):
    everything = string.maketrans('', '')
    digits = everything.translate(everything, string.digits)
    return str_in.translate(everything, digits)

def get_verb(str_in):
    if str_in.strip()[0] == "-":
        return "decrease"
    elif str_in.strip()[0] == "+":
        return "increase"
    else:
        return "set"

def change_brightness(verb, amount):
    set_value = change_amount(verb, amount)
    with open(BACKLIGHT_DIR+"/brightness", 'w') as fh:
        fh.write(str(set_value))
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    verb = get_verb(sys.argv[1])
    value = sanitize_input(sys.argv[1])
    change_brightness(verb, value)
