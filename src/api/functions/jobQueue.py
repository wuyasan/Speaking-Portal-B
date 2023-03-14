# Queue for handling job reuqests: JobQueue
from enum import Enum
import uuid
import os
import shutil
SERVER_FILES_PATH = os.getcwd() + "/server_files"

class JobStatus(Enum):
    PENDING = 0
    COMPLETED = 1
    ERROR = 2
    PROCESSING_FILES = 3
    MFA_VALIDATION = 4
    MFA_ALIGN = 5
    MFA_CONVERTER = 6
    SCHEDULING_FRAMES = 7
    GENERATING_VIDEO_FRAMES = 8
    STITCHING_VIDEO_FRAMES = 9

class Job:
        
        def __init__(self):
            uuid_str = str(uuid.uuid4())
            self.job_id = uuid_str
            self.status = JobStatus.PENDING
            self.job_dir = SERVER_FILES_PATH + "/jobs/" + uuid_str
            # Create job directory
            os.makedirs(self.job_dir, exist_ok=True)
            # Create inputs directory
            os.makedirs(self.job_dir + "/inputs", exist_ok=True)
            # Create outputs directory
            os.makedirs(self.job_dir + "/outputs", exist_ok=True)

        def set_status(self, status):
            self.status = status

        def get_status(self):
            return self.status
        
        def get_job_dir(self):
            return self.job_dir
        
        def get_job_id(self):
            return self.job_id
        
        def get_job(self):
            return {
                "job_id": self.job_id,
                "status": self.status,
            }

class JobQueue:
     
    def __init__(self):
         self.queue = []

    def add_job(self, job: Job) -> None:
        self.queue.append(job)

    def get_job(self, job_id) -> Job:
        for job in self.queue:
            if job.get_job_id() == job_id:
                return job
        return None
    
    def get_job_status(self, job_id) -> JobStatus:
        job = self.get_job(job_id)
        if job is not None:
            return job.get_status()
        return None
    
    def get_job_dir(self, job_id) -> str:
        job = self.get_job(job_id)
        if job is not None:
            return job.get_job_dir()
        return None
    
    def get_job_queue(self) -> list:
        return self.queue
    
    def get_job_queue_length(self) -> int:
        return len(self.queue)
    
    def set_job_status(self, job_id, status) -> bool:
        job = self.get_job(job_id)
        if job is not None:
            job.set_status(status)
            return True
        return False
    
    def remove_job(self, job_id) -> bool:
        job = self.get_job(job_id)
        # Delete job directory
        print("Deleting job directory: " + job.get_job_dir())
        shutil.rmtree(job.get_job_dir())

        if job is not None:
            self.queue.remove(job)
            return True
        return False