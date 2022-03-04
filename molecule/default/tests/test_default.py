import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nodejs(host):
    cmd = host.run("/opt/node/bin/node --version")
    assert cmd.stdout == """v8.11.3"""

    cmd = host.run("node --version")
    assert cmd.stdout == """v8.11.3"""

    cmd = host.run("/opt/node/bin/npm --version")
    assert cmd.stdout == """5.6.0"""

    cmd = host.run("npm --version")
    assert cmd.stdout == """5.6.0"""

    cmd = host.run("/opt/node/bin/npx --version")
    assert cmd.stdout == """9.7.1"""

    cmd = host.run("npx --version")
    assert cmd.stdout == """9.7.1"""

    assert host.file("/root/.npmrc").exists
