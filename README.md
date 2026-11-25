[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.518-blue.svg)](https://doi.org/https://doi.org/10.25663/brainlife.app.518)

# Clean parcellations

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Removes unwanted or missing parcels from a volumetric parcellation and renumbers the remaining parcels consecutively, updating label.json, with nibabel and numpy; a parcellation utility.**

Drops parcels listed in discard_labels plus any parcel present in the image but not in label.json (and vice versa), sets them to 0, renumbers the remaining parcels 1..N and writes a matching label.json. Use it before building networks or summary statistics so node lists match the image. The original key.txt is copied unchanged and does not reflect the renumbering.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.518](https://doi.org/10.25663/brainlife.app.518)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `parc` | `neuro/parcellation/volume` | yes | Volumetric parcellation (parc.nii.gz) with its key.txt and label.json; label.json voxel_value entries define the valid parcels. |

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/parcellation/volume` | This parcellation will have missing and unwanted parcels removed from the parcellation. This will help with network generation and summary statistics |

| Parameter | Type | Default | Description |
|---|---|---|---|
| `discard_labels` | string |  | Space-separated voxel values (from label.json) of the parcels to remove, e.g. "1 181"; leave empty to only remove parcels missing from label.json or the image. |

Runtime: container `brainlife/dipy:1.4.0`; 1 CPUs.

<!-- brainlife-app:end -->

This app will This app will remove parcels from a parcellation/volume datatype based on user input. This is done using python, specifically nibabel and numpy.

### Authors

- Brad Caron (bacaron@utexas.edu)

### Contributors

- Soichi Hayashi (shayashi@iu.edu)

### Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations

We kindly ask that you cite the following articles when publishing papers and code using this code.

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

## Running the App

### On Brainlife.io

You can submit this App online at [https://doi.org/https://doi.org/10.25663/brainlife.app.518](https://doi.org/https://doi.org/10.25663/brainlife.app.518) via the 'Execute' tab.

### Running Locally (on your machine)

1. git clone this repo

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
	"parc": "/input/parc/parc.nii.gz",
	"key": "/input/parc/key.txt",
	"label": "/input/parc/label.json",
	"discard_labels": "1 181"
}
``` 

### Sample Datasets

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download
```

3. Launch the App by executing 'main'

```bash
./main
```

## Output

The main output of this App is a parcellation/volume datatype containing only the parcels the user wanted.

#### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.   

- nibabel: https://nipy.org/nibabel/
- numpy: https://numpy.org/

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
