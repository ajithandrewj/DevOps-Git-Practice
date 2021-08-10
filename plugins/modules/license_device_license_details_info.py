#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_device_license_details_info
short_description: Information module for License Device License Details
description:
- Get all License Device License Details.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_uuid:
    description:
    - Device_uuid path parameter. Id of device.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: License Device License Details reference
  description: Complete reference of the License Device License Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all License Device License Details
  cisco.dnac.license_device_license_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    device_uuid: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "device_uuid": "string",
        "site": "string",
        "model": "string",
        "license_mode": "string",
        "is_license_expired": true,
        "software_version": "string",
        "network_license": "string",
        "evaluation_license_expiry": "string",
        "device_name": "string",
        "device_type": "string",
        "dna_level": "string",
        "virtual_account_name": "string",
        "ip_address": "string",
        "mac_address": "string",
        "sntc_status": "string",
        "feature_license": [
          "string"
        ],
        "has_sup_cards": true,
        "udi": "string",
        "stacked_devices": [
          {
            "mac_address": "string",
            "id": "string",
            "role": "string",
            "serial_number": "string"
          }
        ],
        "is_stacked_device": true,
        "access_points": [
          {
            "ap_type": "string",
            "count": "string"
          }
        ],
        "chassis_details": {
          "board_serial_number": "string",
          "modules": [
            {
              "module_type": "string",
              "module_name": "string",
              "serial_number": "string",
              "id": "string"
            }
          ],
          "supervisor_cards": [
            {
              "serial_number": "string",
              "supervisor_card_type": "string",
              "status": "string"
            }
          ],
          "port": 0
        }
      }
    ]
"""