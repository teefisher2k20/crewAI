from unittest import mock
from pathlib import Path
import pytest
from crewai.cli.create_crew import create_crew
from crewai.cli.create_flow import create_flow
from crewai.cli.utils import print_next_steps

@mock.patch("crewai.cli.utils.Console")
@mock.patch("rich.panel.Panel")
def test_print_next_steps(mock_panel, mock_console_class):
    mock_console = mock_console_class.return_value

    # We need to mock the console at the module level
    with mock.patch("crewai.cli.utils.console", mock_console):
        print_next_steps("test_folder")

    mock_panel.assert_called_once()
    args, kwargs = mock_panel.call_args
    assert "cd test_folder" in args[0]
    assert "crewai install" in args[0]
    assert "crewai run" in args[0]
    assert kwargs["title"] == "🚀 Next Steps"
    assert kwargs["border_style"] == "green"

    mock_console.print.assert_called()


@mock.patch("crewai.cli.create_crew.create_folder_structure")
@mock.patch("crewai.cli.create_crew.load_env_vars")
@mock.patch("crewai.cli.create_crew.copy_template")
@mock.patch("crewai.cli.create_crew.print_next_steps")
def test_create_crew_standalone_calls_print_next_steps(
    mock_print_next_steps, mock_copy_template, mock_load_env_vars, mock_create_folder_structure
):
    mock_create_folder_structure.return_value = (Path("test_crew"), "test_crew", "TestCrew")
    mock_load_env_vars.return_value = {}

    # Mocking open to avoid file operations
    with mock.patch("builtins.open", mock.mock_open()):
        create_crew("test_crew", skip_provider=True)

    mock_print_next_steps.assert_called_once_with("test_crew")

@mock.patch("crewai.cli.create_crew.create_folder_structure")
@mock.patch("crewai.cli.create_crew.load_env_vars")
@mock.patch("crewai.cli.create_crew.copy_template")
@mock.patch("crewai.cli.create_crew.print_next_steps")
def test_create_crew_embedded_does_not_call_print_next_steps(
    mock_print_next_steps, mock_copy_template, mock_load_env_vars, mock_create_folder_structure
):
    mock_create_folder_structure.return_value = (Path("existing_flow/test_crew"), "test_crew", "TestCrew")
    mock_load_env_vars.return_value = {}

    # Mocking open to avoid file operations
    with mock.patch("builtins.open", mock.mock_open()):
        create_crew("test_crew", skip_provider=True, parent_folder="existing_flow")

    mock_print_next_steps.assert_not_called()

@mock.patch("crewai.cli.create_flow.Path")
@mock.patch("crewai.cli.create_flow.Telemetry")
@mock.patch("crewai.cli.create_flow.print_next_steps")
def test_create_flow_calls_print_next_steps(
    mock_print_next_steps, mock_telemetry, mock_path
):
    # Mock project_root.exists() to return False
    # Path() returns a mock object when called
    mock_project_root = mock.MagicMock(spec=Path)
    mock_project_root.exists.return_value = False
    mock_path.return_value = mock_project_root

    # Configure the division operator for Path
    mock_project_root.__truediv__.return_value = mock_project_root

    # We need to mock the open() calls and other things to avoid errors
    with mock.patch("builtins.open", mock.mock_open()):
        with mock.patch("crewai.cli.create_flow.Path.mkdir"):
            create_flow("test_flow")

    mock_print_next_steps.assert_called_once_with("test_flow")
