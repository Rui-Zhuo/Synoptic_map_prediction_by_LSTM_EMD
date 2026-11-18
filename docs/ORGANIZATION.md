# Repository organization — 2026-11-18

The Git checkout remains at `CODE/`; the parent project directory and external `RESULT` archive are preserved. The paper and public repository concern solar activity and synoptic-map prediction; the HCS/PSP repository was used as a presentation reference.

## Structure and naming

- Existing scientific workflow directories and compact historical data examples remain in place to preserve references.
- Earlier duplicate EMD and Transformer scripts are grouped under `archive/`; [the archive index](../archive/README.md) maps their old names.
- `autoencoder_decoder/antoencoder.py` was renamed to `autoencoder_decoder/autoencoder.py`.
- `paper/`, `figures/`, and `references/` contain publication assets, provenance, and citations.
- Every Python/MATLAB source has a purpose and input-context header. Additional comments explain signed-order columns, EMD component windows, LSTM sequence context, recursive prediction, and spherical-harmonic normalization.
- New generated checkpoints and preparation files are ignored. Existing tracked checkpoints/data are retained; adding an ignore rule does not remove them from Git history.

## Small workflow repairs

1. `gather_harmonic_coefficients.m` additionally saves `save_var` to the configured MAT path, matching Python's `loadmat` contract.
2. The forecast formatter reads `model_output` and writes `predicted_harmonics`; the reconstruction and coefficient comparison scripts use the same named path.
3. The PyWavelets family spelling was corrected from `cmorl1.5-1.0` to `cmor1.5-1.0`.
4. Dependency notes now distinguish the pinned reconstruction environment from an unarchived original training environment.

Model architectures, historical cutoffs, optimization, normalization, seeds, and checkpoint-selection behavior are retained. In particular, the main EMD-LSTM script fits normalization before splitting and leaves best-checkpoint restoration commented out; these details must be considered when designing an independent evaluation.

No external simulations, large archive migrations, or full retraining were performed. Source PDFs were copied unchanged from the author-provided publication folder.
