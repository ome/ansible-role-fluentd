import os
import json
import time
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running_and_enabled(host):
    service = host.service('fluentd')
    assert service.is_running
    assert service.is_enabled

def test_nginx(host):
    host.command("curl -sf http://localhost/nonexistent.html")
    time.sleep(10)

    access = host.file(
        '/var/log/fluent/nginx-access.log.pos'
    ).content_string.splitlines()[-1].split(None, 2)
    error = host.file(
        '/var/log/fluent/nginx-error.log.pos'
    ).content_string.splitlines()[-1].split(None, 2)

    assert '/var/log/nginx/access.log' == access[0]

    assert '/var/log/nginx/error.log' == error[0]
