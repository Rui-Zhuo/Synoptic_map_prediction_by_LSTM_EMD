# Defines the lightweight Python package entry point and version metadata. Install the
# repository in editable mode to make its configuration and utilities available to
# research scripts.
# Inputs and run settings: see README.md and docs/DATA.md.

"""Utilities for the solar-activity prediction research scripts."""

from .config import ProjectConfig, load_config
from .constants import DEFAULT_RANDOM_SEED

__all__ = ["DEFAULT_RANDOM_SEED", "ProjectConfig", "load_config"]
