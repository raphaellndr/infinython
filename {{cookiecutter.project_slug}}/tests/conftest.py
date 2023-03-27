"""Tests configuration."""

import socket

import pytest
from py.xml import html  # pylint: disable = no-name-in-module, import-error

# pytest-html hooks for report customization


def pytest_html_report_title(report):
    """Pytest-html title customization."""
    report.title = "Viperz - Tests report"


def pytest_configure(config):
    """Pytest-html environment customization."""
    config._metadata["INSTANCE"] = socket.gethostname()  # pylint: disable = protected-access


def pytest_html_results_table_header(cells):
    """Pytest-html table header customization."""
    column = html.th(html.div("vvv", class_="sort-icon"), "STD ID", class_="sortable", col="stdid")
    cells.insert(0, column)
    cells.pop()


def pytest_html_results_table_row(report, cells):
    """Pytest-html table content customization."""
    if hasattr(report, "std"):
        cells.insert(0, html.td(report.std, class_="col-stdid"))
    else:
        cells.insert(0, "")
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable = unused-argument
    """Pytest-html report data fetching customization."""
    outcome = yield
    report = outcome.get_result()
    report.std = "\u2014"
    for marker in item.iter_markers():
        if marker.name == "std" and len(marker.args) != 0:
            report.std = marker.args[0]
            break
