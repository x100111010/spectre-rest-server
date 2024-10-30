import os

NETWORK_TYPE = os.getenv("NETWORK_TYPE", "mainnet").lower()

match NETWORK_TYPE:
    case "mainnet":
        address_prefix = "spectre"
        address_example = "spectre:qz33fqskc6m3z50klk38vhj48ycaacl7fdzlz3r6nfckekvzhp44geacqff3u"
    case "testnet":
        address_prefix = "spectretest"
        address_example = "spectretest:qz72rp20attcv6vg76fge75hdaj5ytmzkpw8qhqwvg8e3lrvwe8zyp9u37wuh"
    case "simnet":
        address_prefix = "spectresim"
        address_example = "spectresim:qp9mpcdw89k7vwsfs50d6jzdlzr9z64nlphf9utpnlm4gk2zj8mu2rfhnp7w0"
    case "devnet":
        address_prefix = "spectredev"
        address_example = "spectredev:qr4gvwyh7mlgu0smt5ef56xxm6u9w69kd3wupddmecpuger0h30770c9k6hqn"
    case _:
        raise ValueError(f"Network type {NETWORK_TYPE} not supported.")

ADDRESS_PREFIX = address_prefix
ADDRESS_EXAMPLE = address_example

REGEX_SPECTRE_ADDRESS = "^" + ADDRESS_PREFIX + ":[a-z0-9]{61,63}$"
