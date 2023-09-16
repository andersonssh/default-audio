from simpleaudiocontroller import AudioController, DeviceTypes
from interface import Interface, print_success, print_fail
from parsers import devices_to_options
from enum import Enum


class MainMenuOptions(str, Enum):
    HEADPHONE = "headphone"
    MICROPHONE = "microphone"
    SETTINGS = "settings"


audio_controller = AudioController()
interface = Interface("Simple control audio devices")


def devices_main(device_type: DeviceTypes) -> bool:
    devices = []
    if device_type == DeviceTypes.HEADPHONE:
        devices = audio_controller.get_headphones()
    elif device_type == DeviceTypes.MICROPHONE:
        devices = audio_controller.get_microphones()
    if not devices:
        return False

    options = devices_to_options(devices)
    selected_device_name = interface.show_options("Select the device you want to use", options)
    selected_device = audio_controller.get_device_by_name(selected_device_name, device_type)
    return audio_controller.set_default_device(selected_device)


def settings_main():
    pass


def main():
    selected_option = interface.show_options(
        "Select a option", [
            {"text": "Set default Phone", "id": MainMenuOptions.HEADPHONE},
            {"text": "Set default Microphone", "id": MainMenuOptions.MICROPHONE},
            {"text": "Load settings at system startup", "id": MainMenuOptions.SETTINGS}
        ]
    )

    if selected_option in [DeviceTypes.HEADPHONE, DeviceTypes.MICROPHONE]:
        result = devices_main(selected_option)
    elif selected_option == MainMenuOptions.SETTINGS:
        result = settings_main()
    else:
        result = False

    if result:
        print_success()
    else:
        print_fail()


if __name__ == '__main__':
    while True:
        main()
