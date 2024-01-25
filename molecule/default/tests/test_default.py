import os
import json
import time
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running_and_enabled(host):
    service = host.service('fluent')
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


    assert 'log/access.log' in access[0]
    #accessj = json.loads(access[2])
    #assert accessj['host'] == '127.0.0.1'
    #assert accessj['method'] == 'GET'
    #assert accessj['path'] == '/nonexistent.html'
    #assert accessj['code'] == '404'
    #assert 'curl' in accessj['agent']

    assert 'log/error.log' in error[0]
    #errorj = json.loads(error[2])
    #assert errorj['log_level'] == 'error'
    #assert 'No such file or directory' in errorj['message']
