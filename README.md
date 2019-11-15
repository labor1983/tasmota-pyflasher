# Tasmota PyFlasher

![GitHub Releases](https://img.shields.io/github/downloads/tasmota/tasmota-pyflasher/1.0/total?label=downloads&color=%231FA3EC&style=for-the-badge) [![GitHub](https://img.shields.io/github/license/tasmota/tasmota-pyflasher?color=1FA3EC&style=for-the-badge)](https://github.com/tasmota/tasmota-pyflasher/blob/v1/LICENSE) [![Discord](https://img.shields.io/discord/479389167382691863?color=1FA3EC&style=for-the-badge)](https://discord.gg/BdEwrjw)

Simple GUI tool for flashing [Tasmota](https://https://github.com/arendst/Tasmota) firmware wihout any installation. Forked from [NodeMCU Pyflasher](https://github.com/marcelstoer/nodemcu-pyflasher) (based on [esptool.py](https://github.com/espressif/esptool) and [wxPython](https://www.wxpython.org/)).

![Tasmota PyFlasher GUI](images/gui.png)

## Installation
Tasmota PyFlasher doesn't have to be installed, just double-click it and it'll start. Check the [releases section](https://github.com/tasmota/tasmota-pyflasher/releases) for download.

## Getting help
In the unlikely event that you're stuck with this simple tool the best way to get help is [Tasmota Discord](https://discord.gg/Ks2Kzd4).

For flashing instructions and toubleshooting visit [Tasmota Wiki](http://tasmota.com)

## Donationware
Show your love and support for open-source development by [donating to the author](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HFN4ZMET5XS2Q) of the original tool - [NodeMCU PyFlasher](https://github.com/marcelstoer/nodemcu-pyflasher).

## Build it yourself
If you want to build this application yourself you need to:

- Install [Python 3.x](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/) (it comes with Python if installed from `python.org`).
- Create a virtual environment with `python -m venv venv`
- Activate the virtual environment with `. venv/bin/activate` (`. venv/Scripts/activate` if you are on Windows with [Cygwin](https://www.cygwin.com/) or [Mingw](http://mingw.org/))
- Run `pip install -r requirements.txt`

**A note on Linux:** As described on the [downloads section of `wxPython`](https://www.wxpython.org/pages/downloads/), wheels for Linux are complicated and may require you to run something like this to install `wxPython` correctly:

```bash
# Assuming you are running it on Ubuntu 18.04 LTS with GTK3
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 \
    wxPython
```

## Why?

There was no GUI flashing tool with the needed Tasmota default settings.

## License
[MIT](http://opensource.org/licenses/MIT)
