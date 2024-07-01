# Home Assistant Integration - Avisos Fitosanitarios

Esta es una integración para Home Assistant que recopila y muestra avisos fitosanitarios emitidos por la Generalitat de Catalunya. La integración permite configurar qué categorías y cultivos deseas monitorizar y muestra los avisos en Lovelace.

## Características

- Recoge y muestra avisos fitosanitarios de la Generalitat de Catalunya.
- Configuración fácil a través de la interfaz de usuario de Home Assistant.
- Notificaciones sobre nuevos cultivos encontrados en los avisos.
- Incluye una tarjeta Lovelace predefinida para mostrar los avisos.

La información extraída de los avisos procede del Departament d´Acció Climàtica, Alimentació i Agenda rural: https://agricultura.gencat.cat/ca/ambits/agricultura/dar_sanitat_vegetal_nou/avisos-fitosanitaris/

## Requerimientos

En el caso de uso de la integración con OpenAI para la extracción de información de los boletines necesitarás tener a mano tu información para la API de ChatGPT.

También necesitas tener la instancia de HACS funcionando en tu Home Assistant

## Instalación

### 1. Instalar mediante HACS

1. Abre Home Assistant y ve a HACS.
2. Selecciona "Integrations" y luego "Custom repositories".
3. Añade la URL de tu repositorio de GitHub: `https://github.com/vmasmitja/ha_avisos_fitosanitarios`.
4. Selecciona "Integration" como categoría y haz clic en "Add".
5. Busca `ha_avisos_fitosanitarios` y selecciona la integración.
6. Haz clic en "Install".

### 2. Configurar la Integración

1. Ve a "Configuración" en Home Assistant.
2. Selecciona "Dispositivos e Integraciones" y busca `Avisos Fitosanitarios`.
3. Haz clic en "Configurar" y sigue las instrucciones para configurar las categorías y cultivos de interés.

### 3. Añadir la Tarjeta Lovelace

1. Ve a tu panel de control de Lovelace en Home Assistant.
2. Añade la tarjeta usando el contenido de `lovelace.yaml`:

```yaml
title: Avisos Fitosanitarios
views:
  - title: Avisos
    cards:
      - type: entities
        title: Avisos Leñosos
        entities:
          - sensor.avisos_fitosanitarios_leñosos_viña_vinya_vitis_vinifera
          - sensor.avisos_fitosanitarios_leñosos_olivo_olivera_olea_europaea
          - sensor.avisos_fitosanitarios_leñosos_almendro_ametller_prunus_dulcis
      - type: entities
        title: Avisos Hortícolas
        entities:
          - sensor.avisos_fitosanitarios_hortícolas_tomate_tomàquet_solanum_lycopersicum
          - sensor.avisos_fitosanitarios_hortícolas_pimiento_pebroter_capsicum_annuum
          - sensor.avisos_fitosanitarios_hortícolas_calabacín_carbassó_cucurbita_pepo
          - sensor.avisos_fitosanitarios_hortícolas_judía_verde_mongeta_phaseolus_vulgaris
          - sensor.avisos_fitosanitarios_hortícolas_puerro_porro_allium_ampeloprasum_var_porrum
          - sensor.avisos_fitosanitarios_hortícolas_col_brassica_oleracea_var_capitata
          - sensor.avisos_fitosanitarios_hortícolas_coliflor_brassica_oleracea_var_botrytis
          - sensor.avisos_fitosanitarios_hortícolas_patata_solanum_tuberosum
          - sensor.avisos_fitosanitarios_hortícolas_fresa_maduixa_fragaria_x_ananassa
      - type: entities
        title: Avisos Extensivos
        entities:
          - sensor.avisos_fitosanitarios_extensivos_maíz_blat_de_moro_zea_mays
          - sensor.avisos_fitosanitarios_extensivos_girasol_gira_sol_helianthus_annuus
          - sensor.avisos_fitosanitarios_extensivos_trigo_blat_triticum_spp
      - type: entities
        title: Avisos Espacios Verdes
        entities:
          - sensor.avisos_fitosanitarios_espacios_verdes_plátano_de_sombra_plataner_platanus_x_hispanica
          - sensor.avisos_fitosanitarios_espacios_verdes_césped_gespa_poaceae
```
## Contribución

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
