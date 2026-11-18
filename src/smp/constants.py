# Centralizes Carrington/year conversion constants, model-specific historical random
# seeds, and PFSS defaults. The EMD-LSTM and original LSTM seeds are retained separately
# from the configurable general seed.
# Inputs and run settings: see README.md and docs/DATA.md.

"""Physical and numerical constants shared by the analysis scripts."""

DEFAULT_RANDOM_SEED = 456
EMD_LSTM_RANDOM_SEED = 789
LSTM_ORIGINAL_RANDOM_SEED = 123
CARRINGTON_ROTATION_DAYS = 27.2753
TROPICAL_YEAR_DAYS = 365.2422
CARRINGTON_ROTATIONS_PER_YEAR = TROPICAL_YEAR_DAYS / CARRINGTON_ROTATION_DAYS
DEFAULT_SOURCE_SURFACE_RADIUS = 2.5
DEFAULT_PFSS_RADIAL_POINTS = 30
