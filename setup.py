from setuptools import setup
setup(
    name="agent-monitor",
    version="0.1.0",
    py_modules=["agent_monitor", "dashboard"],
    install_requires=["streamlit>=1.28", "prometheus-client>=0.18", "structlog>=23.0"],
    python_requires=">=3.9",
)
