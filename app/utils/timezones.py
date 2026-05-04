from enum import Enum

class ALLOWED_ISO_ENUM(str, Enum):
    CO="CO",
    MX="MX",
    AR="AR",
    CL="CL",
    PE="PE",
    VE="VE",
    EC="EC",
    UY="UY",
    PY="PY",
    BO="BO"

tz_by_iso = {
    "CO":"America/Bogota",
    "MX":"America/Mexico_City",
    "AR":"America/Argentina/Buenos_Aires",
    "CL":"America/Santiago",
    "PE":"America/Lima",
    "VE":"America/Caracas",
    "EC":"America/Guayaquil",
    "UY":"America/Montevideo",
    "PY":"America/Asuncion",
    "BO":"America/La_Paz",
}