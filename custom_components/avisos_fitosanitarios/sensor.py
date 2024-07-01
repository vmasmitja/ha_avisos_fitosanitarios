import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import callback
from homeassistant.helpers.dispatcher import dispatcher_send
from homeassistant.util import Throttle
from .const import DOMAIN, PDF_URLS, TIPOS_CULTIVOS
from . import catalunya

_LOGGER = logging.getLogger(__name__)
MIN_TIME_BETWEEN_UPDATES = timedelta(days=1)

NEW_CULTIVO_SIGNAL = "new_cultivo_signal"

def setup_platform(hass, config, add_entities, discovery_info=None):
    categorias = config.get("categorias", [])
    cultivos = config.get("cultivos", [])
    sensors = []

    for categoria in categorias:
        for cultivo in cultivos:
            sensors.append(AvisoFitosanitarioSensor(hass, categoria, cultivo))

    add_entities(sensors, True)

class AvisoFitosanitarioSensor(SensorEntity):

    def __init__(self, hass, categoria, cultivo):
        self._hass = hass
        self._categoria = categoria
        self._cultivo = cultivo
        self._state = None
        self._pdf_url = None

    @property
    def name(self):
        return f"Avisos Fitosanitarios - {self._categoria} - {self._cultivo}"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"pdf_url": self._pdf_url}

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        avisos, pdf_url = catalunya.get_avisos(PDF_URLS["catalunya"][self._categoria], [self._cultivo])
        self._state = avisos.get(self._cultivo, "No hay avisos")
        self._pdf_url = pdf_url

        # Comprobar si hay nuevos cultivos
        nuevos_cultivos = avisos.get("nuevos_cultivos", [])
        for nuevo_cultivo in nuevos_cultivos:
            if nuevo_cultivo not in TIPOS_CULTIVOS.values():
                self._hass.async_run_job(self._notify_new_cultivo, nuevo_cultivo)

    @callback
    def _notify_new_cultivo(self, cultivo):
        dispatcher_send(self._hass, NEW_CULTIVO_SIGNAL, cultivo)
        _LOGGER.info(f"Nuevo cultivo encontrado: {cultivo}")

def async_setup_entry(hass, config_entry, async_add_entities):
    hass.data[DOMAIN][config_entry.entry_id] = config_entry.data
    setup_platform(hass, config_entry.data, async_add_entities)

def async_setup(hass, config):
    def handle_new_cultivo_signal(cultivo):
        hass.components.persistent_notification.create(
            f"Se ha encontrado un nuevo cultivo: {cultivo}", title="Nuevo Cultivo Encontrado"
        )

    hass.helpers.dispatcher.async_dispatcher_connect(NEW_CULTIVO_SIGNAL, handle_new_cultivo_signal)
    return True
