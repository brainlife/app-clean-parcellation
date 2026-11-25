<h1 align="center">Clean parcellations</h1>

<p align="center">
  A volumetric parcellation with unwanted and unmatched parcels removed and the remaining parcels renumbered 1..N, with a matching <code>label.json</code>.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.518"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.518-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Removes unwanted or missing parcels from a volumetric parcellation and renumbers the remaining parcels consecutively, updating label.json, with nibabel and numpy; a parcellation utility.**

Drops parcels listed in discard_labels plus any parcel present in the image but not in label.json (and vice versa), sets them to 0, renumbers the remaining parcels 1..N and writes a matching label.json. Use it before building networks or summary statistics so node lists match the image. The original key.txt is copied unchanged and does not reflect the renumbering.

| | |
|---|---|
| **Inputs** | `neuro/parcellation/volume` |
| **Outputs** | `neuro/parcellation/volume` |
| **Container** | `brainlife/dipy:1.4.0` |
| **Resources** | 1 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.518](https://doi.org/10.25663/brainlife.app.518) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `parc` | `neuro/parcellation/volume` | yes | Volumetric parcellation (parc.nii.gz) with its key.txt and label.json; label.json voxel_value entries define the valid parcels. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/parcellation/volume` | This parcellation will have missing and unwanted parcels removed from the parcellation. This will help with network generation and summary statistics |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `discard_labels` | string |  | Space-separated voxel values (from label.json) of the parcels to remove, e.g. "1 181"; leave empty to only remove parcels missing from label.json or the image. |

</details>

<!-- brainlife-app:end -->

## How it works

The App is written in Python with [nibabel](https://nipy.org/nibabel/) and [numpy](https://numpy.org/). It removes (sets to 0):

- the parcels whose voxel values you list in `discard_labels`;
- any parcel that is present in the image but has no entry in `label.json`, and any `label.json` entry that has no voxels in the image.

The remaining parcels are renumbered consecutively from 1, and a new `label.json` is written with the updated `voxel_value`, `label` and `desc` fields. Clean a parcellation this way before building networks or computing summary statistics, so that the node list matches the image.

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.518](https://doi.org/10.25663/brainlife.app.518), choose a `neuro/parcellation/volume` dataset from your project, enter the voxel values to remove in `discard_labels` (space-separated, or leave it empty) and press **Execute**. The cleaned parcellation is archived to your project as a `neuro/parcellation/volume` dataset tagged `cleaned`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) and [`jq`](https://jqlang.github.io/jq/). `main` runs the Python script inside the `brainlife/dipy:1.4.0` container; without Singularity, install Python 3 with nibabel and numpy.

1. Clone this repository and check out the App's branch: `git checkout v1.0`.
2. Create `config.json` with the paths to your parcellation files and the parcels to remove:

   ```json
   {
       "parcellation": "/input/parc/parc.nii.gz",
       "key": "/input/parc/key.txt",
       "labels": "/input/parc/label.json",
       "discard_labels": "1 181"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

### Sample data

Download a parcellation from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset id>
```

## Outputs

```text
output/
├── parc.nii.gz   the cleaned, renumbered parcellation
├── label.json    labels of the remaining parcels, renumbered 1..N
└── key.txt       copied unchanged from the input
```

`key.txt` is copied as is and does not reflect the renumbering; use `label.json` for the new voxel values.

## Troubleshooting

- **`something went wrong. check derivatives`**: `output/parc.nii.gz` was not written. Check that the parcellation has a `label.json` whose entries carry `voxel_value` fields.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Clean parcellations. brainlife.io App. [doi:10.25663/brainlife.app.518](https://doi.org/10.25663/brainlife.app.518)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Brad Caron

**Contributors:** Soichi Hayashi

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](LICENSE), Copyright (c) 2020 brainlife.io, The University of Texas at Austin and Indiana University.
