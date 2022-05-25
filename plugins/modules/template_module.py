#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = (
            "Madhan Sankaranarayanan, Rishita Chowdhary"
            )

DOCUMENTATION = r"""
---
module: template_module
short_description: Resource module for Template functions
description:
- Manage operations create, update, query and delete of the resource Configuration Template.
- API to create a template by project name and template name.
- API to update a template by template name and project name.
- API to query a template by template name and project name.
- API to delete a template by template name and project name.
version_added: '6.4.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rishita Chowdhary (@rischowd)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices:
      - merged
      - deleted
      - query
    default: merged
  config:
    description:
    - List of details of templates being managed. 
    type: list
    elements: dict
    suboptions:
      author:
        description: Author of template.
        type: str
      composite:
        description: Is it composite template.
        type: bool
      containingTemplates:
        description: Configuration Template Create's containingTemplates.
        suboptions:
          composite:
            description: Is it composite template.
            type: bool
          description:
            description: Description of template.
            type: str
          deviceTypes:
            description: Configuration Template Create's deviceTypes.
            type: list
            elements: dict
            suboptions:
              productFamily:
                description: Device family.
                type: str
              productSeries:
                description: Device series.
                type: str
              productType:
                description: Device type.
                type: str
          id:
            description: UUID of template.
            type: str
          language:
            description: Template language
            choices:
              - JINJA
              - VELOCITY
            type: str
          name:
            description: Name of template.
            type: str
          projectName:
            description: Project name.
            type: str
          rollbackTemplateParams:
            description: Configuration Template Create's rollbackTemplateParams.
            type: list
            elements: dict
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
                type: list
                elements: dict
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                      elements: str
                      type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
          tags:
            description: Configuration Template Create's tags.
            suboptions:
              id:
                description: UUID of tag.
                type: str
              name:
                description: Name of tag.
                type: str
            type: list
            elements: dict
          templateContent:
            description: Template content.
            type: str
          templateParams:
            description: Configuration Template Create's templateParams.
            suboptions:
              binding:
                description: Bind to source.
                type: str
              customOrder:
                description: CustomOrder of template param.
                type: int
              dataType:
                description: Datatype of template param.
                type: str
              defaultValue:
                description: Default value of template param.
                type: str
              description:
                description: Description of template param.
                type: str
              displayName:
                description: Display name of param.
                type: str
              group:
                description: Group.
                type: str
              id:
                description: UUID of template param.
                type: str
              instructionText:
                description: Instruction text for param.
                type: str
              key:
                description: Key.
                type: str
              notParam:
                description: Is it not a variable.
                type: bool
              order:
                description: Order of template param.
                type: int
              paramArray:
                description: Is it an array.
                type: bool
              parameterName:
                description: Name of template param.
                type: str
              provider:
                description: Provider.
                type: str
              range:
                description: Configuration Template Create's range.
                suboptions:
                  id:
                    description: UUID of range.
                    type: str
                  maxValue:
                    description: Max value of range.
                    type: int
                  minValue:
                    description: Min value of range.
                    type: int
                type: list
                elements: dict
              required:
                description: Is param required.
                type: bool
              selection:
                description: Configuration Template Create's selection.
                suboptions:
                  defaultSelectedValues:
                    description: Default selection values.
                    elements: str
                    type: list
                  id:
                    description: UUID of selection.
                    type: str
                  selectionType:
                    description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                    type: str
                  selectionValues:
                    description: Selection values.
                    type: dict
                type: dict
            type: list
          version:
            description: Current version of template.
            type: str
        type: list
        elements: dict
      createTime:
        description: Create time of template.
        type: int
      customParamsOrder:
        description: Custom Params Order.
        type: bool
      template_description:
        description: Description of template.
        type: str
      device_types:
        description: Configuration Template Create's deviceTypes.
        suboptions:
          productFamily:
            description: Device family.
            type: str
          productSeries:
            description: Device series.
            type: str
          productType:
            description: Device type.
            type: str
        type: list
        elements: dict
      failurePolicy:
        description: Define failure policy if template provisioning fails.
        type: str
      language:
        description: Template language
        choices:
          - JINJA
          - VELOCITY
        type: str
      lastUpdateTime:
        description: Update time of template.
        type: int
      latestVersionTime:
        description: Latest versioned template time.
        type: int
      template_name:
        description: Name of template.
        type: str
      parentTemplateId:
        description: Parent templateID.
        type: str
      projectId:
        description: Project UUID.
        type: str
      project_name:
        description: Project name.
        type: str
      rollbackTemplateContent:
        description: Rollback template content.
        type: str
      rollbackTemplateParams:
        description: Configuration Template Create's rollbackTemplateParams.
        suboptions:
          binding:
            description: Bind to source.
            type: str
          customOrder:
            description: CustomOrder of template param.
            type: int
          dataType:
            description: Datatype of template param.
            type: str
          defaultValue:
            description: Default value of template param.
            type: str
          description:
            description: Description of template param.
            type: str
          displayName:
            description: Display name of param.
            type: str
          group:
            description: Group.
            type: str
          id:
            description: UUID of template param.
            type: str
          instructionText:
            description: Instruction text for param.
            type: str
          key:
            description: Key.
            type: str
          notParam:
            description: Is it not a variable.
            type: bool
          order:
            description: Order of template param.
            type: int
          paramArray:
            description: Is it an array.
            type: bool
          parameterName:
            description: Name of template param.
            type: str
          provider:
            description: Provider.
            type: str
          range:
            description: Configuration Template Create's range.
            suboptions:
              id:
                description: UUID of range.
                type: str
              maxValue:
                description: Max value of range.
                type: int
              minValue:
                description: Min value of range.
                type: int
            type: list
            elements: dict
          required:
            description: Is param required.
            type: bool
          selection:
            description: Configuration Template Create's selection.
            suboptions:
              defaultSelectedValues:
                description: Default selection values.
                elements: str
                type: list
              id:
                description: UUID of selection.
                type: str
              selectionType:
                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                type: str
              selectionValues:
                description: Selection values.
                type: dict
            type: dict
        type: list
        elements: dict
      software_type:
        description: Applicable device software type.
        type: str
      software_variant:
        description: Applicable device software variant.
        type: str
      softwareVersion:
        description: Applicable device software version.
        type: str
      template_tag:
        description: Configuration Template Create's tags.
        suboptions:
          id:
            description: UUID of tag.
            type: str
          name:
            description: Name of tag.
            type: str
        type: list
        elements: dict
      template_content:
        description: Template content.
        type: str
      templateParams:
        description: Configuration Template Create's templateParams.
        suboptions:
          binding:
            description: Bind to source.
            type: str
          customOrder:
            description: CustomOrder of template param.
            type: int
          dataType:
            description: Datatype of template param.
            type: str
          defaultValue:
            description: Default value of template param.
            type: str
          description:
            description: Description of template param.
            type: str
          displayName:
            description: Display name of param.
            type: str
          group:
            description: Group.
            type: str
          id:
            description: UUID of template param.
            type: str
          instructionText:
            description: Instruction text for param.
            type: str
          key:
            description: Key.
            type: str
          notParam:
            description: Is it not a variable.
            type: bool
          order:
            description: Order of template param.
            type: int
          paramArray:
            description: Is it an array.
            type: bool
          parameterName:
            description: Name of template param.
            type: str
          provider:
            description: Provider.
            type: str
          range:
            description: Configuration Template Create's range.
            suboptions:
              id:
                description: UUID of range.
                type: str
              maxValue:
                description: Max value of range.
                type: int
              minValue:
                description: Min value of range.
                type: int
            type: list
            elements: dict
          required:
            description: Is param required.
            type: bool
          selection:
            description: Configuration Template Create's selection.
            suboptions:
              defaultSelectedValues:
                description: Default selection values.
                elements: str
                type: list
              id:
                description: UUID of selection.
                type: str
              selectionType:
                description: Type of selection(SINGLE_SELECT or MULTI_SELECT).
                type: str
              selectionValues:
                description: Selection values.
                type: dict
            type: dict
        type: list
        elements: dict
      validationErrors:
        description: Configuration Template Create's validationErrors.
        suboptions:
          rollbackTemplateErrors:
            description: Validation or design conflicts errors of rollback template.
            elements: dict
            type: list
          templateErrors:
            description: Validation or design conflicts errors.
            elements: dict
            type: list
          templateId:
            description: UUID of template.
            type: str
          templateVersion:
            description: Current version of template.
            type: str
        type: dict
      version:
        description: Current version of template.
        type: str
      version_description:
        description: Template version comments.
       type: str
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template,
    configuration_templates.ConfigurationTemplates.deletes_the_template,
    configuration_templates.ConfigurationTemplates.update_template,
    configuration_templates.ConfigurationTemplates.get_template_details,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/project/{projectId}/template,
    delete /dna/intent/api/v1/template-programmer/template/{templateId},
    put /dna/intent/api/v1/template-programmer/template,
    get /dna/intent/api/v1/template-programmer/template/{templateId},

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.template_module:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        author: string
        composite: true
        createTime: 0
        customParamsOrder: true
        description: string
        deviceTypes:
        - productFamily: string
          productSeries: string
          productType: string
        failurePolicy: string
        id: string
        language: string
        lastUpdateTime: 0
        latestVersionTime: 0
        name: string
        parentTemplateId: string
        projectId: string
        projectName: string
        rollbackTemplateContent: string
        softwareType: string
        softwareVariant: string
        softwareVersion: string
        tags:
        - id: string
          name: string
        templateContent: string
        validationErrors:
            rollbackTemplateErrors:
            - {}
            templateErrors:
            - {}
            templateId: string
            templateVersion: string
        version: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
			"endTime": 0, 
			"version": 0, 
			"data": String, 
			"startTime": 0, 
			"username": String, 
			"progress": String, 
			"serviceType": String, "rootId": String, 
			"isError": bool, 
			"instanceTenantId": String, 
			"id": String
		}, 
		"version": 0
    }
"""

import copy
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
    validate_list_of_dicts,
    log,
    get_dict_result,
    dnac_compare_equality,
)
from ansible.module_utils.basic import AnsibleModule

class DnacTemplate:

    def __init__(self, module):
        self.module = module
        self.params = module.params
        self.config = copy.deepcopy(module.params.get("config"))
        self.have_create = {} 
        self.want_create = {} 
        self.diff_create = []
        self.validated = []
        dnac_params = self.get_dnac_params(self.params)
        log(str(dnac_params))
        self.dnac = DNACSDK(params=dnac_params)
        self.log = dnac_params.get("dnac_log")

        self.result = dict(changed=False, diff=[], response=[], warnings=[])


    def get_state(self):
        return self.params.get("state")


    def validate_input(self):
        temp_spec = dict(
            project_name=dict(required=True, type='str'),
            template_content=dict(required=False, type='str'),
            language=dict(required=False, choices=['velocity', 'jinja']),
            device_types=dict(required=False, type='list', elements='dict'),
            software_type=dict(required=False, type='str'),
            software_variant=dict(required=False, type='str'),
            version_description=dict(required=False, type='str'),
            template_name=dict(required=True, type='str'),
            )

        if self.config:
            msg = None
            # Validate template params
            valid_temp, invalid_params = validate_list_of_dicts(
                self.config, temp_spec
            )

            if invalid_params:
                msg = "Invalid parameters in playbook: {0}".format(
                    "\n".join(invalid_params)
                )
                self.module.fail_json(msg=msg)

            self.validated = valid_temp

            if self.log:
                log(str(valid_temp))
                log(str(self.validated))

            if self.params.get("state") == "merged":
                for temp in self.validated:
                    if not temp.get("language") or not temp.get("device_types") \
                            or not temp.get("software_type"):
                        msg = "missing required arguments: language or deviceTypes or softwareType"
                        self.module.fail_json(msg=msg)


    def get_dnac_params(self, params):
        dnac_params = dict(
            dnac_host=params.get("dnac_host"),
            dnac_port=params.get("dnac_port"),
            dnac_username=params.get("dnac_username"),
            dnac_password=params.get("dnac_password"),
            dnac_verify=params.get("dnac_verify"),
            dnac_debug=params.get("dnac_debug"),
            dnac_log=params.get("dnac_log")
        )
        return dnac_params


    def get_template_params(self, params):
        temp_params = dict(
            tags=params.get("template_tag"),
            author=params.get("author"),
            composite=params.get("composite"),
            containingTemplates=params.get("containingTemplates"),
            createTime=params.get("createTime"),
            customParamsOrder=params.get("customParamsOrder"),
            description=params.get("template_description"),
            deviceTypes=params.get("device_types"),
            failurePolicy=params.get("failurePolicy"),
            id=params.get("templateId"),
            language=params.get("language").upper(),
            lastUpdateTime=params.get("lastUpdateTime"),
            latestVersionTime=params.get("latestVersionTime"),
            name=params.get("template_name"),
            parentTemplateId=params.get("parentTemplateId"),
            projectId=params.get("projectId"),
            projectName=params.get("project_name"),
            rollbackTemplateContent=params.get("rollbackTemplateContent"),
            rollbackTemplateParams=params.get("rollbackTemplateParams"),
            softwareType=params.get("software_type"),
            softwareVariant=params.get("software_variant"),
            softwareVersion=params.get("softwareVersion"),
            templateContent=params.get("template_content"),
            templateParams=params.get("templateParams"),
            validationErrors=params.get("validationErrors"),
            version=params.get("version"),
            project_id=params.get("projectId"),
        )
        return temp_params


    def get_template(self):
        result = None

        for temp in self.validated:
            items = self.dnac.exec(
                family="configuration_templates",
                function="get_template_details",
                params={"template_id": temp.get("templateId")}
            )

            if items:
                result = items

                if self.log:
                    log(str(items))

        self.result['response'] = items 
        return result


    def get_have(self):
        prev_template = None
        template_exists = False
        have_create = {}

        #Get available templates. Filter templates based on provided projectName
        for temp in self.validated:
            template_list = self.dnac.exec(
                family="configuration_templates",
                function='gets_the_templates_available',
                params={"project_names":temp.get("project_name")},
            )
            #API execution error returns a dict
            if template_list and isinstance(template_list, list):
                template_details = get_dict_result(template_list, 'name', temp.get("template_name"))

                if template_details:
                    temp["templateId"] = template_details.get("templateId")
                    have_create["templateId"] = template_details.get("templateId")
                    prev_template = self.get_template()

                    if self.log:
                        log(str(prev_template))

                template_exists = prev_template is not None and isinstance(prev_template, dict)
            else:
                self.module.fail_json(msg="Project Not Found")

        have_create['template'] = prev_template
        have_create['template_found'] = template_exists
        self.have_create = have_create

    def get_want(self):
        want_create = {}

        for temp in self.validated:
            template_params = self.get_template_params(temp)
            version_comments = temp.get("version_description")

            if self.params.get("state") == "merged" and \
                    not self.have_create.get("template_found"):
                #ProjectId is required for creating a new template.
                #Store it with other template parameters.
                items = self.dnac.exec(
                    family="configuration_templates",
                    function='get_projects',
                    params={"name":temp.get("project_name")},
                )
                template_params["projectId"] = items[0].get("id")
                template_params["project_id"] = items[0].get("id")

        want_create["template_params"] = template_params
        want_create["comments"] = version_comments

        self.want_create = want_create


    def requires_update(self):
        current_obj = self.have_create.get("template")
        requested_obj = self.want_create.get("template_params")
        obj_params = [
            ("tags", "tags", ""),
            ("author", "author", ""),
            ("composite", "composite", False),
            ("containingTemplates", "containingTemplates", []),
            ("createTime", "createTime", ""),
            ("customParamsOrder", "customParamsOrder", False),
            ("description", "description", ""),
            ("deviceTypes", "deviceTypes", []),
            ("failurePolicy", "failurePolicy", ""),
            ("id", "id", ""),
            ("language", "language", "VELOCITY"),
            ("lastUpdateTime", "lastUpdateTime", ""),
            ("latestVersionTime", "latestVersionTime", ""),
            ("name", "name", ""),
            ("parentTemplateId", "parentTemplateId", ""),
            ("projectId", "projectId", ""),
            ("projectName", "projectName", ""),
            ("rollbackTemplateContent", "rollbackTemplateContent", ""),
            ("rollbackTemplateParams", "rollbackTemplateParams", []),
            ("softwareType", "softwareType", ""),
            ("softwareVariant", "softwareVariant", ""),
            ("softwareVersion", "softwareVersion", ""),
            ("templateContent", "templateContent", ""),
            ("templateParams", "templateParams", []),
            ("validationErrors", "validationErrors", {}),
            ("version", "version", ""),
        ]

        return any(not dnac_compare_equality(current_obj.get(dnac_param, default),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param, default) in obj_params)


    def get_task_details(self, id):
        result = None
        response = self.dnac.exec(
            family="task",
            function='get_task_by_id',
            params={"task_id":id},
        )

        if self.log:
            log(str(response))

        if isinstance(response, dict):
            result = response.get("response")

        return result


    def get_diff_merge(self):
        diff_create = []
        diff_create_update = []
        template_id = None
        template_ceated = False
        template_updated = False
        template_exists = self.have_create.get("template_found")

        if template_exists:
            if self.requires_update():
                response = self.dnac.exec(
                    family="configuration_templates",
                    function="update_template",
                    params=self.want_create.get("template_params"),
                    op_modifies=True,
                )

                template_updated = True
                template_id = self.have_create.get("templateId")

                if self.log:
                    log("Updating Existing Template")
            else:
                #Template does not need update
                self.result['response'] = self.have_create.get("template") 
                self.module.exit_json(msg="Template does not need update")
        else:
            response = self.dnac.exec(
                family="configuration_templates",
                function='create_template',
                op_modifies=True,
                params=self.want_create.get("template_params"),
            )

            if self.log:
                log("Template created. Get template_id for versioning")

            if isinstance(response, dict):
                create_error = False
                task_details = {}
                task_id = response.get("response").get("taskId")

                if task_id:
                    while(True):
                        task_details = self.get_task_details(task_id)
                        if task_details and (task_details.get("isError")==True):
                            create_error = True
                            break

                        if task_details and \
                            ("Successfully created template" in task_details.get("progress")):
                            break
                        
                    if not create_error:
                        template_id = task_details.get("data")

            if template_id:
                template_created = True

        if template_updated or template_created:
            #Template needs to be versioned
            version_params = dict(
                comments=self.want_create.get("comments"),
                templateId=template_id
            )
            response = self.dnac.exec(
                family="configuration_templates",
                function='version_template',
                op_modifies=True,
                params=version_params
            )
            task_details = {}
            task_id = response.get("response").get("taskId")

            if task_id:
                task_details = self.get_task_details(task_id)

                if self.log:
                    log(str(task_details))
                self.result['changed'] = True
                self.result['diff'] = self.validated
                
            self.result['response'] = task_details if task_details else response


    def get_diff_query(self):
        template_exists = self.have_create.get("template_found")

        if template_exists:
            self.result['response'] = self.have_create.get("template")
        else:
            self.module.exit_json(msg="Template not found")


    def get_diff_delete(self):
        template_exists = self.have_create.get("template_found")

        if template_exists:
            response = self.dnac.exec(
                family="configuration_templates",
                function="deletes_the_template",
                params={"template_id": self.have_create.get("templateId")},
            )
            task_details = {}
            task_id = response.get("response").get("taskId")

            if task_id:
                task_details = self.get_task_details(task_id)

                if self.log:
                    log(str(task_details))
                self.result['changed'] = True
            self.result['response'] = task_details if task_details else response
        else:
            self.module.exit_json(msg="Template not found")


def main():
    """ main entry point for module execution
    """

    element_spec = dict(
        dnac_host=dict(required=True, type='str'),
        dnac_port=dict(required=False, type='str', default='443'),
        dnac_username=dict(required=True, type='str', no_log=True),
        dnac_password=dict(required=True, type='str', no_log=True),
        dnac_verify=dict(required=False, type='bool', default='False'),
        dnac_debug=dict(required=False, type='bool', default='False'),
        dnac_log=dict(required=False, type='bool', default='False'),
        config=dict(required=True, type='list', elements='dict'),
        state=dict(
            default='merged',
            choices=['merged', 'delete', 'query']),
        )
    
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_template = DnacTemplate(module)
    dnac_template.validate_input()
    state = dnac_template.get_state()

    dnac_template.get_have()
    dnac_template.get_want()

    if state == "merged":
        dnac_template.get_diff_merge()

    if state == "query":
        dnac_template.get_diff_query()

    if state == "delete":
        dnac_template.get_diff_delete()

    module.exit_json(**dnac_template.result)

if __name__ == '__main__':
    main()
