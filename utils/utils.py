from enum import Enum, auto
from collections import namedtuple


# *** ENUMS ***
Retailers = Enum("Retailers", ["EpicGames"])
SaveOrNot = Enum("SaveOrNot", ["SaveAndOpen", "JustSave", "OpenFromMemory"])
SendMail = Enum("SendMail", [("TRUE", True), ("FALSE", False)])


# class Retailers(IntEnum):
#     EpicGames = 1


# class SaveOrNot(IntEnum):
#     SaveAndOpen = 1
#     JustSave = 2
#     OpenFromMemory = 3


# *** NAMEDTUPLES ***
BackendState = namedtuple("BackendState", ["retailer", "save_or_not", "send_mail"])
BackendState.__new__.__defaults__ = (
    Retailers._value2member_map_.get(1).value,
    SaveOrNot._value2member_map_.get(1).value,
    SendMail._value2member_map_.get(1).value,
)

# define button
DefinedButton = namedtuple(
    "DefinedButton", ["name", "command", "relx", "rely", "anchor"]
)
DefinedButton.__new__.__defaults__ = ("",) * len(DefinedButton._fields)

# define option menu
DefinedOptionMenu = namedtuple(
    "DefinedOptionMenu",
    ["relx", "rely", "anchor"],
)
DefinedOptionMenu.__new__.__defaults__ = ("",) * len(DefinedOptionMenu._fields)

# define checkbox
DefinedCheckBox = namedtuple(
    "DefinedCheckBox",
    ["text", "command", "onvalue", "offvalue", "relx", "rely", "anchor"],
)
DefinedCheckBox.__new__.__defaults__ = ("",) * len(DefinedCheckBox._fields)

# define a slider
DefinedSlider = namedtuple(
    "DefinedSlider", ["from_", "to_", "command", "relx", "rely", "anchor"]
)

# define pack
DefinedPack = namedtuple("DefinedPack", ["padx", "pady"])
DefinedPack.__new__.__defaults__ = (0,) * len(DefinedPack._fields)

# define grid
DefinedGrid = namedtuple("DefinedGrid", ["row", "column", "padx", "pady"])
DefinedGrid.__new__.__defaults__ = (0,) * len(DefinedGrid._fields)
