import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bacula_director_is_installed(host):
    host.package("bacula-director").is_installed


def test_bacula_director_is_running(host):
    host.service("bacula-dir").is_running


def test_bacula_director_is_enabled(host):
    host.service("bacula-dir").is_enabled


def test_bacula_director_listen_port(host):
    host.socket("tcp://0.0.0.0:9101").is_listening
