# BL1 Commander

Commander style mod which contains various quality of life features.
It also acts as an example mod for those who want to learn how to mod
Borderlands 1 using the PythonSDK.

# Credits

This mod is based heavily on the BL2 Commander mods by **c0dycode**
and **mopiod** and also on **apple1417's** various cheaty mods.

# Features

* Save Restore Position
* Quitting to Menu without saving
* Modifying gamespeed and having the player ignore the speed
* Removing the 30s timer required for saving
* Toggle Ghost Mode (unbound by default)
* Toggle HLQ Noclip (unbound by default)
* Rebalance to level 69 (unbound by default)

# Developers

This section is only useful to people who would like to learn how to create
python mods. This assumes you have a basic to intermediate understanding of
programming (Procedural or OOP). I recommend looking at these files (in order)
as it shows you how to use the features of the sdk.

1. `__init__.py` Entry point for python sdk mods
2. `pyproject.toml` Configuration file for setting up your mod
3. `keybinds.py` Contains keybind hooks for actions
4. `hooks.py` Contains unrealscript hooks
5. `commands.py` Contains custom console commands

If you follow the example provided you should be able to use the console command
`rlm folder_name` in-game to hot-reload your mod. This way you don't have to
reset your game to see changes. Something's might still require a full reset
though.
