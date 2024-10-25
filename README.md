# BL1 PythonSDK Mod Database

This is a temporary repository to centralise PythonSDK mods for BL1.

# Installation Guide

If you haven't already download the PythonSDK release from
[here](https://github.com/Ry0511/pyunrealsdk/releases) and ensure you have
installed it correctly.

Once you have done that you can then do this:

1. Download one or more mods below
2. Extract the contents of the downloaded `.zip` file to your Mods folder at
   `Borderlands/Binaries/Mods`
3. Open `Borderlands.exe` and once you reach the main menu open the console
   and type `mods`
4. Use the on-screen instructions to enable the mod; Once enabled it should
   auto-enable next time you start.

# Contents

- Example User
    - [Example Mod](https://www.example.com/)
    - [Another Example Mod](https://www.example.com/)


- -Ry
    - [BL1 Commander](./Mods/-Ry/Releases/BL1Commander/bl1_commander-1.0.0.zip)


- Example User 2
    - [Example Mod Again](https://www.example.com/)
    - [Example Mod Once More](https://www.example.com/)

# License

Mod developers will decide on the license for their mods. LICENSE.template is
provided as a base but is not required. If you do not know or don't care just
use that.

# Developers Guide

You do not need to add your own folder here. I probably shouldn't have added
mine tbh instead just fork the repo and add to the `README.md` the release of
your mod. Then once you're ready to release just make a PR to merge the changes
into the main repo. Alternatively, you can just link to your own release github
if that is more ideal for you. 

When packaging your mod, package it as a `.zip` file and ensure that the mod can
be directly extracted to the users `Mods/` directory without any issues.
