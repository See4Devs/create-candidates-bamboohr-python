# Post Candidates on BambooHR with Python

A basic python script to create candidates on [BambooHR](https://www.bamboohr.com).

## Prerequisites

If you don't have it, Install the requests library

```bash
pip3 install requests
```

You need to have a [BambooHR account](https://www.bamboohr.com/signup) and then gernerate an API key so you can use it to run the python code.

## Run the code

```bash
python3 get_bamboohr_jobs.py
```

You’ll see a list of job IDs and their corresponding titles outputted in your terminal or shell. Make a note of the `jobId` you want to use when posting candidates.

```bash
python3 post_bamboohr_candidates.py
```

Replace the `subdomain`, `api_key` and `'the_job_id_you_obtained'` with the actual job ID you retrieved from the previous script.

Author : Lucien Chemaly
