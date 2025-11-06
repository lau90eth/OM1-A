from dataclasses import dataclass, field
from enum import Enum

from pycdr2 import IdlStruct
from pycdr2.types import int8

from .std_msgs import Header


@dataclass
class AudioStatus(IdlStruct, typename="AudioStatus"):
    class STATUS_MIC(Enum):
        DISABLED = 0
        READY = 1
        ACTIVE = 2
        UNKNOWN = 3

    class STATUS_SPEAKER(Enum):
        DISABLED = 0
        READY = 1
        ACTIVE = 2
        UNKNOWN = 3

    header: Header
    mic_status: int8 = 0
    speaker_status: int8 = 0
    mode: str = field(default_factory=lambda: "unknown")

@dataclass
class AIStatusRequest(IdlStruct, typename="AIStatusRequest"):
    header: Header
    request_type: str = field(default_factory=lambda: "status")

@dataclass
class AIStatusResponse(IdlStruct, typename="AIStatusResponse"):
    header: Header
    status: str = field(default_factory=lambda: "ok")
    message: str = field(default_factory=lambda: "")

@dataclass
class CameraStatus(IdlStruct, typename="CameraStatus"):
    header: Header
    fps: float = 0.0
    resolution: str = field(default_factory=lambda: "unknown")
    status: str = field(default_factory=lambda: "unknown")

@dataclass
class ModeStatusRequest(IdlStruct, typename="ModeStatusRequest"):
    header: Header
    mode: str = field(default_factory=lambda: "unknown")

@dataclass
class ModeStatusResponse(IdlStruct, typename="ModeStatusResponse"):
    header: Header
    current_mode: str = field(default_factory=lambda: "unknown")
    status: str = field(default_factory=lambda: "ok")