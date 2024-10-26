from pathlib import Path

import bl1_commander.commands
import bl1_commander.hooks
from mods_base import SETTINGS_DIR
from mods_base import build_mod
from unrealsdk import logging

# .Module or bl1_commander.Module
from .keybinds import (
    on_save_position,
    on_restore_position,
    on_quit_without_saving,
    on_increase_game_speed,
    on_decrease_game_speed,
    on_reset_game_speed,
    on_player_ignore_game_speed,
    on_toggle_ghost,
    on_toggle_hlq_noclip,
    on_make_op,
)

from .hooks import on_player_loaded

from .commands import say_hello_cmd, balance_me_cmd

# Gets populated from `build_mod` below
__version__: str
__version_info__: tuple[int, ...]

build_mod(
    # These are defaulted
    # inject_version_from_pyproject=True, # This is True by default
    # version_info_parser=lambda v: tuple(int(x) for x in v.split(".")),
    # deregister_same_settings=True,      # This is True by default
    keybinds=[
        on_save_position,
        on_restore_position,
        on_quit_without_saving,
        on_increase_game_speed,
        on_decrease_game_speed,
        on_reset_game_speed,
        on_player_ignore_game_speed,
        on_toggle_ghost,
        on_toggle_hlq_noclip,
        on_make_op
    ],
    hooks=[on_player_loaded],
    commands=[say_hello_cmd, balance_me_cmd],
    # Defaults to f"{SETTINGS_DIR}/dir_name.json" i.e., ./Settings/bl1_commander.json
    settings_file=Path(f"{SETTINGS_DIR}/BL1Commander.json"),
)

logging.info(f"BL1 Commander Loaded: {__version__}, {__version_info__}")
