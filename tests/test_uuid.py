from uuid import UUID
from click.testing import CliRunner
from rn.main import cli


class TestUUID:

    def test_uuid(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['uuid'])
        output = result.output[:-1]
        uuid = UUID(output)

        assert result.exit_code == 0
        assert output == str(uuid)

    def test_iterator(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['uuid', '-i 10', '-d ,'])
        output = result.output.split(',')

        assert result.exit_code == 0
        assert len(output) == 10

    def test_delimiter(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['uuid', '-i 10', '-d ,'])

        assert result.exit_code == 0
        assert result.output.count(',') == 9
