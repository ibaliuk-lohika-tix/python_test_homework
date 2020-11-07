from dataclasses import dataclass, field


@dataclass()
class ContextProfile:
    file_path: str = None
    error_message: str = None
    result: str = None


@dataclass()
class Context:
    profile: ContextProfile = field(default_factory=ContextProfile)
    root_path: str = None
