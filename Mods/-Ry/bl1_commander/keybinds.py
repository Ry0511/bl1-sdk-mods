import mods_base
from mods_base import keybind
from mods_base import EInputEvent
from mods_base import get_pc
import unrealsdk

from unrealsdk import logging
from unrealsdk.unreal import WrappedStruct

################################################################################
# | UTILITY |
################################################################################


def display_hud_message(title: str, msg: str, msg_type: int = 0, duration: float = 1.5):
    # WillowPlayerController, WillowHUD, and WillowHUDMovie
    # WillowHUD.DisplayCustomMessage
    pc = get_pc()
    white = unrealsdk.make_struct("Core.Object.Color", B=255, G=255, R=255, A=255)

    hud = pc.myHUD
    if hud is None:
        return

    hud_movie = hud.GetHUDMovie()
    if hud_movie is None:
        return

    global _game_speed_scalar
    scaled_duration = max(0.005, duration * _game_speed_scalar)

    hud_movie.AddTrainingText(
        0, msg, title, scaled_duration, white, "", False, 0.0, None, True
    )


################################################################################
# | SAVE RESTORE POSITION |
################################################################################

# Will probably add more slots
_saved_location: tuple[float, float, float] = (0, 0, 0)


def is_player_available() -> bool:
    pc = mods_base.get_pc()
    return pc is not None and pc.Pawn is not None


@keybind(identifier="Save Position", key="F7", event_filter=None)
def on_save_position(event: EInputEvent):
    if event is EInputEvent.IE_Released or not is_player_available():
        return

    global _saved_location
    pos: WrappedStruct = get_pc().Pawn.Location
    _saved_location = (pos.X, pos.Y, pos.Z)
    display_hud_message("BL1 Comander", "Position Saved!")


@keybind(identifier="Restore Position", key="F8", event_filter=EInputEvent.IE_Released)
def on_restore_position():
    if not is_player_available():
        return

    global _saved_location
    wpc = get_pc()
    pos = unrealsdk.make_struct(
        "Vector", X=_saved_location[0], Y=_saved_location[1], Z=_saved_location[2]
    )

    # wpc.Pawn.SetLocation might work
    wpc.NoFailSetPawnLocation(wpc.Pawn, pos)
    display_hud_message("BL1 Comander", "Position Restored!")


################################################################################
# | QUIT WITHOUT SAVING |
################################################################################


@keybind(identifier="Quit Without Saving", key="F9")
def on_quit_without_saving():
    if not is_player_available():
        return

    wpc = get_pc()
    wpc.DestroyOnlineGame(False)
    wpc.ConsoleCommand("open menumap")


################################################################################
# | MODIFY GAME SPEED |
################################################################################

# This is more of a gimmick than an actual feature. It works but not perfectly.
_player_ignores_speed: bool = False
_game_speed_scalar: float = 1.0


def update_game_speed(display_message: bool = True):
    global _game_speed_scalar
    global _player_ignores_speed

    _game_speed_scalar = max(0.01, min(10.0, _game_speed_scalar))

    pc = get_pc()
    pc.WorldInfo.TimeDilation = _game_speed_scalar

    if _player_ignores_speed:
        pc.Pawn.CustomTimeDilation = min(10.0, 1.0 / _game_speed_scalar)
    else:
        pc.Pawn.CustomTimeDilation = 1.0

    if display_message:
        display_hud_message("BL1 Commander", f"Game Speed: {_game_speed_scalar:.2f}")


@keybind(identifier="Decrease Game Speed", key="LeftBracket")
def on_decrease_game_speed():
    if not is_player_available():
        return

    global _game_speed_scalar
    _game_speed_scalar *= 0.8
    update_game_speed()


@keybind(identifier="Increase Game Speed", key="RightBracket")
def on_increase_game_speed():
    if not is_player_available():
        return

    global _game_speed_scalar
    _game_speed_scalar *= 1.25
    update_game_speed()


@keybind(identifier="Reset Game Speed", key="Semicolon")
def on_reset_game_speed():
    if not is_player_available():
        return

    global _game_speed_scalar
    _game_speed_scalar = 1.0
    update_game_speed()


@keybind(identifier="Player Ignores Game Speed (Toggle)", key="Quote")
def on_player_ignore_game_speed():
    if not is_player_available():
        return

    logging.info("Player Ignores Game Speed!")
    global _player_ignores_speed
    _player_ignores_speed = not _player_ignores_speed

    msg: str
    if _player_ignores_speed:
        msg = "Player Ignores Game Speed!"
    else:
        msg = "Player Doesn't Ignore Game Speed!"

    display_hud_message("BL1 Commander", msg)
    update_game_speed(display_message=False)


################################################################################
# | CHEAT FEATURES |
################################################################################


@keybind(
    identifier="Toggle Ghost Mode",
    key="",
    description="Gives noclip not sure how it differs from HLQ"
                " maybe enemies don't see you?",
)
def on_toggle_ghost():
    if not is_player_available():
        return

    get_pc().ServerToggleGhost()


@keybind(
    identifier="Toggle HLQ Noclip",
    key="",
    description="Gives noclip (its faster than ghost mode)",
)
def on_toggle_hlq_noclip():
    if not is_player_available():
        return

    get_pc().ServerToggleHLQ()


@keybind(
    identifier="Make me overpowered",
    key="",
    description="Makes the user level 69 and gives them some good gear;"
    " This deletes your inventory.",
)
def on_make_op():
    if not is_player_available():
        return

    get_pc().ServerBalanceMe(100, 100)
