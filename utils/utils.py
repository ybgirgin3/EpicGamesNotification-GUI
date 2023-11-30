from enum import Enum, auto
from dataclasses import dataclass, asdict


# *** ENUMS ***
Retailers = Enum("Retailers", ["EpicGames"])
SaveOrNot = Enum("SaveOrNot", ["SaveAndOpen", "JustSave", "OpenFromMemory"])
SendMail = Enum("SendMail", [("TRUE", True), ("FALSE", False)])


@dataclass
class BackendState:
    retailer_id: int = 1
    save_or_not: int = 1
    send_mail: bool = False

    dict = asdict


@dataclass
class Button:
    name: str
    command: str
    relx: int
    rely: int
    anchor: str


@dataclass
class OptionMenu:
    relx: int
    rely: int
    anchor: str


@dataclass
class CheckBox:
    text: str
    command: str
    onValue: int
    offValue: int
    relx: int
    rely: int
    anchor: str


@dataclass
class Pack:
    padX: int
    padY: int


@dataclass
class Grid:
    row: int
    column: int
    padX: int
    padY: int
