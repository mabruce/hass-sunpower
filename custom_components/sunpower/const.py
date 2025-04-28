"""Constants for the sunpower integration."""
from collections import namedtuple
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    EntityCategory,
    UnitOfApparentPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfInformation,
    UnitOfPower,
    UnitOfReactivePower,
    UnitOfTemperature,
    UnitOfTime,
)

DOMAIN = "sunpower"

SUNPOWER_DESCRIPTIVE_NAMES = "use_descriptive_names"
SUNPOWER_OBJECT = "sunpower"
SUNPOWER_HOST = "host"
SUNPOWER_COORDINATOR = "coordinator"
UPDATE_INTERVAL = 120
DEFAULT_SUNPOWER_UPDATE_INTERVAL = 120
MIN_SUNPOWER_UPDATE_INTERVAL = 60
SUNPOWER_UPDATE_INTERVAL = "PVS_UPDATE_INTERVAL"
SETUP_TIMEOUT_MIN = 5

PVS_DEVICE_TYPE = "PVS"
INVERTER_DEVICE_TYPE = "Inverter"
METER_DEVICE_TYPE = "Power Meter"

PVS_STATE = "STATE"

METER_STATE = "STATE"

INVERTER_STATE = "STATE"

WORKING_STATE = "working"


SensorConfig = namedtuple("SensorConfig", "field title unit icon device_class state_class")

METER_SENSORS = {
    "METER_FREQUENCY": SensorConfig(
        "freq_hz", "Frequency", UnitOfFrequency.HERTZ, "mdi:flash", None, SensorStateClass.MEASUREMENT
    ),
    "METER_NET_KWH": SensorConfig(
        "net_ltea_3phsum_kwh",
        "Lifetime Power",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "METER_KW": SensorConfig(
        "p_3phsum_kw", "Power", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "METER_VAR": SensorConfig(
        "q_3phsum_kvar", "UnitOfElectricPotential.VOLTReactive", UnitOfReactivePower.VOLT_AMPERE_REACTIVE, "mdi:flash", None, SensorStateClass.MEASUREMENT
    ),
    "METER_VA": SensorConfig(
        "s_3phsum_kva", "UnitOfElectricPotential.VOLTApparent", UnitOfApparentPower.VOLT_AMPERE, "mdi:flash", None, SensorStateClass.MEASUREMENT
    ),
    "METER_POWER_FACTOR": SensorConfig(
        "tot_pf_rto", "Power Factor", PERCENTAGE, "mdi:flash", SensorDeviceClass.POWER_FACTOR, SensorStateClass.MEASUREMENT
    ),
    "METER_L1_A": SensorConfig(
        "i1_a", "Leg 1 Amps", UnitOfElectricCurrent.AMPERE, "mdi:flash", SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT
    ),
    "METER_L2_A": SensorConfig(
        "i2_a", "Leg 2 Amps", UnitOfElectricCurrent.AMPERE, "mdi:flash", SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT
    ),
    "METER_L1_KW": SensorConfig(
        "p1_kw", "Leg 1 KW", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "METER_L2_KW": SensorConfig(
        "p2_kw", "Leg 2 KW", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "METER_L1_V": SensorConfig(
        "v1n_v", "Leg 1 Volts", UnitOfElectricPotential.VOLT, "mdi:flash", SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT
    ),
    "METER_L2_V": SensorConfig(
        "v2n_v", "Leg 2 Volts", UnitOfElectricPotential.VOLT, "mdi:flash", SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT
    ),
    "METER_L12_V": SensorConfig(
        "v12_v", "Supply Volts", UnitOfElectricPotential.VOLT, "mdi:flash", SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT
    ),
    "METER_TO_GRID": SensorConfig(
        "neg_ltea_3phsum_kwh",
        "KWH To Grid",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "METER_TO_HOME": SensorConfig(
        "pos_ltea_3phsum_kwh",
        "KWH To Home",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
}

INVERTER_SENSORS = {
    "INVERTER_NET_KWH": SensorConfig(
        "ltea_3phsum_kwh",
        "Lifetime Power",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "INVERTER_KW": SensorConfig(
        "p_3phsum_kw", "Power", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_VOLTS": SensorConfig(
        "vln_3phavg_v", "Voltage", UnitOfElectricPotential.VOLT, "mdi:flash", SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_AMPS": SensorConfig(
        "i_3phsum_a", "Amps", UnitOfElectricCurrent.AMPERE, "mdi:flash", SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_MPPT_KW": SensorConfig(
        "p_mpptsum_kw", "MPPT KW", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_MPPT1_KW": SensorConfig(
        "p_mppt1_kw", "MPPT KW", UnitOfPower.KILO_WATT, "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_MPPT_V": SensorConfig(
        "v_mppt1_v", "MPPT Volts", UnitOfElectricPotential.VOLT, "mdi:flash", SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_MPPT_A": SensorConfig(
        "i_mppt1_a", "MPPT Amps", POWER_VOLT_AMPERE, "mdi:flash", SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT
    ),
    "INVERTER_TEMPERATURE": SensorConfig(
        "t_htsnk_degc",
        "Temperature",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
    ),
    "INVERTER_FREQUENCY": SensorConfig(
        "freq_hz", "Frequency", UnitOfFrequency.HERTZ, "mdi:flash", None, SensorStateClass.MEASUREMENT
    ),
}


PVS_SENSORS = {
    "PVS_LOAD": SensorConfig("dl_cpu_load", "System Load", "", "mdi:gauge", None, SensorStateClass.MEASUREMENT),
    "PVS_ERROR_COUNT": SensorConfig("dl_err_count", "Error Count", "", "mdi:alert-circle", None, SensorStateClass.TOTAL),
    "PVS_COMMUNICATION_ERRORS": SensorConfig(
        "dl_comm_err", "Communication Errors", "", "mdi:network-off", None, SensorStateClass.TOTAL
    ),
    "PVS_SKIPPED_SCANS": SensorConfig(
        "dl_skipped_scans", "Skipped Scans", "", "mdi:network-strength-off-outline", None, SensorStateClass.TOTAL_INCREASING
    ),
    "PVS_SCAN_TIME": SensorConfig(
        "dl_scan_time", "Scan Time", UnitOfTime.SECONDS, "mdi:timer-outline", None, SensorStateClass.MEASUREMENT
    ),
    "PVS_UNTRANSMITTED": SensorConfig(
        "dl_untransmitted", "Untransmitted Data", "", "mdi:radio-tower", None, SensorStateClass.MEASUREMENT
    ),
    "PVS_UPTIME": SensorConfig(
        "dl_uptime", "Uptime", UnitOfTime.SECONDS, "mdi:timer-outline", None, SensorStateClass.TOTAL_INCREASING
    ),
    "PVS_MEMORY_USED": SensorConfig(
        "dl_mem_used", "Memory Used", UnitOfInformation.KILOBYTES, "mdi:memory", None, SensorStateClass.MEASUREMENT
    ),
    "PVS_FLASH_AVAILABLE": SensorConfig(
        "dl_flash_avail", "Flash Available", UnitOfInformation.KILOBYTES, "mdi:memory", None, SensorStateClass.MEASUREMENT
    ),
}

SENSOR_CONFIGS = {
    PVS_DEVICE_TYPE: PVS_SENSORS,
    INVERTER_DEVICE_TYPE: INVERTER_SENSORS,
    METER_DEVICE_TYPE: METER_SENSORS,
}

FIELD_ADAPTORS = {
    PVS_DEVICE_TYPE: {
        "dl_cpu_load": {"Avg CPU Load": "2.2.3", "AvgCPULoad": "2.2.2"},
        "dl_err_count": {"Error Count": "2.2.3"},
        "dl_comm_err": {"Communication Error Count": "2.2.3"},
        "dl_skipped_scans": {"Skipped Scans": "2.2.3"},
        "dl_scan_time": {"Scan Time": "2.2.3"},
        "dl_untransmitted": {"Untransmitted Data Points": "2.2.3"},
        "dl_uptime": {"Time Since Powerup": "2.2.3"},
        "dl_mem_used": {"Memory Used": "2.2.3"},
        "dl_flash_avail": {"Flash Space Available": "2.2.3"},
        "SERIAL": {"Serial Number": "2.2.3"},
        "SWVER": {"Software Version": "2.2.3"},
        "HWVER": {"Hardware Version": "2.2.3"},
        "MODEL": {"Model": "2.2.3"},
    },
    INVERTER_DEVICE_TYPE: {
        "ltea_3phsum_kwh": {"Total Lifetime Energy": "2.2.3"},
        "p_3phsum_kw": {"Avg DC Power": "2.2.3"},
        "vln_3phavg_v": {"Avg DC Voltage": "2.2.3"},
        "i_3phsum_a": {"Avg DC Amps": "2.2.3"},
        "p_mpptsum_kw": {},  # MPPT Cumulative kW
        "p_mppt1_kw": {},  # MPPT kW
        "v_mppt1_v": {},  # MPPT Voltage
        "i_mppt1_a": {},  # MPPT Current
        "t_htsnk_degc": {"Avg Heat Sink Temperature": "2.2.3"},
        "freq_hz": {"Avg AC Frequency": "2.2.3"},
        "SERIAL": {"Serial Number": "2.2.3"},
        "DESCR": {"": "2.2.3"},
        "TYPE": {"": "2.2.3"},
        "MODEL": {"Model": "2.2.3"},
        "SWVER": {"Software Version": "2.2.3"},
    },
    METER_DEVICE_TYPE: {
        "freq_hz": {"Avg AC Frequency": "2.2.3"},  # Frequency
        "net_ltea_3phsum_kwh": {"Total Lifetime Energy": "2.2.3"},  # Lifetime Energy
        "p_3phsum_kw": {"Avg Real Power": "2.2.3"},  # "Power"
        "q_3phsum_kvar": {"Avg Reactive Power": "2.2.3"},  # "UnitOfElectricPotential.VOLTReactive"
        "s_3phsum_kva": {"Avg Apparent Power": "2.2.3"},  # "UnitOfElectricPotential.VOLTApparent"
        "tot_pf_rto": {"Avg Power Factor": "2.2.3"},  # "Power Factor"
        "i1_a": {},  # "Leg 1 Amps"
        "i2_a": {},  # "Leg 2 Amps"
        "p1_kw": {},  # "Leg 1 KW"
        "p2_kw": {},  # "Leg 2 KW"
        "v1n_v": {},  # "Leg 1 Volts"
        "v2n_v": {},  # "Leg 2 Volts"
        "v12_v": {},  # "Supply Volts"
        "neg_ltea_3phsum_kwh": {},  # "KWH To Grid"
        "pos_ltea_3phsum_kwh": {},  # "KWH To Home"
        "SERIAL": {"Serial Number": "2.2.3"},
        "DESCR": {"": "2.2.3"},
        "MODEL": {"Model": "2.2.3"},
        "SWVER": {"Software Version": "2.2.3"},
    },
}
