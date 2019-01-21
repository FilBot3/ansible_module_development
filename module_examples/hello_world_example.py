#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible Module Documentation Layout detailed at this link:
# => https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html


# Copyriht: (c) 2019
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Set metadata about the module for when others view informaiton about it when
# choosing whether or not to use your module.
ANSIBLE_METADATA = {
	'metadata_version': '1.1',
	'status': ['preview'],
	'supported_by': 'community'
}

# A docstring that contains a YAML format detailing how to use the module and
# what the module does.
DOCUMENTATION = '''
---
module: hello_world_example
short_description: This module says hello world to people, loudly.
description:
  - "This is a longer description. You can use YAML scalars if need be."
options:
  name:
    description:
      - "The name of who to say hello to."
    default: world
    type: str
    required: true
    version_added: "2.7"
  loud:
    description:
      - "Say it loudly?"
    required: false
author:
  - Phillip Dudley (Predatorian3@gmail.com)
version_added: "2.7"
notes:
  - "This is the notes section. Other informaiton and stuff."
...
'''

# A docstring that gives examples of how o use the module in a Playbook.
# Try to be thorough and show all the different ways to use the module.
EXAMPLES = '''
# Passing in a name
- name: Say hello world
  hello_world_example
    name: Phillip

# Say it loudly to the person
- name: Say hello world, loudly
  hello_world_example:
    name: Phillip
    loud: True

# Fail for module testing purposes
- name: Fail to say hello world
  hello_world_example:
    name: fail me
'''

# This docstring details the returns that are output by this module to be used
# by other Ansible modules.
# Refer to the documentaiton link above for more information about what kind
# of fields are used in the return section.
RETURN = '''
name:
  description: The name of the person Hello was said to
  returned: success
  type: string
full_message:
  description: The whole message after the transformations happened.
  returned: success
  type: string
'''

# These libraries are only available within Ansible. So this code must be ran
# inside of Ansible. It is possible to test with only Pthon, but you need to
# setup the virtualenv, and then source the dev setup for Ansible.
# 
# Because of how the Ansible Module is written, the license, DOCUMENATION,
# EXAMPLES, RETURNS must all come prior to the import. 
from ansible.module_utils.basic import AnsibleModule

def main():
    # Code goes here...
# End of main():

# If this file is executed via Python, execut the main() function to call the
# module and run code.
if __name__ == '__main__':
    main()
# End of if __name__