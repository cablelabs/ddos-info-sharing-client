# Right now, this class is the same as the ObjectTypes class in CRITs, except it doesn't inherit from anything.


class ObjectTypes:
    """
    Vocabulary for Object Types.
    """


    ADJUST_TOKEN = "Adjust Token"
    AGGREGATE_BYTES_PER_SECOND = "Aggregate Bytes per Second"
    AGGREGATE_PACKETS_PER_SECOND = "Aggregate Packets per Second"
    API_KEY = "API Key"
    AS_NUMBER = "AS Number"
    AS_NAME = "AS Name"
    ATTACK_START_TIME = "Attack Start Time"
    ATTACK_STOP_TIME = "Attack Stop Time"
    ATTACK_TYPE = "Attack Type"
    BANK_ACCOUNT = "Bank account"
    BASE64_ALPHA = "Base64 Alphabet"
    BITCOIN_ACCOUNT = "Bitcoin account"
    C2_URL = "C2 URL"
    CERTIFICATE_FINGERPRINT = "Certificate Fingerprint"
    CERTIFICATE_NAME = "Certificate Name"
    CHECKSUM_CRC16 = "Checksum CRC16"
    CITY = "City"
    CMD_LINE = "Command Line"
    COOKIE_NAME = "Cookie Name"
    COMPANY_NAME = "Company name"
    COUNTRY = "Country"
    CRX = "CRX"
    DEBUG_PATH = "Debug Path"
    DEBUG_STRING = "Debug String"
    DEST_PORT = "Destination Port"
    DEVICE_IO = "Device IO"
    DOC_FROM_URL = "Document from URL"
    DOCUMENT_METADATA = "Document Metadata"
    DOMAIN = "Domain"
    EMAIL_BOUNDARY = "Email Boundary"
    EMAIL_ADDRESS = "Email Address"
    EMAIL_FROM = "Email Address From"
    EMAIL_HEADER_FIELD = "Email Header Field"
    EMAIL_HELO = "Email HELO"
    EMAIL_MESSAGE_ID = "Email Message ID"
    EMAIL_ORIGINATING_IP = "Email Originating IP"
    EMAIL_REPLY_TO = "Email Reply-To"
    EMAIL_SENDER = "Email Address Sender"
    EMAIL_SUBJECT = "Email Subject"
    EMAIL_X_MAILER = "Email X-Mailer"
    EMAIL_X_ORIGINATING_IP = "Email X-Originating IP"
    ENCRYPTION_KEY = "Encryption Key"
    EXTRA = "Extra"
    FILE_CREATED = "File Created"
    FILE_DELETED = "File Deleted"
    FILE_MOVED = "File Moved"
    FILE_NAME = "File Name"
    FILE_OPENED = "File Opened"
    FILE_PATH = "File Path"
    FILE_READ = "File Read"
    FILE_WRITTEN = "File Written"
    FILE_UPLOAD = "File Upload" # Used to upload a file to CRITs!
    GET_PARAM = "GET Parameter"
    HEX_STRING = "HEX String"
    HTML_ID = "HTML ID"
    HTTP_REQUEST = "HTTP Request"
    HTTP_RESP_CODE = "HTTP Response Code"
    IMPHASH = "IMPHASH"
    IPV4_ADDRESS = "IPv4 Address"
    IPV4_SUBNET = "IPv4 Subnet"
    IPV6_ADDRESS = "IPv6 Address"
    IPV6_SUBNET = "IPv6 Subnet"
    LAST_TIME_RECEIVED = "Last Time Received"
    LATITUDE = "Latitude"
    LAUNCH_AGENT = "Launch Agent"
    LOCATION = "Location"
    LONGITUDE = "Longitude"
    MAC_ADDRESS = "MAC Address"
    MALWARE_NAME = "Malware Name"
    MD5 = "MD5"
    MEMORY_ALLOC = "Memory Alloc"
    MEMORY_PROTECT = "Memory Protect"
    MEMORY_READ = "Memory Read"
    MEMORY_WRITTEN = "Memory Written"
    MUTANT_CREATED = "Mutant Created"
    MUTEX = "Mutex"
    NAME_SERVER = "Name Server"
    NUMBER_OF_REPORTERS = "Number of Reporters"
    NUMBER_OF_TIMES_SEEN = "Number of Times Seen"
    OTHER_FILE_OP = "Other File Operation"
    PASSWORD = "Password"
    PASSWORD_SALT = "Password Salt"
    PAYLOAD_DATA = "Payload Data"
    PAYLOAD_TYPE = "Payload Type"
    PEAK_BYTES_PER_SECOND = "Peak Bytes per Second"
    PEAK_PACKETS_PER_SECOND = "Peak Packets per Second"
    PIPE = "Pipe"
    PIVY_GROUP_NAME = "PIVY Group Name"
    PIVY_PASSWORD = "PIVY Password"
    POST_DATA = "POST Data"
    PROCESS_NAME = "Process Name"
    PROTOCOL = "Protocol"
    RC4_KEY = "RC4 Key"
    REFERER = "Referer"
    REFERER_OF_REFERER = "Referer of Referer"
    REGISTRAR = "Registrar"
    REGISTRY_KEY = "Registry Key"
    REG_KEY_CREATED = "Registry Key Created"
    REG_KEY_DELETED = "Registry Key Deleted"
    REG_KEY_ENUMERATED = "Registry Key Enumerated"
    REG_KEY_MONITORED = "Registry Key Monitored"
    REG_KEY_OPENED = "Registry Key Opened"
    REG_KEY_VALUE_CREATED = "Registry Key Value Created"
    REG_KEY_VALUE_DELETED = "Registry Key Value Deleted"
    REG_KEY_VALUE_MODIFIED = "Registry Key Value Modified"
    REG_KEY_VALUE_QUERIED = "Registry Key Value Queried"
    REPORTED_BY = "Reported By"
    SERVICE_NAME = "Service Name"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SMS_ORIGIN = "SMS Origin"
    SOURCE_PORT = "Source Port"
    SSDEEP = "SSDEEP"
    STATE = "State"
    STRING = "String"
    TELEPHONE = "Telephone"
    TIMESTAMP = "Timestamp"
    TIME_CREATED = "Time Created"
    TIME_FIRST_SEEN = "Time First Seen"
    TIME_LAST_SEEN = "Time Last Seen"
    TIME_UPDATED = "Time Updated"
    TOTAL_BYTES_SENT = "Total Bytes Sent"
    TOTAL_PACKETS_SENT = "Total Packets Sent"
    TRACKING_ID = "Tracking ID"
    TS_END = "TS End"
    TS_START = "TS Start"
    URI = "URI"
    USER_AGENT = "User Agent"
    USER_ID = "User ID"
    VICTIM_IP = "Victim IP"
    VOLUME_QUERIED = "Volume Queried"
    WEBSTORAGE_KEY = "Webstorage Key"
    WEB_PAYLOAD = "Web Payload"
    WHOIS_NAME = "WHOIS Name"
    WHOIS_ADDR1 = "WHOIS Address 1"
    WHOIS_ADDR2 = "WHOIS Address 2"
    WHOIS_REGISTRANT_EMAIL_ADDRESS = "WHOIS Registrant Email Address"
    XPI = "XPI"