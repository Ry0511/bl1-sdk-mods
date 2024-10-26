import argparse

from mods_base import command
from mods_base import get_pc

from .keybinds import display_hud_message

################################################################################
# | EXAMPLE COMMAND |
################################################################################


# !sayhello -n="-Ry" -a=23
@command(cmd="!sayhello", description="Says hello to the user.")
def say_hello_cmd(args: argparse.Namespace) -> None:
    print(f"Hello {args.name} with age {args.age}!")
    return


# The option -h, --help is hidden and can be used to print help information
# !sayhello -h
# !sayhello --help
# !sayhello -n="Ryan" --age=23
# !sayhello --name="-Ry" -a=23

# Default valued command
say_hello_cmd.add_argument(
    "-n", "--name",
    type=str,
    default="Unknown",
    help="The user to say hello to"
)

# If unspecified the value will be `None` even if marked as required
say_hello_cmd.add_argument(
    "-a", "--age",
    type=int,
    required=True,
    help="The age of the user to say hello to"
)

################################################################################
# | BALANCE ME COMMAND |
################################################################################


@command(
    cmd="!balanceme",
    description="Balances the player to a specified gamestage and awesome level;"
                " This deletes your inventory."
)
def balance_me_cmd(args: argparse.Namespace) -> None:

    if args.gamestage is None or args.awesome_level is None:
        print("--gamestage and --awesome_level are required")
        return

    pc = get_pc()

    if pc is None or pc.Pawn is None:
        print("Player Controller or Player Pawn is None; aborting...")
        return

    # NOTE: if UNREALSDK_LOCKING_PROCESS_EVENT=1 is defined this will become a
    #  DEADLOCK. There might be a `CallAfter` system somewhere will need to ask
    #  apple1417 about it.
    pc.ServerBalanceMe(args.gamestage, args.awesome_level)



balance_me_cmd.add_argument("-gs", "--gamestage", type=int)
balance_me_cmd.add_argument("-al", "--awesome-level", type=int)
