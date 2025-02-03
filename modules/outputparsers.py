def parse_errors(output):
    return [line for line in output.split('\n') if 'Error:' in line]

def parse_warnings(output):
    return [line for line in output.split('\n') if 'Warning:' in line]