import os
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_NAME): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.async_set(f"{DOMAIN}.setup", "complete")
    return True

async def async_setup_entry(hass, config_entry):
    hass.async_add_job(setup_lovelace, hass)
    return True

async def setup_lovelace(hass: HomeAssistant):
    lovelace_path = os.path.join(
        hass.config.path(), ".storage", "lovelace"
    )
    with open(lovelace_path, "r") as f:
        lovelace_config = f.read()

    # Agregar la tarjeta predefinida
    predefined_lovelace_path = os.path.join(
        hass.config.path(), "custom_components", DOMAIN, "lovelace.yaml"
    )
    with open(predefined_lovelace_path, "r") as f:
        predefined_lovelace = f.read()

    lovelace_config += "\n" + predefined_lovelace

    with open(lovelace_path, "w") as f:
        f.write(lovelace_config)

    hass.components.lovelace.reload_lovelace()
