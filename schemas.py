from pydantic import BaseModel
from typing import List, Optional

class Issue(BaseModel):
    issue: str
    severity: str
    location: Optional[str] = None

class AnalysisResponse(BaseModel):
    damage_score: int
    safety_rating: str
    identified_issues: List[Issue]
    maintenance_suggestions: List[str]
    inspection_summary: str
