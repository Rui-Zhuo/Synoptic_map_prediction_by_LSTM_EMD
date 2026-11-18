# Figure provenance

The five README images were extracted on 2026-11-18 from the author-supplied English publisher PDF, [Zhuo et al. (2024)](../paper/Zhuo_et_al_2024_SCES.pdf), DOI [10.1007/s11430-023-1354-4](https://doi.org/10.1007/s11430-023-1354-4). Copyright: Science China Press 2024, as stated in the article. No new figure license is asserted.

They are published reference results, not a rerun of this checkout. Figures were rendered with Poppler at a longest-page dimension of 2400 pixels and cropped around the original panels; axes, legends, and scientific content are retained. Captions in the README are summaries; consult the PDF for full original captions and interpretation.

| Original figure | PDF page (1-based) | Image | Crop x, y, width, height (pixels) |
| --- | --- | --- | --- |
| 10 | 12 | [figure_10_lstm_workflow.png](figure_10_lstm_workflow.png) | (350, 205, 1110, 640) |
| 11 | 12 | [figure_11_sunspot_prediction.png](figure_11_sunspot_prediction.png) | (140, 920, 1510, 900) |
| 12 | 13 | [figure_12_emd_lstm.png](figure_12_emd_lstm.png) | (205, 720, 1375, 1380) |
| 14 | 15 | [figure_14_predicted_maps.png](figure_14_predicted_maps.png) | (235, 210, 1315, 595) |
| 15 | 16 | [figure_15_map_validation.png](figure_15_map_validation.png) | (235, 210, 1365, 1520) |

Example extraction from the repository root (Poppler):

```bash
pdftoppm -f 12 -l 12 -scale-to 2400 -x 350 -y 205 -W 1110 -H 640 -singlefile -png paper/Zhuo_et_al_2024_SCES.pdf figures/figure_10_lstm_workflow
```

The external local RESULT archive contains historical plot exports. The curated README set uses the publication PDF to keep the displayed figures consistent with the cited paper.
