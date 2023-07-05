from setuptools import setup, find_packages
setup(
    name = 'timestamp_conversion_example',
    version = '1.0',
    packages = find_packages(include = ('timestamp_conversion_example*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.6'],
    entry_points = {
'console_scripts' : [
'main = timestamp_conversion_example.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
