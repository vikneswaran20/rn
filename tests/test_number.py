from click.testing import CliRunner
from rn.main import cli


class TestNumbers:

    def test_number_defaults(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number'])
        output = int(result.output)

        assert result.exit_code == 0
        assert output >= 0 and output <= 1000

    def test_iterator(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number', '-i 10', '-d ,'])
        output = result.output.split(',')

        assert result.exit_code == 0
        assert len(output) == 10

    def test_delimiter(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number', '-i 10', '-d ,'])

        assert result.exit_code == 0
        assert result.output.count(',') == 9

    def test_sorting_asc(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number', '-i 10', '-d ,', '-s', 'asc'])
        output = list(map(int, result.output.split(',')))
        test = list(output)
        test.sort()

        assert result.exit_code == 0
        assert output == test

    def test_sorting_desc(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number', '-i 10', '-d ,', '-s', 'desc'])
        output = list(map(int, result.output.split(',')))
        test = list(output)
        test.sort(reverse=True)

        assert result.exit_code == 0
        assert output == test

    def test_uniq(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['number', '-i 10', '-d ,', '-u'])
        output = list(map(int, result.output.split(',')))

        assert result.exit_code == 0
        assert len(set(output)) == len(output)
