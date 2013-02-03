def get_request_type(command):
	try:
		return command_mapping[command]
	except KeyError:
		return 'unknown'

command_mapping = {}
command_mapping['new'] = 'meta'
command_mapping['setup'] = 'perform'
command_mapping['draw'] = 'perform'
command_mapping['phase'] = 'perform'
command_mapping['turn'] = 'perform'
command_mapping['play'] = 'perform'
command_mapping['out'] = 'perform'
command_mapping['exit'] = 'sys'
command_mapping['test'] = 'sys'
