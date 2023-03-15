import os
import sys
from functions import returnObj, jobQueue

def JpntextConvert(input_path, output_path, job: jobQueue.Job = None):
    try:
        with open(input_path, 'r+', encoding='UTF-8') as f:
            text = f.read()
            print("OG JAPNESE TEXT: " + text)
            result = " ".join(list(text))
            print("RESULT: " + result)
            f.write(result)
            f.close()
            return returnObj.success(msg="Japanese text converted to ARPA", data={"output_path": output_path}, job_id=job.get_job_id())
    except Exception as e:
        return returnObj.error(msg="Failed to convert Japanese text to ARPA" + str(e), data={"error": str(e)}, job_id=job.get_job_id())
