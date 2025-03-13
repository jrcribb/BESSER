from pydantic import BaseModel
from typing import Optional, Dict, Any, Literal

class DjangoConfig(BaseModel):
    project_name: str
    app_name: str
    containerization: bool = False

class SQLConfig(BaseModel):
    dialect: Literal["standard", "postgresql", "mysql"] = "standard"

class ClassDiagramInput(BaseModel):
    diagramTitle: str = "Diagram"
    elements: Dict[str, Any]
    generator: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
