import customtkinter
from customtkinter import (
    CTkButton,
    CTkCheckBox,
    CTkOptionMenu,
    StringVar,
)
from collections import namedtuple, defaultdict
from typing import Any, DefaultDict, Union

# backend
from utils.backend import backend
from utils.utils import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class EpicGamesGUI:
    app = customtkinter.CTk()

    # state: DefaultDict = defaultdict(lambda: None)

    # optionButtonName: str = None
    # app.geometry("640x480")

    # DEFINITIONS
    # customtkinter.set_window_scaling(0.5)
    # customtkinter.set_widget_scaling(0.5)

    def __init__(self) -> None:
        self.create_app()
        self.app.mainloop()

    def create_app(self):
        return (
            # Select Retailer
            self.grid(
                self.option_menu(
                    # ["EpicGames", "Steam(Experimental)"],
                    [r.name for r in Retailers],
                    DefinedOptionMenu(
                        relx=3,
                        rely=3,
                        anchor="w",
                    ),
                ),
                DefinedGrid(0, 0, 10, 10),
            ),
            # save, open direct
            self.grid(
                self.option_menu(
                    # ["Save and Open", "Just Save"],
                    [s.name for s in SaveOrNot],
                    DefinedOptionMenu(
                        relx=3,
                        rely=3,
                        anchor="w",
                    ),
                ),
                DefinedGrid(1, 0, 10, 10),
            ),
            # send mail or not
            self.grid(
                self.checkbox(
                    DefinedCheckBox(
                        text="Send Mail?",
                        command=self._checkbox_callback,
                        onvalue="on",
                        offvalue="off",
                        relx=3,
                        rely=3,
                        anchor="w",
                    )
                ),
                DefinedGrid(2, 0, 10, 10),
            ),
            # create button pack
            self.grid(
                self.button(DefinedButton("CustomButton", self._button, 0.5, 0.5, "s")),
                DefinedGrid(4, 0, 10, 10),
            ),
        )

    # *** WIDGET FACTORIES ***
    def button(self, button: DefinedButton) -> CTkButton:
        confirm_button = customtkinter.CTkButton(
            master=self.app, text=button.name, command=button.command
        )
        confirm_button.place(
            relx=button.relx,
            rely=button.rely,
            anchor=button.anchor,
        )
        return confirm_button

    def option_menu(self, options: list, option: DefinedOptionMenu) -> CTkOptionMenu:
        defVal = StringVar(
            value=options[0] if len(options) else "No retailer Found to Select"
        )
        optionMenu = CTkOptionMenu(
            master=self.app,
            values=options,
            variable=defVal,
            # NOTE: define command directly because
            # we need to define custom option menu for prevent empty menu items
            command=self._retailer_optionmenu_callback
            if "EpicGames" in options
            else self._save_optionmenu_callback,
        )
        optionMenu.place(
            relx=option.relx,
            rely=option.rely,
            anchor=option.anchor,
        )
        return optionMenu

    def checkbox(self, vars: DefinedCheckBox) -> CTkCheckBox:
        check_var = StringVar(value="off")
        checkboxButton = CTkCheckBox(
            master=self.app,
            text=vars.text,
            variable=check_var,
            command=lambda: vars.command(check_var),
            onvalue=vars.onvalue,
            offvalue=vars.offvalue,
        )

        checkboxButton.place(
            relx=vars.relx,
            rely=vars.rely,
            anchor=vars.anchor,
        )

        return checkboxButton

    def pack(self, obj: Union[CTkButton, CTkOptionMenu, Any], pack: DefinedPack):
        return obj.pack(padx=pack.padx, pady=pack.pady)

    def grid(self, obj: Union[CTkButton, CTkOptionMenu, Any], _grid: DefinedGrid):
        return obj.grid(
            row=_grid.row, column=_grid.column, padx=_grid.padx, pady=_grid.pady
        )

    # *** WIDGET CALLBACKS ***
    @classmethod
    def _button(cls):
        print(BackendState()._asdict)
        # backend(BackendState)

    @classmethod
    def _retailer_optionmenu_callback(cls, choice):
        # print(cls.create_app)
        print([e for e in Retailers])
        print("choise in retailer menu", choice)

        # find choice number for enum
        # retailer = Retailers.choice
        retailer_value = getattr(Retailers, choice).value
        print("retailer_value:", retailer_value)

        backendState = BackendState._replace(retailer=retailer_value)
        # print(BackendState.__asdict__)
        # cls.state["retailer"] = choice

    @classmethod
    def _save_optionmenu_callback(cls, choice):
        # print(cls.create_app)
        print([e for e in SaveOrNot])
        print("choise in save menu", choice)
        save_value = getattr(SaveOrNot, choice).value
        backendState = BackendState._replace(save_or_not=save_value)
        # cls.state["save_or_not"] = choice

    @classmethod
    def _checkbox_callback(cls, val):
        _send_mail = "TRUE" if val.get() == "on" else "FALSE"
        print("_send mail right before the set value to the state", _send_mail)
        check_box_val = getattr(SendMail, _send_mail).value
        print("checkbox", check_box_val)
        backendState = BackendState._replace(send_mail=_send_mail)
        # cls.state["send_mail"] = _send_mail


if __name__ == "__main__":
    EpicGamesGUI()
