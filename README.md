# Laptop screen backlight control for Linux

Small shell script to control screen backlight in linux

```
Control display backlight.
Usage: /usr/local/bin/blight.py [+|-]0-100% 

Examples:
/usr/local/bin/blight.py +15%	 - increase brightness by 15%
/usr/local/bin/blight.py -10%	 - decrease brightness by 10%
/usr/local/bin/blight.py 75% 	 - set brightness to 75%
```

## Install
```
git clone https://github.com/joohoi/blight
sudo cp blight/blight.py /usr/local/bin
sudo chmod a+x /usr/local/bin
```

Edit /usr/local/bin/blight.py to point it to correct directory for backlight control, eg:

```
BACKLIGHT_DIR = "/sys/class/backlight/intel_backlight"
```

Add following line to your sudoers file to let unprivileged users to run the script with appropriate privileges using sudo

```
ALL     ALL=NOPASSWD: /usr/local/bin/blight.py
```

## i3-wm configuration

If you are running i3-wm and have multimedia keys, check the keycodes using `xev` and add the appropriate bindings. In my system:


```
bindsym XF86MonBrightnessUp exec sudo blight.py +5%
bindsym XF86MonBrightnessDown exec sudo blight.py -5%
```

Refresh your i3 configuration (default mod+shift+r) and you should be good to go
