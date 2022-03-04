Ansible role for nodejs
==================================

Installs NodeJS toolchain

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nodejs-toolchain/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nodejs-toolchain/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-nodejs-toolchain/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-nodejs-toolchain/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| nodejs\_toolchain\_version | Version of nodejs toolchain to install | string | "" | true |
| nodejs\_toolchain\_user | User that will be using the nodejs toolchain | string | "" | false |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-nodejs-toolchain
      vars:
        nodejs_toolchain_version: "v8.11.3"
```

License
-------

[Apache License](LICENSE)
