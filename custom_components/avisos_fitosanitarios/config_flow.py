from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, TIPOS_CULTIVOS

class AvisosFitosanitariosConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Avisos Fitosanitarios", data=user_input)

        data_schema = vol.Schema({
            vol.Required("categorias"): vol.All(vol.Length(min=1), [vol.In(TIPOS_CULTIVOS.keys())]),
            vol.Required("cultivos"): vol.All(vol.Length(min=1), [vol.In([especie for sublist in TIPOS_CULTIVOS.values() for especie in sublist])]),
            vol.Optional("use_api", default=False): bool,
            vol.Optional("api_key", default=""): str
        })

        return self.async_show_form(step_id="user", data_schema=data_schema)

    async def async_step_import(self, user_input=None):
        return await self.async_step_user(user_input)
