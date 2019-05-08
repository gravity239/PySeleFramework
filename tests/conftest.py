import pytest


def pytest_addoption(parser):
    parser.addoption("--remote-host", action="store", help="Remote server for execution. http://127.0.0.1:4444/wd/hub",
                     metavar="")
    parser.addoption("--driver", action="store",
                     help="Configure the driver that you want to execute the tests. It should be: chrome, firefox",
                     metavar="")
    parser.addoption("--browser-config-file", action="store", help="Configure the setting for chrome, firefox",
                     metavar="")
    parser.addoption("--run-mode", action="store", help="Running mode such as desktop or mobile", metavar="")


@pytest.fixture(scope="session", autouse=True)
def remote_host(request):
    remote_host = request.config.getoption("--remote-host", None)
    pytest.remote_host = remote_host
    return remote_host


@pytest.fixture(scope="session", autouse=True)
def browser_name(request):
    browser_name = request.config.getoption("--driver", "chrome", True)
    pytest.browser_name = browser_name
    return browser_name


@pytest.fixture(scope="session", autouse=True)
def browser_config_file(request):
    import os
    browser_config_file = request.config.getoption("--browser-config-file",
                                                   os.path.join("tests/config/browser_setting_default.cfg"), True)
    pytest.browser_config_file = browser_config_file
    return browser_config_file


@pytest.fixture(scope="session", autouse=True)
def run_mode(request):
    run_mode = request.config.getoption("--run-mode", "desktop", True)
    pytest.run_mode = run_mode
    return run_mode
