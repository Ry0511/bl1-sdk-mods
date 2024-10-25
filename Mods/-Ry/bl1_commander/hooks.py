import unrealsdk
from unrealsdk.hooks import Type
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from mods_base import hook


@hook(
    hook_func="WillowGame.WillowPlayerController:SpawningProcessComplete",
    hook_type=Type.POST,
)
def on_player_loaded(
    obj: UObject,
    __args: WrappedStruct,
    __ret: any,
    __func: BoundFunction,
) -> None:
    # This removes the 30s timer required for saving
    obj.ClientSetProfileLoaded()

    # This enabled cool things :)
    if obj.CheatManager is None:
        obj.CheatManager = unrealsdk.construct_object(
            "WillowGame.WillowCheatManager", obj
        )
