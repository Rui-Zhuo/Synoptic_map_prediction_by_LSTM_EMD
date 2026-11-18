# Validation — 2026-11-18

## Completed checks

- Python sources compile, including archived and renamed scripts.
- Seven portable unit tests pass: normalization, smoothing, missing-file behavior, absolute default paths, forecast output handoff, and an absolute archive-path override.
- Python abstract syntax trees were compared with the previous commit. Apart from the intentional PyWavelets name correction and added tests, Python execution logic is unchanged; renamed scripts were compared with their original paths.
- The corrected `cmor1.5-1.0` wavelet executes on a synthetic 100-sample sequence and returns a 9-by-100 transform. This small API check is not validation of the paper spectra.
- Local relative Markdown links, complete source-file coverage in the README, PDF checksums, and the five figure crops were checked. Images were visually inspected against the rendered publication pages.
- The English and Chinese PDFs are byte-identical to the supplied source files. Their SHA-256 hashes are recorded in [paper/SHA256SUMS.txt](../paper/SHA256SUMS.txt).

## Limits

MATLAB R2022a could not start because the installed license has expired (License Manager Error -10). MATLAB numerical tests and the modified MAT/table handoffs therefore received static inspection only.

The local Python installation has NumPy 1.26.4 alongside an older SciPy that reports an incompatible supported range. The small wavelet check succeeds, but this installed environment is not claimed to match `requirements.txt`; use a fresh environment with the documented pins for model work.

The first utility-test attempt lacked the editable `smp` package. The successful local run used `PYTHONPATH=src`; CI installs the package with `pip install -e . --no-deps` before testing.

Full model training, reconstruction of all 36 coefficient forecasts, data-version comparisons, and SWMF calculations were not rerun. The displayed figures are reference results extracted from the published paper. Main-model defaults still select a single coefficient and a historical cutoff; scaling and final-weight checkpoint behavior remain unchanged and are documented in [DATA.md](DATA.md).
