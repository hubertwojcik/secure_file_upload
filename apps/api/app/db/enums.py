import enum

class FileStatus(str, enum.Enum):
    PENDING_SCAN = "PENDING_SCAN"
    CLEAN = "CLEAN"
    MALICIOUS = "MALICIOUS"
    ERROR = "ERROR"
