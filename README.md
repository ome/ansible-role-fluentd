Fluentd
=======

Install Fluentd log collector.

Uses the stable commmunity td-agent package supplied by Treasure Data https://docs.fluentd.org/v1.0/articles/install-by-rpm


Variables
---------

Optional:
- `fluentd_groups`: List of additional groups the Fluentd/td-agent user should be a member of, e.g. to allow access to restricted logs, default none
- `fluentd_plugins`: List of Fluentd plugins to install, default none. See https://www.fluentd.org/plugins
- `fluentd_env`: Dictionary of environment variables


Configuration
-------------

Configuration files should be placed in `/etc/td-agent/conf.d`.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
