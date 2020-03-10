import os
import json
import time
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running_and_enabled(host):
    service = host.service('td-agent')
    assert service.is_running
    assert service.is_enabled


def test_nginx(host):
    host.command("curl -sf http://localhost/nonexistent.html")
    time.sleep(10)

    access = host.file(
        '/var/log/td-agent/nginx-access/fluentd.log'
        ).content_string.splitlines()[-1].split(None, 2)
    error = host.file(
        '/var/log/td-agent/nginx-error/fluentd.log'
        ).content_string.splitlines()[-1].split(None, 2)

    assert access[1] == 'nginx.access'
    accessj = json.loads(access[2])
    assert accessj['host'] == '127.0.0.1'
    assert accessj['method'] == 'GET'
    assert accessj['path'] == '/nonexistent.html'
    assert accessj['code'] == '404'
    assert 'curl' in accessj['agent']

    assert error[1] == 'nginx.error'
    errorj = json.loads(error[2])
    assert errorj['log_level'] == 'error'
    assert 'No such file or directory' in errorj['message']
