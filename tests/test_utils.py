# Checks default path resolution, normalization, moving-average length, and missing-file
# errors. These lightweight tests validate shared helpers and do not reproduce the
# scientific training or paper figures.
# Inputs and run settings: see README.md and docs/DATA.md.

import tempfile
import json
import unittest
from pathlib import Path

import numpy as np

from smp.config import load_config
from smp.utils import min_max_normalize, moving_average, require_file


class UtilityTests(unittest.TestCase):
    def test_forecast_handoff_uses_output_root(self) -> None:
        config = load_config()
        self.assertEqual(config.path('model_output'), config.output_root / 'model_output')
        self.assertEqual(config.path('predicted_harmonics'),
                         config.output_root / 'predict_SC25' / 'harmonics')

    def test_local_paths_can_map_existing_archive(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'archive'
            overrides = Path(directory) / 'override.json'
            overrides.write_text(json.dumps({'paths': {'harmonic_coefficients':
                str(archive / 'coefficients.mat')}}), encoding='utf-8')
            self.assertEqual(load_config(overrides).path('harmonic_coefficients'),
                             archive / 'coefficients.mat')

    def test_default_paths_are_absolute(self) -> None:
        config = load_config()
        self.assertTrue(config.path("sunspot").is_absolute())
        self.assertTrue(config.path("model_output").is_absolute())

    def test_min_max_normalize(self) -> None:
        result = min_max_normalize(np.array([-2.0, 0.0, 2.0]))
        np.testing.assert_allclose(result, [0.0, 0.5, 1.0])

    def test_min_max_normalize_rejects_constant_data(self) -> None:
        with self.assertRaisesRegex(ValueError, "constant"):
            min_max_normalize(np.ones(3))

    def test_moving_average_preserves_length(self) -> None:
        self.assertEqual(moving_average(np.arange(5.0), 3).shape, (5,))

    def test_require_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.dat"
            with self.assertRaisesRegex(FileNotFoundError, "config/local.json"):
                require_file(missing)


if __name__ == "__main__":
    unittest.main()
