#!/usr/bin/env python3
"""
Test the certificate

@authors: Roman Yasinovskyy
@version: 2025.12
"""

import pathlib
import ssl
import subprocess

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID


def test_certificate_file_permissions() -> None:
    """Check cert file permissions

    Must be rw-r--r--
    :url: https://stackoverflow.com/questions/35375084/c-unix-how-to-extract-the-bits-from-st-mode
    """
    cert_file = "exercises/authorization/panda/ssl/certs/selfsigned330.crt"
    assert pathlib.Path(cert_file).stat().st_mode == 0o100644


def test_certificate_content() -> None:
    """Check cert data"""
    expected_cert_attributes = {
        NameOID.COUNTRY_NAME: "US",
        NameOID.STATE_OR_PROVINCE_NAME: "Iowa",
        NameOID.LOCALITY_NAME: "Decorah",
        NameOID.ORGANIZATION_NAME: "CS330",
        NameOID.ORGANIZATIONAL_UNIT_NAME: "2025FA",
        NameOID.COMMON_NAME: "Norse Panda",
        NameOID.EMAIL_ADDRESS: "panda@example.com",
    }
    cert_file = "exercises/authorization/panda/ssl/certs/selfsigned330.crt"
    with open(cert_file) as f:
        cert_dict = x509.load_pem_x509_certificate(f.read().encode(), default_backend())
    for attrib, expected_value in expected_cert_attributes.items():
        assert cert_dict.issuer.get_attributes_for_oid(attrib)[0].value == expected_value


def test_certificate_text() -> None:
    """Check cert data using openssl

    Relies on text parsing
    :url: https://stackoverflow.com/questions/16899247/how-can-i-decode-a-ssl-certificate-using-python
    """
    cert_file = "exercises/authorization/panda/ssl/certs/selfsigned330.crt"
    cert_txt = subprocess.check_output(["openssl", "x509", "-text", "-noout", "-in", cert_file])
    cert_issuer = {
        item.split(" = ")[0].strip(): item.split(" = ")[1]
        for item in cert_txt.decode(encoding="utf-8").split("\n")[6].strip()[7:].split(",")
    }
    assert {
        "C": "US",
        "ST": "Iowa",
        "L": "Decorah",
        "O": "CS330",
        "OU": "2025FA",
    }.items() <= cert_issuer.items()


@pytest.mark.skip(reason="Undocumented functionality of ssl")
def test_certificate_content_hack() -> None:
    """Check cert data
    Relies on an undocumented functionality

    :url: https://stackoverflow.com/questions/16899247/how-can-i-decode-a-ssl-certificate-using-python
    """
    cert_file = "exercises/authorization/panda/ssl/certs/selfsigned330.crt"
    cert_dict = ssl._ssl._test_decode_cert(cert_file)
    assert cert_dict["issuer"][0][0] == ("countryName", "US")
    assert cert_dict["issuer"][1][0] == ("stateOrProvinceName", "Iowa")
    assert cert_dict["issuer"][2][0] == ("localityName", "Decorah")
    assert cert_dict["issuer"][3][0] == ("organizationName", "CS330")
    assert cert_dict["issuer"][4][0] == ("organizationalUnitName", "2025FA")
    assert cert_dict["issuer"][5][0] == ("commonName", "Norse Panda")
    assert cert_dict["issuer"][6][0] == ("emailAddress", "panda@example.com")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
