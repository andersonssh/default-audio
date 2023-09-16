from rich import print as rich_print
from rich.console import Console
from typing import Union

console = Console()


def clear_console(func):
    def wrapper(*args, **kwargs):
        console.clear()
        return func(*args, **kwargs)
    return wrapper


def get_valid_list_index(user_input: str, original_list: list, start_option_index: int):
    numeric_entry = "".join([i for i in user_input if i.isnumeric()])
    if not numeric_entry:
        return None

    numeric_entry = int(numeric_entry)
    index = numeric_entry - start_option_index
    if index < 0 or index >= len(original_list):
        return None
    return index


class Interface:
    def __init__(self, main_menu: str):
        self.main_menu = main_menu

    @clear_console
    def show_options(self, question_text: str, options: list, start_option_index: int = 1):
        """Show options and return the selected one"""
        console.print(self.main_menu.upper(), justify="center", style="bold underline", width=80)
        console.print(end="\n")
        console.print(question_text, justify="left", style="bold", width=80)
        for index, option in enumerate(options, start=start_option_index):
            text = option["text"]
            emphasis = option.get("emphasis")
            emphasis_text = option.get("emphasis_text")
            emphasis_color = option.get("emphasis_color")
            console.print(
                f" {f'[{emphasis_color}]' if emphasis and emphasis_color else ''}"
                f"{index}. "
                f"{text}"
                f"{f' {emphasis_text}' if emphasis and emphasis_text else ''}"
                f"{f'[/{emphasis_color}]' if emphasis and emphasis_color else ''}",
                highlight=False
            )
        console.print(style="bold underline", width=80, end="\n")

        entry = input("Option: ")
        option_index = get_valid_list_index(entry, options, start_option_index)
        if option_index is None:
            return None
        return options[option_index]["id"]


def print_success():
    console.print("Operation [bold green]completed successfully![/bold green] :tada: :thumbs_up:",
                  justify="center", width=80)
    input("Press enter to continue...")


def print_fail():
    console.print("Operation [bold red]failed![/bold red] :cry: :thumbs_down:",
                  justify="center", width=80)
    input("Press enter to continue...")
