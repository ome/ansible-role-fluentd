import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_service_running_and_enabled(Service):
    service = Service('td-agent')
    assert service.is_running
    assert service.is_enabled
