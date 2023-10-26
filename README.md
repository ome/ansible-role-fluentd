Fluentd
=======

[![Actions Status](https://github.com/ome/ansible-role-fluentd/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-fluentd/actions)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-fluentd-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/ome/fluentd/)

Install Fluentd log collector.

Uses the stable commmunity td-agent package supplied by Treasure Data https://docs.fluentd.org/v1.0/articles/install-by-rpm


Variables
---------

Optional:
- `fluentd_groups`: List of additional groups the Fluentd/td-agent user should be a member of, e.g. to allow access to restricted logs, default none
- `fluentd_plugins`: List of Fluentd plugins to install, default none. See https://www.fluentd.org/plugins
- `fluentd_env`: Dictionary of environment variables
- `fluentd_yum_lock_timeout`: Time in seconds to wait for the yum process to free the lockfile


Configuration
-------------

Configuration files should be placed in `/etc/td-agent/conf.d`.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
