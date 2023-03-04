
def success(msg, job_id = 0, data = None, code = 200, text_file_path = None, audio_file_path = None):
    return {
        'status': 'success',
        'message': msg,
        'job_id': job_id,
        'data': data,
        'code': code,
    }

def error(msg, job_id = 0, data = None, code = 400):
    return {
        'status': 'error',
        'message': msg,
        'job_id': job_id,
        'data': data,
        'code': code
    }