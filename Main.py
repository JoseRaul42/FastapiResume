from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os
import sys
import httpx

# Retrieve environment variables directly
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Validate environment variables
if not url or not key:
    print("Supabase URL or API key is missing. Check your environment variables.")
    sys.exit(1)  # Exit the application if the environment variables are not set

# Initialize Supabase client
supabase: Client = create_client(url, key)

app = FastAPI(title="Jose's Resume API")

@app.get("/ResumeSummary/")
async def read_resume_summary():
    async with httpx.AsyncClient() as client:
        supabase_response = await client.get(
            f"{url}/rest/v1/resume?select=Summary",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}"
            }
        )
    
    if supabase_response.status_code != 200:
        print("Error fetching data:", supabase_response.text)
        raise HTTPException(status_code=400, detail="Error fetching data from Supabase.")
    
    data = supabase_response.json()
    
    if not data:
        raise HTTPException(status_code=404, detail="No summary found.")
    
    summaries = [record['Summary'] for record in data]
    return summaries

@app.get("/ResumeTech/")
async def read_resume_tech():
    async with httpx.AsyncClient() as client:
        supabase_response = await client.get(
            f"{url}/rest/v1/resume?select=Tech",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}"
            }
        )
    
    if supabase_response.status_code != 200:
        print("Error fetching data:", supabase_response.text)
        raise HTTPException(status_code=400, detail="Error fetching data from Supabase.")
    
    data = supabase_response.json()
    
    if not data:
        raise HTTPException(status_code=404, detail="No tech information found.")
    
    techs = [record['Tech'] for record in data]
    return techs

@app.get("/ResumeExp/")
async def read_resume_exp():
    async with httpx.AsyncClient() as client:
        supabase_response = await client.get(
            f"{url}/rest/v1/resume?select=exp",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}"
            }
        )
    
    if supabase_response.status_code != 200:
        print("Error fetching data:", supabase_response.text)
        raise HTTPException(status_code=400, detail="Error fetching data from Supabase.")
    
    data = supabase_response.json()
    
    if not data:
        raise HTTPException(status_code=404, detail="No experience information found.")
    
    experiences = [record['exp'] for record in data]
    return experiences

@app.get("/ResumeProjects/")
async def read_resume_projects():
    async with httpx.AsyncClient() as client:
        supabase_response = await client.get(
            f"{url}/rest/v1/resume?select=Projects",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}"
            }
        )
    
    if supabase_response.status_code != 200:
        print("Error fetching data:", supabase_response.text)
        raise HTTPException(status_code=400, detail="Error fetching data from Supabase.")
    
    data = supabase_response.json()
    
    if not data:
        raise HTTPException(status_code=404, detail="No projects found.")
    
    projects = [record['Projects'] for record in data]
    return projects
