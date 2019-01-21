# Adding modules and plugins locally

## Overview

`Plugins` are pieces of code that are shared between modules or other things
withing the Ansible environment. `Modules` are methods for users to utilize in
their playbooks and perform actions they defined.

There are a few different places that plugins and modules can be placed to 
allow them to be used by playbooks. They can be system wide, user available,
local to the playbok, or even to specific roles.

## Plugins

### Types of Plugins

There ar a few different types of plugins for Ansible and Ansible Playbooks.

* action_plugins
* cache_plugins
* callback_plugins
* connection_plugins
* filter_plugins
* inventory_plugins
* lookup_plugins
* shell_plugins
* strategy_plugins
* test_plugins
* vars_plugins

### Plugin Locations

These are the differentlocations that an Ansible Python Plugin can e placed.

* `export ANSIBLE_${plugin type}_PLUGINS=/path/to:/ansible/plugin:/locations`
   * Similar to ANSIBLE_ACTION_PLUGINS, or ANSIBLE_FILTER_PLUGINS
* `/usr/share/ansible/plugins/plugin_type/${plugin type}_plugins/`
* `${HOME}/.ansible/plugins/${plugin type}_plugins/`
* `${ANSIBLE_PLAYBOOK}/${plugin type}_plugins/`
* `${ANSIBLE_PLAYBOOK}/roles/${ROLE_NAME}/${plugin type}_plugins/`

## Modules

### Module Locations

These are the different locaitons that an Ansible Python Module can be placed

* `export ANSIBLE_LIBRARY=/path/to:/folder/with:/ansible/modules`
* `/usr/share/ansible/plugins/modules/`
* `${HOME}/.ansible/plugins/modules/`
* `${ANSIBLE_PlAYBOOK}/library/`
* `${ANSIBLE_PlAYBOOK}/roles/${ROLE_NAME}/library/`