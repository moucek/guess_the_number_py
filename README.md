# guess_the_number_py

we need the following packages 
- odml  converter - https://github.com/G-Node/python-odml/tree/master/odml/scripts/odml_to_rdf 
- nixio Python bindings for NIX - https://github.com/G-Node/nixpy documentation and stable version  - https://pypi.org/project/nixio/1.5.0b1/ - 
- odml https://github.com/G-Node/python-odml - open metadata Markup Language - file based format (XML, JSON, YAML) for storing metadata
- nix-odML converter - https://github.com/G-Node/nix-odML-converter - reads in odML / NIX files and writes the metadata structure to newly created NIX / odML file

download all and install with command "python setup.py install"

How to proceeed

- take EEG data together with metadata from EEGbase eegdatabase.kiv.zcu.cz

 - update metadata to the new odml 1.4 version using odml converter

-  create the nix file containing only odml- xml metadata from EEGGbase (that were already converted to the version 1.4) with nix-odml converter (convert_odml_to_nix)  

- add data (.eeg..vhdr,.vmrk files) to already created nix file with convert_bv_to_nix, available at https://github.com/JiriVanek/guess_the_number_py (it is a preliminary conversion from brainVision format that has to be updated)

How to update BrainVision loader/parser - look at https://github.com/mne-tools/mne-python/blob/master/mne/io/brainvision/brainvision.py
where is a loader from BrainVision format that converts data to some inner MNE stuctures, then it is necessary is to find mapping between MNE and NIX.
