# Data layout

Place data under the configured `data_root` using the layout below, or override
individual paths in `config/local.json`.

```text
data/
├── GONG/{fits,harmonics,mrzqs/fits}/
├── OMNI/omni_27_av.dat
├── Sunspot/{sn.mat,sn_sm.mat,sn_interp.mat,SN_*_tot_V2.0*.csv}
├── WSO/{download/dat,download/txt,field,harmonics}/
├── WSO/gather_harmonic_coefficient.mat
└── transformer/{2002_2004_5min_data.csv,2005_data_5min_4day.csv}
```

## Upstream sources

- WSO synoptic maps: <http://wso.stanford.edu/#Synoptic>
- SILSO International Sunspot Number: <https://www.sidc.be/SILSO/datafiles>
- GONG magnetic-field products: <https://gong.nso.edu/data/magmap/>
- NASA OMNI data: <https://omniweb.gsfc.nasa.gov/>

The preprocessed `.mat`, `.fits`, and `.xlsx` files already committed here are
retained as compact workflow examples or derived products. A derived file does
not automatically inherit permission for unrestricted reuse from its source.

Configuration precedence is `config/default.json`, untracked
`config/local.json`, then the `SMP_*` environment variables.

## Main scientific data contracts

| Product | Contents and consumer |
| --- | --- |
| `WSO/harmonics/crNNNN.dat` | Four columns: degree l, nonnegative order m, cosine coefficient g, sine coefficient h. Consumed by gathering and map reconstruction. |
| `WSO/gather_harmonic_coefficient.mat` | `save_var`: row 1 contains l, row 2 signed m, remaining rows consecutive CR samples. Degree-nine data have 100 coefficient columns. |
| `Sunspot/sn.mat` | Model key `sn`, an N-by-1 vector of monthly sunspot-number values. |
| `Sunspot/sn_sm.mat` | Model key `sn`, an N-by-1 vector of 13-month-smoothed monthly values. Prepare this MAT file from the appropriate dated SILSO record. |
| `Sunspot/sn_interp.mat` | `save_var`: CR, fractional year, and interpolated sunspot number in three columns, used by the experimental one-to-one LSTM mapping. |
| `model_output/g_l_m.csv` | One forecast value per row, no header, 150 future CR values for the main EMD-LSTM export. Signed m identifies cosine (m ≥ 0) or sine (m < 0) components. |
| `predict_SC25/harmonics/crNNNN.dat` | Forecast tables through l=5, generated from all 36 signed-order CSVs. The formatter maps forecast row 1 to CR2259. |

The Python model reads zero-based rows 0/1 as metadata and starts observations at row 2. The supplied historical matrix starts at CR1642. Keep column order synchronized with the EMD-LSTM `look_back_mat` table, and keep CR alignment consistent with the selected training cutoff. The default `dev=141` is a historical hindcast setting; it does not automatically match the formatter's CR2259 origin. For the full original 617-CR record through CR2258, remove that holdout before exporting forecasts labeled CR2259 onward.

`gather_harmonic_coefficients.m` writes both ASCII and MAT versions when saving is enabled. `neaten_sunspot_number.m` exports interpolated ASCII/CSV records; it does not generate every sunspot MAT file required by the Python models.

## Forecast handoff

1. Set the model input matrix and historical cutoff. Inspect `lm`, `look_back_mat`, `future_step`, and `save_or_not` in the main EMD-LSTM script before training.
2. Export all 36 coefficient sequences into `cfg.paths.model_output` / `config.path("model_output")`.
3. Run `neaten_predict_harmonic_coefficient.m` to write per-rotation tables into the shared `predicted_harmonics` path.
4. In `plot_synoptic_map_from_harmonic_coefficient.m`, set `mode=2` and choose the CR range. Its maps use 180 colatitude samples and 360 longitude samples; WSO values are converted from microtesla to gauss.

Predicted harmonic tables and rendered PNGs are different products. Residual/correlation plots additionally require numeric reconstructed maps or prepared workspace variables; the map plotter does not automatically create all downstream MAT grids.

## Using the existing local RESULT archive

The existing external archive can remain at `F:/Project/Synoptic_map_prediction_by_LSTM_EMD/RESULT`. For access to its precomputed forecast products, merge these values into the private `config/local.json`:

```json
{
  "output_root": "F:/Project/Synoptic_map_prediction_by_LSTM_EMD/RESULT",
  "paths": {
    "model_output": "F:/Project/Synoptic_map_prediction_by_LSTM_EMD/RESULT/predict_SC25/model_output",
    "predicted_harmonics": "F:/Project/Synoptic_map_prediction_by_LSTM_EMD/RESULT/predict_SC25/harmonics"
  }
}
```

Keep the private data root pointed at the actual observation archive. The RESULT archive is not a replacement for WSO/GONG/SILSO input data, and some historical plotting scripts expect additional case-specific subdirectories.

## Reproduction limits

- CWT currently selects l=0 and leaves CSV/figure exports disabled; choose the desired degrees and enable the matching export paths before the MATLAB spectrum plotting step.
- Sunspot and coefficient models write `best_model.pkl` to the current working directory. Preserve trained runs in separate working directories; existing checked-in checkpoint names are historical artifacts without a complete training manifest.
- The EMD-LSTM normalization fits the retained series before splitting, and checkpoint restoration is disabled. These historical conventions are documented rather than silently replaced.
- A full 36-coefficient forecast requires manual selection and potentially lengthy training. The forecast formatter does not train missing coefficients.
- PFSS scripts use GONG templates and local MAT files. FITS header dates, rotation numbers, orientation, and flux balance must match any substituted prediction.
- SWMF scripts read external simulation products. The upstream SWMF run and complete external toolchains are not supplied.
