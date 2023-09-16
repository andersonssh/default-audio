from typing import List
from simpleaudiocontroller import Device


def devices_to_options(devices: List[Device]):
    result = []
    for device in devices:
        result.append({
            "text": f"{device.name}",
            "emphasis": device.is_current_device,
            "emphasis_text": "(CURRENTLY IN USE)",
            "emphasis_color": "red",
            "id": device.name
        })

    return result
