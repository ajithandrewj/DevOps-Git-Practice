#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_smart_account_details_info
short_description: Information module for License Smart Account Details
description:
- Get all License Smart Account Details.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: License Smart Account Details reference
  description: Complete reference of the License Smart Account Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all License Smart Account Details
  cisco.dnac.license_smart_account_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "name": "string",
          "id": "string",
          "domain": "string",
          "is_active_smart_account": true
        }
      ],
      "version": "string"
    }
"""