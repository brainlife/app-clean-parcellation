#!/usr/bin/env python3

import os
import argparse
import nibabel as nib
import numpy as np
import json

def clean_parcellation(parc,labels_json,labels_json_labels,discard_labels):
	
	# get the unique labels list, other than 0, which will be first
	parc_values = np.unique(parc.get_fdata())[1:].astype(np.int)
	parc_labels = list(parc_values.astype(np.str))

	# grab data in parcellation not in labels_json
	labels_not_in_json = [ f for f in parc_labels if f not in labels_json_labels ]

	# grab data in labels_json not in parcellation
	labels_not_in_parc = [ f for f in labels_json_labels if f not in parc_labels ]

	# merge missing labels
	labels_not_in = labels_not_in_json + labels_not_in_parc

	# add discard labels
	remove_labels = labels_not_in + discard_labels

	# drop labels from labels_json
	labels_json_reduced = [ f for f in labels_json if str(f['voxel_value']) not in remove_labels ]

	# remove labels from parc
	parc_data = parc.get_fdata()
	for i in remove_labels:
		parc_data[parc_data == np.int(i)] = 0
	output_img = nib.Nifti1Image(parc_data, parc.affine, parc.header)

	# save nifti
	nib.save(output_img,'./output/parc.nii.gz')

	# write out json
	with open('./output/label.json','w') as output_labels:
		json.dump(labels_json_reduced,output_labels)

def main():
	
	# make output directory
	if ~os.path.isdir('output'):
		os.mkdir('output')

	# load configs
	with open('config.json','r') as config_f:
		config = json.load(config_f)

	# set discard labels
	discard_labels = config['discard_labels'].split()

	# load labels json
	with open(config['labels'],'r') as labels_f:
		labels_json = json.load(labels_f)

	# extract labels from labels.json
	labels_json_labels = [ str(f['voxel_value']) for f in labels_json ]

	# load parcellation
	parc = nib.load(config['parcellation'])

	# clean parcellation
	clean_parcellation(parc,labels_json,labels_json_labels,discard_labels)

if __name__ == '__main__':
	main()
