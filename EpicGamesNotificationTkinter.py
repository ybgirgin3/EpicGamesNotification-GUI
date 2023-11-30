import customtkinter

from customtkinter import (
    CTkButton,
    CTkCheckBox,
    CTkOptionMenu,
    StringVar,
)
from typing import Any, Union

# backend
from utils.backend import backend
from utils.utils import *
from dacite import from_dict

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class EpicGamesGUI:
    app = customtkinter.CTk()

    bs = BackendState().dict()

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
                    OptionMenu(
                        relx=3,
                        rely=3,
                        anchor="w",
                    ),
                ),
                Grid(0, 0, 10, 10),
            ),
            # save, open direct
            self.grid(
                self.option_menu(
                    # ["Save and Open", "Just Save"],
                    [s.name for s in SaveOrNot],
                    OptionMenu(
                        relx=3,
                        rely=3,
                        anchor="w",
                    ),
                ),
                Grid(1, 0, 10, 10),
            ),
            # send mail or not
            self.grid(
                self.checkbox(
                    CheckBox(
                        text="Send Mail?",
                        command=self._checkbox_callback,
                        onValue="on",
                        offValue="off",
                        relx=3,
                        rely=3,
                        anchor="w",
                    )
                ),
                Grid(2, 0, 10, 10),
            ),
            # create button pack
            self.grid(
                self.button(Button("CustomButton", self._button, 0.5, 0.5, "s")),
                Grid(4, 0, 10, 10),
            ),
        )

    # *** WIDGET FACTORIES ***
    def button(self, button: Button) -> CTkButton:
        confirm_button = customtkinter.CTkButton(
            master=self.app, text=button.name, command=button.command
        )
        confirm_button.place(
            relx=button.relx,
            rely=button.rely,
            anchor=button.anchor,
        )
        return confirm_button

    def option_menu(self, options: list, option: OptionMenu) -> CTkOptionMenu:
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

    def checkbox(self, vars: CheckBox) -> CTkCheckBox:
        check_var = StringVar(value="off")
        checkboxButton = CTkCheckBox(
            master=self.app,
            text=vars.text,
            variable=check_var,
            command=lambda: vars.command(check_var),
            onvalue=vars.onValue,
            offvalue=vars.offValue,
        )

        checkboxButton.place(
            relx=vars.relx,
            rely=vars.rely,
            anchor=vars.anchor,
        )

        return checkboxButton

    def grid(self, obj: Union[CTkButton, CTkOptionMenu, Any], _grid: Grid):
        return obj.grid(
            row=_grid.row, column=_grid.column, padx=_grid.padX, pady=_grid.padY
        )

    # *** WIDGET CALLBACKS ***
    @classmethod
    def _button(cls):
        print(cls.bs)
        backend(state=from_dict(data_class=BackendState, data=cls.bs))

    @classmethod
    def _retailer_optionmenu_callback(cls, choice):
        retailer_value = getattr(Retailers, choice).value
        cls.bs["retailer_id"] = retailer_value
        print("bs after update", cls.bs)

    @classmethod
    def _save_optionmenu_callback(cls, choice):
        save_value = getattr(SaveOrNot, choice).value
        print("save value", save_value)
        cls.bs["save_or_not"] = save_value
        print("bs after update", cls.bs)

    @classmethod
    def _checkbox_callback(cls, val):
        _send_mail = "TRUE" if val.get() == "on" else "FALSE"
        check_box_val = getattr(SendMail, _send_mail).value
        print("checkbox", check_box_val)
        cls.bs["send_mail"] = check_box_val
        print("bs after update", cls.bs)


if __name__ == "__main__":
    EpicGamesGUI()
